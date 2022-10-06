import gmplot


apikey = 'AIzaSyCDWgirDuFObeOnbFsHQ-2F3bW_-959U2M' # (your API key here)
gmap = gmplot.GoogleMapPlotter(37.7670, -122.4385, 13, apikey=apikey)
gmap.draw("map.html")   