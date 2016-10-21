#!/bin/python

import shapefile

sf = shapefile.Reader("C:/Users/Gilang Tartila/Documents/gis/negara.shp")
print sf
shapes = sf.shapes()
print len(shapes)

#for name in dir(shapes[3]):
#	if not name.startswitch('__'):
#		print name
