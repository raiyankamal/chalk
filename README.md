chalk
=====
Chalk is a Python library for vizualizing various Python data structures in SVG format. The following data structure and primitive types are supported in the current version:

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

The default output file is chalk.svg, saved at the current working directory. The output file can be specified by providing a value for the 'filename' parameter. The output is writtne in 'a.svg' in the following example:

>>> chalk.draw(my_list, 'a.svg')
