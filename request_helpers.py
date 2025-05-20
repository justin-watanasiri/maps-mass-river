import requests
from endpoints import *
from auth import get_api_key

apiKey = get_api_key('api_key.txt')

def searchNearby():
    headers = {
        'Content-Type': 'application/json',
        'X-Goog-Api-Key': apiKey,
        'X-Goog-FieldMask': 'places.displayName,places.location'
    }

    payload = {
    'locationRestriction': {
        'circle': {
            'center': {
                'latitude': 37.7749,
                'longitude': -122.4194
            },
            'radius': 100.0
        }
    }
}
    return requests.post(url=urlSearchNearby, headers=headers, json=payload)
    

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