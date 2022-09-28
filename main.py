import pandas as pn

medellin = pn.read_csv('MedellinSH.csv', sep=';')
medellin.harassmentRisk = medellin.harassmentRisk.fillna(medellin.harassmentRisk.mean())

#--------------------------------------------------------------------------------------------------#

o_unicos = medellin.origin.unique()
graph = {}
i = 0

'''
for i in range(3):
    print(O_unicos[i])
    print(medellin[medellin.origin == O_unicos[i]]["harassmentRisk"])

g_nodes = {}
for i in range(2):
    if O_unicos[i] in g_nodes:
        g_nodes[O_unicos[i]].append(medellin[medellin.origin == O_unicos[i]]["destination"])
    else:
        g_nodes[O_unicos[i]] = medellin[medellin.origin == O_unicos[i]]["destination"] 

print(g_nodes)

graph = {}
H_risk = medellin.harassmentRisk
length = medellin.length 
way = medellin.oneway
for i in range(2):
    graph[H_risk[i],length[i],way[i]] = g_nodes[O_unicos[i]]


graph_nodes = g_nodes.items()
for item in graph_nodes:
    print(item)

graph_nodes = graph.items()
for item in graph_nodes:
    print(item)
    print(" ")

print(o_unicos)
for origin in o_unicos:
    graph[origin] = []


for row in medellin.itertuples():
    s_harassament = row[6]
    length = row[4]
    if i < len(o_unicos):
        origen = graph[o_unicos[i]]
        i+=1

    destination = {row[3] : (s_harassament, length) }
    origen.update(destination)


'''


for origin in o_unicos:
    graph[origin] = []


for row in medellin.itertuples():
    s_harassament = row[6]
    length = row[4]
    origenes = row[2]
    destination = (row[3],row[6],row[4])
    origen = graph[origenes]
    if origenes in graph:
        origen.append(destination)
    else:
        origen = destination
        
    if row[5] == True:
        tup_one = ("_OneWay_",row[2],row[6],row[4])
        if row[3] in graph:
             graph[row[3]].append(tup_one)
        else:
            graph[row[3]] = [tup_one]
            
        
print(graph["(-75.5686884, 6.2063927)"])
