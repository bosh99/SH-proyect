import gmplot
from main import *



apikey = 'AIzaSyBEkzz6baWpUTM_DhdTcK9oTxVL0r-ZXJc' # (your API key here)
gmap = gmplot.GoogleMapPlotter(6.20020215,-75.5784848084993, 15, apikey=apikey)
gmap.draw("map.html")

path = zip(*grafico)

gmap.plot(*path, edge_width=7, color='red')
gmap.draw('map.html')