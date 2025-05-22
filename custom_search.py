import requests
from request_helpers import *
from csv_helpers import *

# Use this file for a custom search. You can modify the searchString variable to control what search string is used exactly.
# Change the csvName variable to change the name of the CSV file that is created. The file will be created in the CSV_Dump directory.

searchString = 'Assonet River activities MA'
csvName = 'test.csv'

results = searchByText(searchString)
resultsJSON = results.json()

createCSV(csvName)
liveData = processData(resultsJSON['places'])
populateCSV(csvName, liveData)
