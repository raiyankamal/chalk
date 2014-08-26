import svgwrite

def draw(datastructure):
	draw_ds(datastructure)


def draw_ds(ds, x=0.0, y=0.0, dwg=None):
	if dwg is None:
		dwg = svgwrite.Drawing('chalk.svg', profile='tiny')

	if type(ds) is list:
		for item in ds:
			x,y = draw_ds(item, x, y, dwg)
	else:
		print('drawing %s' % ds)
		dwg.add(dwg.text(str(ds), insert=(x, y), fill='red'))
		return (x,y+10)
	
	dwg.save()