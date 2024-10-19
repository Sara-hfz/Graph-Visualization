import matplotlib.pyplot as plt
import networkx as nt

class InvalidVertexError(Exception):
    pass

class graph:

    def __init__(self):
        self.vertices = self.get_vertices()
        self.edges = self.get_edges()

    def __str__(self):

        print_vertex = "graph includes vertices: "
        for vertex in self.vertices:
            if vertex is self.vertices[-1]:
                print_vertex= print_vertex + vertex
            else:
                print_vertex= print_vertex + vertex + " , "

        print_edge = "the edges are : "
        for edge in self.edges:
            if edge is self.edges[-1]:
                print_edge = print_edge + edge[0] + edge[1]
            else:                 
                print_edge = print_edge + edge[0] + edge[1] + " , " 

        return f"{print_vertex}\n{print_edge}"

    
    def get_vertices(self):

        vertexlist= input("Please Enter The Name Of Vertexes:").split() #saving vertex names in a list. the names themself can be any numeric and sequence datatype.
        return vertexlist
        #the vertex inputs aren't duplicate. 
        #match the name pattern?
        #I should try to raise an exceotion if the user input is unsupported(like a,b,c-)
        


    def get_edges(self):

        edgelist={} # save the adjacent verticess of each node and then build the edges -> use a dictionary.

        for vertex in self.vertices:#this is where there may be error if the entered adjacent nodes are not in the 
            #vertex list or written in the wrong format for example if the user enters ab and not a vertex name that has been entered

            edgelist[vertex]=[]
            print(f'Please Enter The Adjacent Vertices Of {vertex} or press enter if you entered all the adjacent vertices.')
            while True:
                user_input=input().strip()
                
                if user_input=="":  
                    break

                try:
                    if user_input in self.vertices:
                        edgelist[vertex].append(user_input)
                    else:
                        raise InvalidVertexError("Invalid Input For The Edge. The Start And End Node Must Be In The Vetices You Entered.")

                except InvalidVertexError:
                    print("invalid edge. enter the correct adjacent node again or press enter for  going to the nect vertex.")

        
        edges=[] #saving the edges in ready made list for easier usage and readability. 
        for key in edgelist:
            for value in edgelist[key]:
                if (value,key) not in edges: #add edge only if it's not already in the dges to avoid duplicates of edges.
                    edges.append((key,value)) # edge data type is tuple so we can't change it.

        return edges
    
        #edges are between two vertices in the list and any two random name.
        #the edges aren't dupliacate.
        #allowing several different user input format. like either entering the adjact list of every vertex. or entering the edge name only
        #or entering the two end node of the edge.
        
def draw_graph():
    g= graph()
    gr= nt.Graph()
    gr.add_nodes_from(g.vertices)
    gr.add_edges_from(g.edges)
    nt.draw(gr, pos= nt.circular_layout(gr), with_labels=True, node_color='skyblue', node_size= 50, font_size= 5, font_weight="bold")
    plt.show()


g = graph()
print(g)


