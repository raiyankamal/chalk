import svgwrite

def draw(datastructure):
	draw_ds(datastructure)


def draw_ds(ds, x=0.0, y=0.0, dwg=None):
	if dwg is None:
		dwg = svgwrite.Drawing('chalk.svg', profile='tiny')

	if type(ds) is list:
		for item in ds:
			px,py = (x,y)

			x,y = draw_ds(item, x, y, dwg)

			dwg.add(dwg.rect(insert=(px, py), size=(10.0, y-py), fill='rgb(50,50,50)'))

	else:
		print('drawing %s' % ds)
		dwg.add(dwg.text(str(ds), insert=(x, y), fill='red'))
		return (x,y+10)
	
	dwg.save()