import svgwrite
import re
import os

from settings import *

def draw(datastructure, filename='chalk.svg', style_sheet=None):
    """
    Creates SVG drawing of the given datastructure, and saves it.
    If a filename is given then the resulting drawing is saved in that file,
    otherwise the default chalk.svg is written.
    """

    try:
        dwg = svgwrite.Drawing(filename, profile='full')
        # dwg.add_stylesheet(STYLE_SHEET, title="chalk-style")

        style_sheet_content = ''
        if style_sheet is None:
            print 'css not given'
            style_sheet = os.path.dirname(os.path.abspath(__file__)) + '/' + STYLE_SHEET
        print 'style_sheet', style_sheet

        with open(style_sheet, 'r') as css_file:
            style_sheet_content = ''.join([ re.sub('\s', ' ', line) for line in css_file])
        
        dwg.defs.add( dwg.style(style_sheet_content))

        draw_ds(datastructure, dwg)

        dwg.save()
    except:
        import traceback
        traceback.print_exc()

def draw_ds(ds, dwg, x=0.0, y=0.0):

    if type(ds) is list:
        w,h = draw_iterable(ds, dwg, x, y)
    elif type(ds) is tuple:
        w,h = draw_iterable(ds, dwg, x, y)
    elif type(ds) is dict:
        w,h = draw_iterable(ds, dwg, x, y)
    elif type(ds) is int:
        w,h = draw_int(ds, dwg, x, y)
    elif type(ds) is str:
        w,h = draw_str(ds, dwg, x, y)

    return (w, h)

def draw_iterable(ds, dwg, x, y):

    g = dwg.g(class_=LIST_CLASS)

    w = 0  #GLYPH_WIDTH*len(title)
    h = PADDING  #GLYPH_HEIGHT + 2*PADDING
    ix = x+PADDING
    iy = y+PADDING  #+GLYPH_HEIGHT+MARGIN
    index_digits = len(str(len(ds)-1))

    for i,item in enumerate(ds):
        index = '%'+str(index_digits)+'d'
        index = index % i
        if type(ds) is dict:
            iw, ih = draw_list_item(item, ds[item], ds, dwg, ix, iy)
        else:
            iw, ih = draw_list_item(index, item, ds, dwg, ix, iy)
        ix += 0  # no horizontal shift
        iy += ih + MARGIN
        w = max(w, iw)
        h += ih+MARGIN

    if len(ds) > 0:
        h -= MARGIN

    # the rectangle around the contents of the list
    h += PADDING
    w += 2*PADDING
    r = None
    if type(ds) is tuple:
        r = dwg.rect(insert=(x, y), size=(w, h), rx=PADDING)
    else:
        r = dwg.rect(insert=(x, y), size=(w, h))
    g.add(r)

    dwg.add(g)

    return (w,h)


def draw_list_item(index, ds, parent_ds, dwg, x, y):

    print('drawing [%s]%s' % (index,ds))

    w = 0
    h = GLYPH_HEIGHT+2*PADDING

    g = dwg.g(class_=LIST_ITEM_CLASS)

    type_tag_margin = GLYPH_HEIGHT

    # draw the index
    gi = dwg.g(class_=LIST_INDEX_CLASS)
    index_width = GLYPH_WIDTH*len(index) + PADDING + type_tag_margin
    index_height = GLYPH_HEIGHT + 2*PADDING
    
    if type(parent_ds) is dict:
        points = []
        points.append((x+type_tag_margin,y))
        points.append((x+index_width,y))
        points.append((x+index_width,y+index_height))
        points.append((x+type_tag_margin,y+index_height))
        points.append((x,y+index_height/2))
        gi.add(dwg.polygon(points=points))
    else:
        gi.add(dwg.rect(insert=(x, y), size=(index_width, index_height)))
    
    gi.add(dwg.text(index, insert=(x+type_tag_margin, y+PADDING+GLYPH_HEIGHT)))
    g.add(gi)
    w += index_width

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