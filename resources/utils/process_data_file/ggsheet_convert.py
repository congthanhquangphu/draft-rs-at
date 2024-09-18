#!pip3 install gspread
#!pip3 install --upgrade google-api-python-client oauth2client

#importing the required libraries
import os
import csv
import gspread
import pandas as pd
from google.oauth2.service_account import Credentials

# define the scope
SCOPES = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = Credentials.from_service_account_file('rs-emagics-4792a5622505.json',scopes=SCOPES)

# authorize the clientsheet 
client = gspread.authorize(creds)


# get the instance of the Spreadsheet
sheet = client.open_by_key('1b0D_Cvsp01aGGJVDZBcVan50yDPz-MpayhIBp2UGHEk')

# get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(0)

def store_to_csv(sheet_instance, sheet_name):
    # Get the current script's directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the path to the data/csv folder
    csv_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))), 'data', 'csv')
    
    # Create the csv folder if it doesn't exist
    os.makedirs(csv_folder, exist_ok=True)
    
    # Create the full path for the CSV file
    csv_file_path = os.path.join(csv_folder, f"{sheet_name}.csv")
    
    # Get all values from the sheet
    data = sheet_instance.get_all_values()
    
    # Write the data to the CSV file
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    
    print(f"Data stored in {csv_file_path}")

# Example usage
sheet_name = sheet_instance.title
store_to_csv(sheet_instance, sheet_name)

# If you want to store all sheets in the spreadsheet
for worksheet in sheet.worksheets():
    store_to_csv(worksheet, worksheet.title)