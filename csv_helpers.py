import os
import csv
import sys


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
        print(f"File {filepath} already exists! Move this file to a different location or delete it. Exiting program.")
        sys.exit(1)


def processData(rawData, river_id):
    finishedData = []
    for loc in rawData:
        activities = extractActivities(loc)

        # Convert dictionary to string of True activities
        # If no activities are found, activity_string will be an empty string
        if activities != '':
            activity_string = ', '.join([key for key, value in activities.items() if value])
        else:
            activity_string = ''


        locData = [
            river_id,
            activity_string,
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


# This function searches the reviews for keywords/aliases that indicate the availability of a given activity.
# If no written reviews are found a manual search may be necessary.
def extractActivities(locData):
    activityList = ['hike, walk, and run', 'swimming', 'paddling', 'boating and sailing', 'fishing']
    foundActivities = {activity: False for activity in activityList}  # Initialize all activities as False

    # The alias/keywords used to search for activities in the reviews. Add/remove aliases as needed.
    hwrAlias = ['hiking', 'hike', 'hiker', 'walk', 'run', 'running', 'walking', 'stroll', 'jog', 'playground', 'trail', 'path']
    swimAlias = ['swim', 'swimming', 'swimmer', 'wade', 'wading', 'beach']
    paddlingAlias = ['paddle', 'paddling', 'kayak', 'canoe', 'canoeing', 'raft', 'rafting']
    boatingAlias = ['boat', 'boating', 'sail', 'sailing', 'surf', 'row', 'tube', 'tubing']
    fishingAlias = ['fish', 'fishing', 'cast', 'angling']
        
    # Check if reviews exist
    if 'reviews' not in locData:
        print("No reviews found for this location")
        return ''

    for review in locData['reviews']:
        # Safely get nested text
        # Not all reviews have a text field: if the reviewer didn't leave a written comment that review will not have a text field
        # If no text field is found we skip the search for that review (otherwise errors happen)
        if 'text' in review and isinstance(review['text'], dict) and 'text' in review['text']:
            review_text = review['text']['text'].lower()
        else:
            print(f"Unexpected review structure: {review}")
            continue
        
        # For each alias in an alias list we search the review text for that alias. If an alias is found we set the corresponding activity to True.
        for alias in hwrAlias:
            if alias in review_text:
                foundActivities['hike, walk, and run'] = True
                break
        for alias in swimAlias:
            if alias in review_text:
                foundActivities['swimming'] = True
                break
        for alias in paddlingAlias:
            if alias in review_text:
                foundActivities['paddling'] = True
                break
        for alias in boatingAlias:
            if alias in review_text:
                foundActivities['boating and sailing'] = True
                break
        for alias in fishingAlias:
            if alias in review_text:
                foundActivities['fishing'] = True
                break
                
    #print('foundActivities are: ', foundActivities) #optional debug info
    return foundActivities


#Takes in location data for a given river (in the form of a list of lists) and appends them to the given CSV file
def populateCSV(filename, data):
    filepath = os.path.join(os.path.dirname(__file__), "CSV_Dump", filename)
    # Check if the file exists
    if os.path.exists(filepath):
        with open(filepath, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
    else:
        print(f"File {filepath} does not exist. File should have been created but was not.")


def readCSV(filename):
    filepath = os.path.join(os.path.dirname(__file__), "CSV_Dump", filename)
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
            return data
    else:
        print(f"File {filepath} does not exist.")
        return None
    

# Given an input CSV file this function extracts just the river ID and name from each row.
def extractRiverList(data):
    riverList = []
    for row in data[1:]:  # Skip the header row
        riverList.append(row[0:2])  
    return riverList