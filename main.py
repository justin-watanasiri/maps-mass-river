import requests
from request_helpers import *

searchString = 'rivers Medford, MA'

x = searchByText(searchString)
xJSON = x.json()

#print(x.text)
print('first place found is:')
print(xJSON['places'][1])


