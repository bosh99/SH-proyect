from os import sep
from tokenize import Double
import pandas as pn
import pprint
import heapq
from collections import deque

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
                tracker[neighbor_] = current_vertex
                if current_vertex not in path:
                    path.append(current_vertex)
                heapq.heappush(pq, (distance, neighbor[0]))
            i+=1
    
    print(distances[ending_vertex])
    return tracker 

def check_route(track, current, camino = deque()):
    if track[current] == float('infinity'):
        camino.appendleft(current)
        return camino
    else:
        camino.appendleft(current)
        return check_route(track, track[current], camino)

def fix_path(camino = deque()):
    new_camino = []

    for element in range(len(camino)):
        coord_ = camino.popleft()
        coord = "{1},{0}".format(*coord_.split(',')).replace("(","").replace(")","").strip()
        splited_cord = coord.split(",")
        tup = (float(splited_cord[0])),float(splited_cord[1])
        new_camino.append(tup)

    return new_camino


destino_ = "(-75.6088979, 6.2324933)" #Universidad de medellin !!!
origen_ = "(-75.5808252, 6.2339338)"

dist = calculate_distances(graph,origen_,destino_)
route = check_route(dist,destino_)
print(route)
grafico = fix_path(route)
print(grafico)
#pprint.pprint(graph["(-75.5705202, 6.2106275)"])
