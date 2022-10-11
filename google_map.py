import gmplot

apikey = 'AIzaSyBEkzz6baWpUTM_DhdTcK9oTxVL0r-ZXJc' # (your API key here)
gmap = gmplot.GoogleMapPlotter(6.20020215,-75.5784848084993, 15, apikey=apikey)
gmap.draw("map.html")
  