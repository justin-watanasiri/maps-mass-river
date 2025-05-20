import requests
from request_helpers import *
from csv_helpers import *

searchString = 'Assonet River activities MA'

x = searchByText(searchString)
xJSON = x.json()

#print(x.text)
print('first place found is:')
print(xJSON['places'][1])

createCSV('test.csv')

