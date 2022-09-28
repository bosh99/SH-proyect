import pandas as pn

medellin = pn.read_csv('MedellinSH.csv', sep=';')
medellin.harassmentRisk = medellin.harassmentRisk.fillna(medellin.harassmentRisk.mean())

#--------------------------------------------------------------------------------------------------#

o_unicos = medellin.origin.unique()
graph = {}
i = 0

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
