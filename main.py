from request_helpers import *
from csv_helpers import *

# Use this file to perform a bulk search. 

# Modify the inputCSV variable to control which input CSV file is used. Script expects the CSV file to be in the CSV_Dump directory.
# The input CSV file should be in the format of the 'rivers' table in supabase. 
# It mainly cares that the river ID is in the first column and the river name is in the second column.
# I've included a sample CSV file called river_rows_sample.csv in the CSV_Dump directory.

# For each row in the input CSV the script will perform a search using the river name and the searchModifier variable.
# Therefore, modify the searchModifier variable to control what search string is used.

# The output file(s) will be created in the CSV_Dump directory as river_name.csv.
# Script will check to see if an output file for a given river already exists. 
# If it does, the script will exit and prompt you to move or delete the file.
# This is because otherwise the script would add the current search results to the existing file which would result in duplicate data.

inputCSV = 'river_rows_sample.csv'
searchModifier = 'activities MA'

riverList = extractRiverList(readCSV(inputCSV))
for river in riverList:
    riverName = river[1]
    riverID = river[0]

    searchString = riverName + ' ' + searchModifier
    print('Now Processing: ', riverName)
    results = searchByText(searchString)
    resultsJSON = results.json()

    csvName = riverName + '.csv'
    createCSV(csvName)
    liveData = processData(resultsJSON['places'], riverID)
    populateCSV(csvName, liveData)
