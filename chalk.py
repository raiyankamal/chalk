import svgwrite

from settings import *

def draw(datastructure):
    draw_ds(datastructure)


def draw_ds(ds, x=0.0, y=0.0, dwg=None):
    if dwg is None:
        dwg = svgwrite.Drawing('chalk.svg', profile='tiny')
        dwg.add_stylesheet(STYLE_SHEET, title="chalk-style")

    if type(ds) is list:
        w,h = draw_list(ds, 'title', x, y, dwg)

    
    dwg.save()

def draw_list(ds, title, x, y, dwg):

    g = dwg.g(class_=LIST_CLASS)

    w = GLYPH_WIDTH*len(title)
    h = GLYPH_HEIGHT + 2*PADDING
    ix = x+PADDING
    iy = y+2*PADDING+GLYPH_HEIGHT+MARGIN
    index_digits = len(str(len(ds)-1))

    for i,item in enumerate(ds):
        index = '%'+str(index_digits)+'d'
        index = index % i
        iw, ih = draw_list_item(index, item, ix, iy, dwg)
        ix += 0  # no horizontal shift
        iy += ih + MARGIN
        w = max(w, iw)
        h += ih+MARGIN

    h += PADDING
    r = dwg.rect(insert=(x, y), size=(w+2*PADDING, h))
    g.add(r)

    t = dwg.text(title, insert=(x+PADDING, y+PADDING+GLYPH_HEIGHT))
    g.add(t)

    dwg.add(g)

    return (w,h)


def draw_list_item(index, ds, x, y, dwg):

    print('drawing [%s] %s' % (index,ds))

    w = 0
    h = GLYPH_HEIGHT+2*PADDING

    g = dwg.g(class_=LIST_ITEM_CLASS)

    # draw the index
    gi = dwg.g(class_=LIST_INDEX_CLASS)
    gi.add(dwg.rect(insert=(x, y), size=(GLYPH_WIDTH*len(index)+2*PADDING, GLYPH_HEIGHT+2*PADDING)))
    gi.add(dwg.text(index, insert=(x+PADDING, y+PADDING+GLYPH_HEIGHT)))
    g.add(gi)
    w += GLYPH_WIDTH*len(index)+2*PADDING

    # draw the value
    gt = dwg.g(class_=TEXT_CLASS)
    gt.add(dwg.rect(insert=(x+w, y), size=(GLYPH_WIDTH*len(str(ds))+2*PADDING, GLYPH_HEIGHT+2*PADDING)))
    gt.add(dwg.text(str(ds), insert=(x+w+PADDING, y+PADDING+GLYPH_HEIGHT)))
    g.add(gt)
    w += GLYPH_WIDTH*len(str(ds))+2*PADDING
    w += PADDING

    dwg.add(g)

    return (w, GLYPH_HEIGHT+2*PADDING)