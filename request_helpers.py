import requests
from endpoints import *
from auth import get_api_key


apiKey = get_api_key('api_key.txt')


# This function isn't used in the current version of the code but is left here for possible future use.
def searchNearby(lat, long, radius):
    headers = {
        'Content-Type': 'application/json',
        'X-Goog-Api-Key': apiKey,
        'X-Goog-FieldMask': 'places.displayName,places.location'
    }

    payload = {
    'locationRestriction': {
        'circle': {
            'center': {
                'latitude': lat,
                'longitude': long
            },
            'radius': radius
        }
    }
}
    return requests.post(url=urlSearchNearby, headers=headers, json=payload)
    

# Searches using a text query. 
# the X-Goog-FieldMask header is used to specify which fields are included in the response. 
# I've included the fields that were relevant at the time of this writing. 
# However, functionality can be expanded by adding more fields (and updating processData() in csv_helpers.py)
# A full list of fields can be found here: https://developers.google.com/maps/documentation/places/web-service/text-search#required-parameters
def searchByText(searchText):
    headers = {
        'Content-Type': 'application/json',
        'X-Goog-Api-Key': apiKey,
        'X-Goog-FieldMask': 'places.displayName,places.location,places.location,places.types,places.formattedAddress,places.googleMapsLinks,places.reviews'
    }

    payload = {
        'textQuery': searchText,

    }
    return requests.post(url=urlSearchText, headers=headers, json=payload)