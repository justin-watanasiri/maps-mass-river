import os
import csv


def createCSV(filename):
    # Create data directory if it doesn't exist
    data_dir = os.path.join(os.path.dirname(__file__), 'CSV_Dump')
    os.makedirs(data_dir, exist_ok=True)
    
    # Create full filepath
    filepath = os.path.join(data_dir, filename)

    if not os.path.exists(filepath):
        with open(filepath, 'w', newline='') as file:
            writer = csv.writer(file)
            # Define your headers
            headers = ['river_id', 'activity', 'name', 'town', 'address', 'description', 'google-map', 'link', 'image', 'latitude', 'longitude']
            # Write headers to the CSV file
            writer.writerow(headers)
            # ...create new file logic...
            pass
    else:
        print(f"File {filepath} already exists")

def processData(rawData):
    finishedData = []
    for loc in rawData:
        locData = [
            '',  # river_id to be filled in later
            '',  # activity to be filled in later
            loc['displayName']['text'],
            loc['formattedAddress'].split(',')[1].strip(),  # townName
            loc['formattedAddress'],
            '',  # Description left blank
            loc['googleMapsLinks']['placeUri'],
            '',  # Link left blank
            '',  # Image left blank
            loc['location']['latitude'],
            loc['location']['longitude']
        ]
        finishedData.append(locData)
        # Optional debug info
        #print('locData is: ', locData)
    #print('finishedData is: ', finishedData)
    return finishedData

#Takes in an array of arrays and appends it to the CSV file. Example:
#[['1', 'activity', 'Assonet River', 'Freetown', 'Assonet River, Freetown, MA 02702, USA', 'description', 'google-map', 'link', 'image', '41.79', '-71.06'],
#['2', 'activity2', 'Assonet River2', 'Freetown2', 'Assonet River2, Freetown2, MA 02702, USA', 'description2', 'google-map2', 'link2', 'image2', '41.79', '-71.06']]
def populateCSV(filename, data):
    filepath = os.path.join(os.path.dirname(__file__), "CSV_Dump", filename)
    # Check if the file exists
    print('filepath is: ', filepath)
    if os.path.exists(filepath):
        with open(filepath, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
    else:
        print(f"File {filepath} does not exist. Please create it first.")