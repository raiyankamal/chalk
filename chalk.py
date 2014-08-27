import svgwrite

from settings import *

def draw(datastructure):
    draw_ds(datastructure)


def draw_ds(ds, x=0.0, y=0.0, dwg=None):
    if dwg is None:
        dwg = svgwrite.Drawing('chalk.svg', profile='tiny')
        dwg.add_stylesheet(STYLE_SHEET, title="chalk-style")

    if type(ds) is list:
        for item in ds:
            px,py = (x,y)

            x,y = draw_ds(item, x, y, dwg)


    else:
        print('drawing %s' % ds)
        
        g = dwg.g(class_=TEXT_CLASS)
        g.add(dwg.rect(insert=(x, y), size=(10.0, 2*PADDING+FONT_SIZE)))
        g.add(dwg.text(str(ds), insert=(x+PADDING, y+PADDING+FONT_SIZE)))

        dwg.add(g)

        # dwg.add(dwg.text(str(ds), insert=(x+PADDING, y+PADDING+FONT_SIZE)))
        
        return (x,y+2*PADDING+FONT_SIZE+MARGIN)
    
    dwg.save()