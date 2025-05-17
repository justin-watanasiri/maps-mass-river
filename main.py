import requests
from request_helpers import *

x = searchByText('rivers Medford, MA')
xJSON = x.json()

#print(x.text)
print('first place found is:')
print(xJSON['places'][1])


