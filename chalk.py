import svgwrite

from settings import *

def draw(datastructure):

    dwg = svgwrite.Drawing('chalk.svg', profile='tiny')
    dwg.add_stylesheet(STYLE_SHEET, title="chalk-style")

    draw_ds(datastructure, dwg)

    dwg.save()

def draw_ds(ds, dwg, x=0.0, y=0.0):

    if type(ds) is list:
        w,h = draw_list(ds, dwg, x, y)
    elif type(ds) is int:
        w,h = draw_int(ds, dwg, x, y)
    elif type(ds) is str:
        w,h = draw_str(ds, dwg, x, y)

    return (w, h)

def draw_list(ds, dwg, x, y):

    g = dwg.g(class_=LIST_CLASS)

    w = 0  #GLYPH_WIDTH*len(title)
    h = PADDING  #GLYPH_HEIGHT + 2*PADDING
    ix = x+PADDING
    iy = y+PADDING  #+GLYPH_HEIGHT+MARGIN
    index_digits = len(str(len(ds)-1))

    for i,item in enumerate(ds):
        index = '%'+str(index_digits)+'d'
        index = index % i
        iw, ih = draw_list_item(index, item, dwg, ix, iy)
        ix += 0  # no horizontal shift
        iy += ih + MARGIN
        w = max(w, iw)
        h += ih+MARGIN

    if len(ds) > 0:
        h -= MARGIN

    # the rectangle around the contents of the list
    h += PADDING
    w += 2*PADDING
    r = dwg.rect(insert=(x, y), size=(w, h))
    g.add(r)

    # title of the list
    #t = dwg.text(title, insert=(x+PADDING, y+PADDING+GLYPH_HEIGHT))
    #g.add(t)

    dwg.add(g)

    return (w,h)


def draw_list_item(index, ds, dwg, x, y):

    print('drawing [%s]%s' % (index,ds))

    w = 0
    h = GLYPH_HEIGHT+2*PADDING

    g = dwg.g(class_=LIST_ITEM_CLASS)

    # draw the index
    gi = dwg.g(class_=LIST_INDEX_CLASS)
    gi.add(dwg.rect(insert=(x, y), size=(GLYPH_WIDTH*len(index)+2*PADDING, GLYPH_HEIGHT+2*PADDING)))
    gi.add(dwg.text(index, insert=(x+PADDING, y+PADDING+GLYPH_HEIGHT)))
    g.add(gi)
    w += GLYPH_WIDTH*len(index)+2*PADDING

    # ww, _ = draw_int(ds, dwg, '', x+w, y)
    ww, hh = draw_ds(ds, dwg, x+w, y)

    w = w + ww
    h = max(h, hh)

    dwg.add(g)

    return (w, h)

def draw_int(ds, dwg, x, y):

    print('drawing %s' % (ds))

    w = 0
    h = GLYPH_HEIGHT+2*PADDING

    # draw the int
    g = dwg.g(class_=INT_CLASS)
    g.add(dwg.rect(insert=(x+w, y), size=(GLYPH_WIDTH*len(str(ds))+2*PADDING, GLYPH_HEIGHT+2*PADDING)))
    g.add(dwg.text(str(ds), insert=(x+w+PADDING, y+PADDING+GLYPH_HEIGHT)))
    w += GLYPH_WIDTH*len(str(ds))+2*PADDING

    dwg.add(g)

    return (w, GLYPH_HEIGHT+2*PADDING)

def draw_str(ds, dwg, x, y):

    print('str:%s' % (ds))

    w = 0
    h = GLYPH_HEIGHT+2*PADDING

    # draw the int
    g = dwg.g(class_=STR_CLASS)
    g.add(dwg.rect(insert=(x+w, y), size=(GLYPH_WIDTH*len(str(ds))+2*PADDING, GLYPH_HEIGHT+2*PADDING)))
    g.add(dwg.text(str(ds), insert=(x+w+PADDING, y+PADDING+GLYPH_HEIGHT)))
    w += GLYPH_WIDTH*len(str(ds))+2*PADDING

    dwg.add(g)

    return (w, GLYPH_HEIGHT+2*PADDING)