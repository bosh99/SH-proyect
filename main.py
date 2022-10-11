import traceback
import pandas as pn
import pprint
import heapq
medellin = pn.read_csv('MedellinSH.csv', sep=';')
medellin.harassmentRisk = medellin.harassmentRisk.fillna(medellin.harassmentRisk.mean())

#------------------------------------------------------------------------------------------------------------------------#

o_unicos = medellin.origin.unique()
graph = {}

for origin in o_unicos:
    graph[origin] = []

'''
    Inside this function we take a previously created dict with every unique origin inside "medellin.csv" 
    then the function evaluates if the origin is already in the graph, if it is, append a new destination. 
    Otherwise create one.

    The condition says that if the pair origin-destination is oneway, then create a new pair that is destiantion-origin.
    Marked as _OneWay_. {origin : [(dest, sh, length),(),()]} ()
'''
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
        tup_one = (row[2],row[6],row[4])
        if row[3] in graph:
             graph[row[3]].append(tup_one)
        else:
            graph[row[3]] = [tup_one]
            
'''
    This function implements the selected algorithm, it works with a priority queue (import above) its evaluated with the 
    product of row[6](SH) and row[4](length). if cuando llegue al destino pare 
'''
def calculate_distances(graph,starting_vertex,ending_vertex):
    distances = {vertex: float('infinity') for vertex in graph} 
    path = []
    tracker = {vertex: float('infinity') for vertex in graph} 
    distances[starting_vertex] = 0

    pq = [(0,starting_vertex)]

    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_vertex == ending_vertex:
                path.append(current_vertex)
                break
        i = 0
        for neighbor in graph[current_vertex]:
            distance = current_distance + (float(graph[current_vertex][i][1])*float(graph[current_vertex][i][2]))
            neighbor_ = neighbor[0]

            if distance < distances[neighbor_]:
                distances[neighbor[0]] = distance
                tracker[neighbor] = graph[current_vertex]
                if current_vertex not in path:
                    path.append(current_vertex)
                heapq.heappush(pq, (distance, neighbor[0]))
            i+=1
    
    pprint.pprint(path)
    return distances[ending_vertex] 

def check_route():
    camino = {vertex: float('infinity') for vertex in graph} 
    
            
print(calculate_distances(graph,"(-75.5705202, 6.2106275)","(-75.570427, 6.2105879)"))

#pprint.pprint(graph["(-75.5705202, 6.2106275)"])
