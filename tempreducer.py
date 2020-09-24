#! /usr/bin/python3


import os
import sys
from datetime import timedelta, datetime
from decimal import Decimal
from window import Array

#window size is initialized
windowsize = int(os.environ['window_size'])
end_value = ''

w = Array(windowsize)

print('date\tforecast')
for line in sys.stdin :
    try: 
        #reading the input form the combiner and spliting it
        key,value = line.rstrip(os.linesep).split('\t')
        date,rowtype = key.split('|')
        #reading the date in string format
        date_time = datetime.strptime(date,'%Y%m%d%H%M')
        #passing the date in date & time format to output
        date_out = datetime.strftime(date_time,'%d/%m/%Y %H:%M')
        if rowtype == 'C' : #if the it has 'C' in the input then it will be directly sent as output
            print('{}\t{}'.format(date_out,value))
        else :
            temp = Decimal(value)
            if end_value == date :
                w.append(temp)
                if w.windowfull() :
                    #sma function is called to perform prediction, in which it will have letter 'S' and 'E'
                    print('{}\t{}'.format(date_out,w.sma()))
            else :
                w.clear()
                w.append(temp)         
            end_value = date
    except Exception as e:
        print(e)
