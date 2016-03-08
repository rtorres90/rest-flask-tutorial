import httplib2
import json

def getGeolocation(inputString):
	google_api_key = "AIzaSyDp-QUsqFaBLlXJ7jKs14deEDSNCYKdQFM"
	location_string = inputString.replace(" ", "+")
	url = ("https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (location_string, google_api_key))
	h = httplib2.Http()
	result = json.loads(h.request(url,'GET')[1])
	latitude = result['results'][0]['geometry']['location']['lat']
	longitude = result['results'][0]['geometry']['location']['lng']
	return latitude, longitude