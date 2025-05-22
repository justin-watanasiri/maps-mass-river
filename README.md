 # maps-mass-river

  IMPORTANT: This script doesn't know what's already in the database. Before uploading one of the CSVs created by this script check to ensure that the info in the CSV is not already present in the database in order to prevent duplicate data from being created. This would most likely happen when running this script against a river that's already been manually entered into the database.

  Prerequisite: VSCode (https://code.visualstudio.com/download)

 ## Installing Python
1. Download python here: https://www.python.org/downloads/ (v3.13 recommended) and install
2. Open VSCode and open a terminal (Terminal > New Terminal)
3. Verify that python was installed correctly by running the following command in the terminal: "python --version"
4. Terminal should repond with "Python 3.13" or something similar
5. If the command in step 3 fails try "python3 --version". If this succeeds continue to use "python3" instead of "python" while following this guide
6. If you get an error like "python is not a recognized command" you will have to add python to your PATH
7. Follow the instructions here for your OS https://realpython.com/add-python-to-path/
8. Reboot your terminal after following the instructions and try running "python --version" again

## Downloading the code
1. Navigate to this page: https://github.com/justin-watanasiri/maps-mass-river
2. Click the green "<> Code" button
3. Select "Download Zip" option
4. Unzip folder to a location of your choosing
5. In your terminal navigate to the folder you just created with "cd {filepath}" (no brackets)

## Create a virtual environment
1. Create a virtual environment with the following command in your terminal: "python -m venv .venv"
2. Activate the virtual environment with the following command: ".venv/Scripts/activate"
3. On mac, try the command "source .venv/bin/activate"
4. Activiation was successful if "(.venv)" now appears at the start of your terminal prompt

## Updating pip
1. In your terminal (which should be using your virtual environment) enter the following command: "python -m pip install --upgrade pip"

## Ensure VSCode is using the right Python interpreter
1. First, install the python extension for VSCode (View > Extensions > Search for "Python")
2. In VSCode open the command palette (ctrl+shift+P in windows, command+shift+P in macos)
3. Start typing "Python: Select Interpreter" and select the option when it appears
VSCode will display one or more options; choose the one with (.venv)

Alternatively, you can achieve the same thing as steps 1-5 by navigating to the directory you want the folder to be inside of in your terminal and using the the following command: "git clone https://github.com/justin-watanasiri/maps-mass-river.git"

## Installing requirements
1. In your terminal, run the following command: "pip install -r requirements.txt"

## Getting an API key
1. In order to run this script (which depends on the google maps/places API) you will need to create a free cloud account. A free account is good for 90 days and a $300 credit. Using this script should not get you anywhere close to the credit limit 
2. This page will explain how to set up a Google Cloud Project: https://developers.google.com/maps/documentation/places/web-service/cloud-setup
3. This page will explain how to generate an API key (https://developers.google.com/maps/documentation/places/web-service/get-api-key)
4. Once you've generated an API key create a file named "api_key.txt" in your "maps-mass-river-main" folder (the folder you unzipped in the Downloading the Code section) and paste the key into that file and save

IMPORTANT: This API key should not be shared with anyone outside of your organization. Definitely make sure that it, and the api_key.txt file are not uploaded to github or any place where people outside of your organization could get access to it

## Running the script (bulk processing)
This is the default intended way to run the script
1. In VSCode, open our project (maps-mass-river-main) folder (File > Open Folder)
2. Open the "main.py" file
3. To run this script, go to Run > Run without Debugging

## Running the script (custom search)
This is an optional way to run the script that gives the user more direct control over the search. But, it only handles on search at a time.
1. In VSCode, open our project (maps-mass-river-main) folder (File > Open Folder)
2. Open the "custom_search.py" file
3. To run this script, go to Run > Run without Debugging

## Getting updated versions of the code
In order to retrieve the latest version of the code as I make changes you'll need to use git
1. Install homebrew here: https://brew.sh/
2. Install git with "brew install git"
3. Get my latest changes with "git fetch" and then "git pull"