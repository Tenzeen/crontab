import os 
import sys
import time
import pandas as pd
import json

# load in dataset
data = pd.read_json('https://healthdata.gov/resource/g62h-syeh.json')

# save it as a csv file
data.to_csv('healthdata')

# get the current time
now = time.time()

# save current time as a string
nowStr = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))
print('Current Time: ', nowStr)

#get current working directory
cwd = os.getcwd()

# create a new file in the current working directory
with open('/home/tenzin_tsegyal/crontab/app_' + nowStr + '.txt', 'w') as f:
    f.write(str(data))
