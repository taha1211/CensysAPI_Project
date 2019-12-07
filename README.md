# CensysAPI_Project
A brief use of the Censys API in a specific circumstance.
This script utilizes Censys' API and their custom Python Library in order to 
conduct a search with a custom doman and validation parameter, creating a csv of the results 
with the following guidelines:

`SHA-256 Fingerprint, Validation Start Date, Validation End Date`

The code requires a few core steps:

**1. Clone the Repo to Your Local Machine**

Since the repository is public, you're more than welcome to test the code locally, or modify it
in order to fit your own custom use-cases for future implementation.

**2.Install the required packages**

In order for the code to work seamlessly, please install the relevant packages. This can be done by
first navigating in your terminal to the repository folder and
executing the following terminal command:

`sudo pip install -r requirements.txt`

**3.Running the Python Code**
The Python script can be executed without any sort of dedicated debugger tool. In order to immediately execute,
enter the following command into the terminal:

`python Censys.py`

The script will generate an 'outputFile.csv' with the pre-selected parameters for use. If any parameters need to be changed,
the source code is heavily commented and easy to understand.
