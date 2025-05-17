 #maps-mass-river

 Prerequisite: VSCode (https://code.visualstudio.com/download)

 # Installing Python
1. Download python here: https://www.python.org/downloads/ (v3.13 recommended) and install
2. Open VSCode and open a terminal (Terminal > New Terminal)
3. Verify that python was installed correctly by running the following command in the terminal: "python --version"
4. Terminal should repond with "Python 3.13" or something similar
5. If you get an error like "python is not a recognized command" you will have to add python to your PATH
6. Follow the instructions here for your OS https://realpython.com/add-python-to-path/
7. Reboot your terminal after following the instructions and try running "python --version" again

# Create a virtual environment
1. Create a virtual environment with the following command in your terminal: "python -m venv .venv"
2. Activate the virtual environment with the following command: ".\.venv\Scripts\activate"
3. Activiation was successful if "(.venv)" now appears at the start of your terminal prompt

# Updating pip
1. In your terminal (which should be using your virtual environment) enter the following command: "python -m pip install --upgrade pip"

# Ensure VSCode is using the right Python interpreter
1. In VSCode open the command palette (ctrl+shift+P in windows, command+shift+P in macos)
2. Start typing "Python: Select Interpreter" and select the option when it appears
VSCode will display one or more options; choose the one with (.venv)

# Downloading the code
1. Navigate to this page: https://github.com/justin-watanasiri/maps-mass-river
2. Click the green "<> Code" button
3. Select "Download Zip" option
4. Unzip folder to a location of your choosing
5. In your terminal navigate to the folder you just created with "cd {filepath}" (no brackets)

Alternatively, you can achieve the same thing as steps 1-5 by navigating to the directory you want the folder to be inside of in your terminal and using the the following command: "git clone https://github.com/justin-watanasiri/maps-mass-river.git"

# Getting an API key
1. In order to run this script (which depends on the google maps/places API) you will need to create a free cloud account. A free account is good for 90 days and a $300 credit. Using this script should not get you anywhere close to the credit limit 
2. This page will explain how to set up a Google Cloud Project: https://developers.google.com/maps/documentation/places/web-service/cloud-setup
3. This page will explain how to generate an API key (https://developers.google.com/maps/documentation/places/web-service/get-api-key)
4. Once you've generated an API key create a file named "api_key.txt" in your "maps-mass-river-main" folder (the folder you unzipped in the Downloading the Code section) and paste the key into that file and save

IMPORTANT: This API key should not be shared with anyone outside of your organization. Definitely make sure that it, and the api_key.txt file are not uploaded to github or any place where people outside of your organization could get access to it

# Running the script
1. In VSCode, open our project (maps-mass-river-main) folder (File > Open Folder)
2. Open the "main.py" file
3. Near the top of the file you will see a variable named "searchString". This string is what the places API will search for. Edit this variable to change the area that this script will search. Possible entries would be 'rivers Medford, MA", 'rivers Somerville, MA" etc
4. To run this script, go to Run > Run without Debugging