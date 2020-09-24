#! /usr/bin/python3


from datetime import datetime, timedelta
from decimal import *
from window import Array
import sys
import os

#window size is intialized
windowsize = int(os.environ['window_size'])
w= Array(windowsize)

for line in sys.stdin :
    try: 
        #reading the input from mapper
        date,traffic= line.rstrip(os.linesep).split('\t')
        traffic = Decimal(traffic)
        w.append(traffic)
        if w.windowfull() :
            # passing the complete window forecast value to the reducer 
            #calling sma function
            print('{}|C\t{}'.format(date,w.sma()))
        else :
            # passing the incomplete window to the reducer (at the start )
            for i in range(0,w.getwindowsize()) :
                print('{}|S\t{}'.format(date,w.get(i)))
    except Exception as e:
        print(e)
# passing date in string format
date_time = datetime.strptime(date,'%Y%m%d%H%M')    

# passing  incomplete window to the reducer (from the end)
for observation in reversed(range(1,w.getwindowsize())) :
    value = w.getall()
    date_time = date_time+timedelta(hours = 1)
    date_out = datetime.strftime(date_time,'%Y%m%d%H%M')
    for i in reversed(range(1,len(value))) :
        print('{}|E\t{}'.format(date_out,value[i]))
    w.clearlast()
