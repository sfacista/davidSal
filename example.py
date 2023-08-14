#!/usr/bin/python3

# Author:
# SomeOtherMetadata:

# Notes:


# Inputs:
## Input 1:

# Outputs:
## Output 1:

#import pandas
import json
import os
import sys

data=[]

#with open('listingsAndReviews.json', encoding="utf8") as aFile:
#    fileContents=aFile.read()

aFile = open('listingsAndReviews.json', encoding="utf8")
fileContents=aFile.read()

#print(fileContents)

aJson=json.loads(fileContents)

print('This should work and hopefully we get to here!')
##comments