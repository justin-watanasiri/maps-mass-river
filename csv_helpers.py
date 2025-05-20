import os


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