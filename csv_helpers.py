import os

def createCSV(filepath):
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