#
#
#	graphDraw usage example
#
#

try:
	from random import randint

	from graphDraw.graph import Graph
	from graphDraw import graphDraw

except ImportError:
	print 'main -- (!) module do not found '	
	exit()



def main():

	graph = Graph()

	# some code to genarate a graph	
	vertices = []
	for i in range(0,5):
		vertices.append(str(i))		 

	for v_label in vertices:
		graph.add_vertex( v_label, randint(0,100) )

	for v_label in vertices:
		for u_label in vertices:
			if v_label != u_label:
				graph.add_edge( v_label, u_label )

	# draw the graph
	graphDraw.draw(graph)




if __name__ == "__main__":

	main()
