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
liveData = [processData(xJSON['places'][1])]
populateCSV('test.csv', liveData)



# testData = [
#     ['1', 'activity', 'Assonet River', 'Freetown', 'Assonet River, Freetown, MA 02702, USA', 'description', 'google-map', 'link', 'image', '41.79', '-71.06'],
#     ['2', 'activity2', 'Assonet River2', 'Freetown2', 'Assonet River2, Freetown2, MA 02702, USA', 'description2', 'google-map2', 'link2', 'image2', '41.79', '-71.06']
# ]





#populateCSV('test.csv', testData)

