import urllib
import json

def getCoordinates(place):
    serviceUrl = "http://maps.googleapis.com/maps/api/geocode/json?"
    address = str(place)
    try:
        url = serviceUrl + urllib.urlencode({'sensor':'true', 'address':address})
        data = urllib.urlopen(url).read()
        js = json.loads(str(data))
        lat = js["results"][0]["geometry"]["location"]["lat"]
        lng = js["results"][0]["geometry"]["location"]["lng"]
        location = js["results"][0]["formatted_address"]
        dictGeo = {"latitude":lat, "longitude":lng, "location":location}
    except Exception as e:
        print e.message
    return dictGeo
