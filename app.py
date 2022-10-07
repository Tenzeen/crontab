import os 
import sys
import time
import pandas as pd
import requests
import crontab

# load in dataset
data = pd.read_csv('https://data.cdc.gov/api/views/9mfq-cb36/rows.csv')

# get current working directory
cwd = os.getcwd()

# print cwd
print(cwd)

# get the current time
now = time.time()

# save current time as a string
nowStr = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))

# create a new file in the current working directory
with open(cwd + 'app_' + nowStr + '.txt', 'w') as f:
    f.write(str(data))
