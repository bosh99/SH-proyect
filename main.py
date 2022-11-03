import pandas as pn
import heapq
import time
from collections import deque

medellin = pn.read_csv('MedellinSH.csv', sep=';')
medellin.harassmentRisk = medellin.harassmentRisk.fillna(medellin.harassmentRisk.mean())

o_unicos = medellin.origin.unique()
graph = {}

for origin in o_unicos:
    graph[origin] = []

'''
    Inside this function we take a previously created dict with every unique origin inside "medellin.csv" 
    then the function evaluates if the origin is already in the graph, if it is, append a new destination. 
    Otherwise create one.

    The condition says that if the pair origin-destination is oneway, then create a new pair that is destiantion-origin.
'''
for row in medellin.itertuples(): #O(n)
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
    This function implements the selected algorithm, it works with a priority queue (import above) its evaluated with either the product or the addition of row[6](SH) and row[4](length).
'''
def calculate_distances(graph,starting_vertex,ending_vertex,operation):
    distances = {vertex: float('infinity') for vertex in graph} 
    path = []
    operators = {'+': lambda x,y : x+y, '*': lambda x,y: x*y, '^': lambda x,y : x*x + y*y}

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
            distance = current_distance + operators[operation](float(graph[current_vertex][i][1]),float(graph[current_vertex][i][2]))
            neighbor_ = neighbor[0]

            if distance < distances[neighbor_]:
                distances[neighbor[0]] = distance
                tracker[neighbor_] = current_vertex
                if current_vertex not in path:
                    path.append(current_vertex)
                heapq.heappush(pq, (distance, neighbor[0]))
            i+=1
    print(distances[neighbor_])
    return tracker 
'''
    Backtracking the path in order to only know the nodes that we must use in the path
'''
def check_route(track, current, camino = deque()):
    if track[current] == float('infinity'):
        camino.appendleft(current)
        return camino
    else:
        camino.appendleft(current)
        return check_route(track, track[current], camino)

'''
    This function fix the latitud and longitud of the coordinates in the CSV
'''
def fix_path(camino = deque()):
    new_camino = []

    for element in range(len(camino)):
        coord_ = camino.popleft()
        coord = "{1},{0}".format(*coord_.split(',')).replace("(","").replace(")","").strip()
        splited_cord = coord.split(",")
        tup = (float(splited_cord[0])),float(splited_cord[1])
        new_camino.append(tup)

    return new_camino

'''
    Loading bar
'''

limite = 40
def bar(segment, total, longitud):
    percent = segment / total
    completado = int(percent*longitud)
    rest = longitud - completado
    barra = f"[{'#' * completado}{'-'* rest}{percent: 2%}]"
    return barra

'''
    Function to create each path
'''

def crear_camino(graph,origen,destino,operacion):
    dist = calculate_distances(graph,origen,destino,operacion)
    route = check_route(dist,destino)
    grafico = fix_path(route) 
    return grafico

origen_ = "(-75.5778046, 6.2029412)" # Test 
destino_ = "(-75.5762232, 6.266327)" # Test

start_time = time.time()
path_1 = crear_camino(graph,origen_,destino_,'*')
path_2 = crear_camino(graph,origen_,destino_,'+')
path_3 =crear_camino(graph,origen_,destino_,'^')
print("Runtime execution => %s seconds. " % (time.time() - start_time))

'''
    Pretty print of the loading bar 
'''
for i in range(limite + 1):
    time.sleep(0.05)
    print(bar(i,limite,40), end = "\r")
print("Ready!, you can open the HTML file via Live Server :)")
