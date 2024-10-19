import matplotlib.pyplot as plt
import networkx as nt



#def vetices()
vertexlist= input("Please Enter The Name Of Vertexes:").split() #saving vertex names in a list. the names themself can be any numeric and sequence datatype.
#I should try to raise an exceotion if the user input is unsupported(like a,b,c-)

#there are several ways to save the edges. if we save them in a list with format like 'AB' 
# we need to split the string to figure out the ending nodes of the edge. an easier way is to save the adjacent vertexws of each node
#and then build the edges.for the second one, we must use a dictionary.

edgelist={}
for vertex in vertexlist:#tis is where there may be error if the entered adjacent nodes are not in the 
    #vertex list or written in the wrong format for example if the user enters ab and not a vertex name that has been entered
    edgelist[vertex]=[]
    print(f'Please Enter The Adjacent Vertices Of {vertex} or type -- if you entered all the adjacent vertices.')
    while True:
        user_input=input().strip()
        if user_input=="--":
            break
        if user_input not in vertexlist:
            print("invalid edge. enter again or -- for the next node.")
        else:
            edgelist[vertex].append(user_input)

edges=[]
for key in edgelist:
    for value in edgelist[key]:
        edges.append([key,value])


gr= nt.Graph()
gr.add_nodes_from(vertexlist)
gr.add_edges_from(edges)
nt.draw(gr, pos= nt.circular_layout(gr), with_labels=True, node_color='skyblue', node_size= 50, font_size= 5, font_weight="bold")
plt.show()