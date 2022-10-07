import os 
import sys
import time
import pandas as pd
import requests
import crontab

# load in dataset
data = pd.read_json('https://healthdata.gov/resource/g62h-syeh.json')

# save it as a csv file
data.to_csv('csv/healthdata', index = None)

# get current working directory
cwd = os.getcwd()

# print cwd
print(cwd)

# get the current time
now = time.time()

# save current time as a string
nowStr = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))

# create a new file in the current working directory
with open(cwd + '/home/tenzin_tsegyal/crontab/app_' + nowStr + '.txt', 'w') as f:
    f.write(str(data))
