import requests
from request_helpers import *
from csv_helpers import *

searchString = 'Assonet River activities MA'

results = searchByText(searchString)
resultsJSON = results.json()

# print('first place found is:')
# print(resultsJSON['places'][1])

#print('all place info is')

createCSV('test.csv')
liveData = processData(resultsJSON['places'])
populateCSV('test.csv', liveData)
