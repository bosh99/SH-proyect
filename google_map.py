import gmplot
from main import *


'''
    Open the map with the Live Server Vscode extension, right click on the Html file after running 'main.py' and 'google_map.py'
'''
apikey ='' # (your API key here)
gmap = gmplot.GoogleMapPlotter(6.20020215,-75.5784848084993, 15, apikey=apikey)

path = zip(*path_1)
gmap.plot(*path, edge_width=7, color='cyan')

path_2 = zip(*path_2)
gmap.plot(*path_2, edge_width=7, color='red')

path_3 = zip(*path_3)
gmap.plot(*path_3, edge_width=7, color='green')

gmap.draw('map.html')


