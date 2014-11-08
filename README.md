chalk
=====
Chalk is a Python module for vizualizing various Python data structures in SVG format. The following data structure and primitive types are supported in the current version:

* List
* Tuple
* Dictionaries

* Int
* Str

How to use
----------
Import the Chalk library, then make a drawing of your datastructure by calling the draw function.

A list is created, then a visialization is created in the following example: 

	>>> import chalk
	>>> my_list = [ x/2 if x % 2 == 0 else 3 * x + 1 for x in range(0,10) ]
	>>> chalk.draw(my_list)

The following drawing of my_list is created:

![alt_tag](https://raw.github.com/raiyankamal/chalk/master/chalk.png)

Chalk can also visualize complex datastrucutres like this list consisting of different data types including nested lists:

	>>> mixed_nested_list = [2, '22', [3], {'a': 'django', 'b': 'pyramid', 'x': 'python',}, [1, 59 ,2], (0,), (4,32,0,1,2), ['abc', 'bca', 'c', 'd']]
	>>> chalk.draw(mixed_nested_list, filename='mixed_nested_list.svg')

![alt_tag](https://raw.github.com/raiyankamal/chalk/master/mixed_nested_list.png)

### Output File ###

The default output file is chalk.svg, saved at the current working directory. The output file can be specified by providing a value for the 'filename' parameter. The output is writtne in 'a.svg' in the following example:

	>>> chalk.draw(my_list, filename='a.svg')

### Custom Styling ###

Chalk styles the output with a default Cascading Style Sheet file. The default CSS file is named chalk-style.css and can be found inside the package. You can assing your custom CSS file by setting the style_sheet parameter.

	>>> chalk.draw(my_list, style_sheet='my-css.css')

Dependencies
------------
Chalk requires [svgwrite](https://pypi.python.org/pypi/svgwrite/)