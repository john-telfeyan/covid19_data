#!/usr/bin/env python
# coding: utf-8

"""
Synopsis: Download manually enterd data from google sheets so it can be pushed to git as CSVs

Created:  4/8/2020
Sources:  https://gspread.readthedocs.io/en/latest/user-guide.html#opening-a-spreadsheet
          https://www.danielecook.com/from-pandas-to-google-sheets/
          https://df2gspread.readthedocs.io/en/latest/examples.html
          
Author:   John Telfeyan
          email: https://bit.ly/3aSlS9K
          
Distribution: EPL-2.0
         
"""

import configparser
from datetime import datetime
from df2gspread import gspread2df as g2d
import gspread
import json
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

if __name__=="__main__":

    # Get sheet auth key and spreadsheet info
    config = configparser.ConfigParser()
    config.read('config/gsheet_config.ini')
    spreadsheet_key = config['covid19_hospitalizations_gsheet']['worksheet_key']
    credentials_path = config['covid19_hospitalizations_gsheet']['credentials_path']
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    # Open sheet and get metadata
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
    gc = gspread.authorize(credentials)
    workbook = gc.open_by_key(spreadsheet_key)
    date_tag = datetime.now().strftime("%Y-%m-%d-%H%M")
    ignore_sheets  = ['Instructions', 'test']
    
    # Download each sheet and convert to csv
    for sheet in workbook.worksheets():
        if sheet.title not in ignore_sheets:
            print (sheet.title)
            df = g2d.download(spreadsheet_key, credentials=credentials, wks_name=sheet.title, col_names=True, row_names=True)
            df.to_csv('data/%s.csv' % sheet.title)
            df.to_csv('data//archive//%s-%s.csv' % (date_tag, str(sheet.title)))




