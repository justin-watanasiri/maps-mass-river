# maps-mass-river

# Prerequisite: VSCode (https://code.visualstudio.com/download)

# 1. Installing Python
# Download python here: https://www.python.org/downloads/ (v3.13 recommended) and install
# Open VSCode and open a terminal (Terminal > New Terminal)
# Verify that python was installed correctly by running the following command in the terminal: "python --version"
# Terminal should repond with "Python 3.13" or something similar
# If you get an error like "python is not a recognized command" you will have to add python to your PATH
# Follow the instructions here for your OS https://realpython.com/add-python-to-path/
# Reboot your terminal after following the instructions and try running "python --version" again

# 2. Create a virtual environment
# Create a virtual environment with the following command in your terminal: "python -m venv .venv"
# Activate the virtual environment with the following command: ".\.venv\Scripts\activate"
# Activiation was successful if "(.venv)" now appears at the start of your terminal prompt

# 3. Updating pip
# In your terminal (which should be using your virtual environment) enter the following command: "python -m pip install --upgrade pip"

# 4. Ensure VSCode is using the right Python interpreter
# In VSCode open the command palette (ctrl+shift+P in windows, command+shift+P in macos)
# Start typing "Python: Select Interpreter" and select the option when it appears
# VSCode will display one or more options; choose the one with (.venv)

# 5. Downloading the code
# Navigate to this page: https://github.com/justin-watanasiri/maps-mass-river
# Click the green "<> Code" button
# Select "Download Zip" option
# Unzip folder to a location of your choosing
# In your terminal navigate to the folder you just created with "cd {filepath}" (no brackets)
# Alternatively, you can achieve the same thing as all of the above by navigating to the directory you want the folder to be inside of in your terminal and using the the following command: "git clone https://github.com/justin-watanasiri/maps-mass-river.git"

# 6. Getting an API key
# In order to run this script (which depends on the google maps/places API) you will need to create a free cloud account. A free account is good for 90 days and a $300 credit. Using this script should not get you anywhere close to the credit limit
# This page will explain how to set up a Google Cloud Project: https://developers.google.com/maps/documentation/places/web-service/cloud-setup
# This page will explain how to generate an API key (https://developers.google.com/maps/documentation/places/web-service/get-api-key)
# Once you've generated an API key create a file named "api_key.txt" in your "maps-mass-river-main" folder (the folder you unzipped in step 5) and paste the key into that file and save
# IMPORTANT: This API key should not be shared with anyone outside of your organization. Definitely make sure that it, and the api_key.txt file are not uploaded to github or any place where people outside of your organization could get access to it

# 7. Running the script
# In VSCode, open our project (maps-mass-river-main) folder (File > Open Folder)
# Open the "main.py" file
# Near the top of the file you will see a variable named "searchString". This string is what the places API will search for. Edit this variable to change the area that this script will search. Possible entries would be 'rivers Medford, MA", 'rivers Somerville, MA" etc
# To run this script, go to Run > Run without Debugging