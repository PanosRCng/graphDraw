#
#	graphDraw module
#
#	 
#	draws the graph
#


try:
	from PygameFrame import PygameFrame
except ImportError:
	print 'graphDraw -- (!) module do not found '	
	exit()


def draw(graph):

	pygameFrame = PygameFrame(graph)

	pygameFrame.loop()
