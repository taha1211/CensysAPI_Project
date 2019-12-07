# CensysAPI_Project
A brief use of the Censys API in a specific circumstance.
This script utilizes Censys' API and their custom Python Library in order to 
conduct a search with a custom doman and validation parameter, creating a csv of the results 
with the following guidelines:

`SHA-256 Fingerprint, Validation Start Date, Validation End Date`

The code requires a few core steps:

**1. Clone the Repo to Your Local Machine**

Since you've been given acces to this repository, you're more than welcome to test the code locally, or modify it
in order to fit your own custom use-cases for future implementation.

**2.Install the required packages**

In order for the code to work seamlessly, please install the relevant packages. This can be done by
first navigating in your terminal to the repository folder and
executing the following terminal command:

`sudo pip install -r requirements.txt`

**3.Running the Python Code**

Before the Python script can be executed, it requires validation entry of both the `api_id` and the `api_secret` order to immediately execute. These can both be found within the account settings of the user's Censys account, and allows for Censys' protection of data requests. Upon replacing both sections with their correct information and saving, the user should be able to enter the following command into the terminal:

`python Censys.py`

The script will generate an 'outputFile.csv' with the pre-selected parameters for use. If any parameters need to be changed,
the source code is heavily commented and easy to understand.



**Additional Info**

Any additional information can be found on the [Censys API Page](https://censys.io/api)
