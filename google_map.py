import gmplot
from main import *


'''
    Open the map with the Live Server Vscode extension, right click on the Html file after running 'main.py' and 'google_map.py'
'''
apikey = "Por reemplazar" # (your API key here)
gmap = gmplot.GoogleMapPlotter(6.20020215,-75.5784848084993, 15, apikey=apikey)
gmap.draw("map.html")

path = zip(*grafico)
gmap.plot(*path, edge_width=7, color='cyan')
gmap.draw('map.html')


