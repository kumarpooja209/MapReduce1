#! /usr/bin/python3


import sys
import os
from datetime import datetime

# setting "column_header" flag to False
column_header = False

for line in sys.stdin :
    #reading values from CSV file, iterates over the no. instance available in the file. 
	holidays,temp,rain,snow,clouds,weather,weather_description,date_time,traffic,date = line.rstrip(os.linesep).split(',')
    # striping double quotes from the date_time
	date = date_time.strip('"')
    # To check if header encountered.
	if column_header : 
        # converting to date object of format "%d/%m/%Y %H:%M".
		date_time = datetime.strptime(date,'%d/%m/%Y %H:%M')
        # Coverting back to string of format "%Y%m%d%H%M"
		date= datetime.strftime(date_time,'%Y%m%d%H%M')
		print('{}\t{}'.format(date,temp))
	column_header = True# updating "column_header" flag to True.
