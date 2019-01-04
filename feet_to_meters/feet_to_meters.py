#!/usr/bin/env python3

import praw
import re

def convertToMeter(feet):
    meters = feet * 3.28084

def extractNumber(feetString):
    feet = ''
    i = 0
    
    while(str.isdigit(feetString[i])):
        feet += feetString[i]
        i += 1

    convertToMeter(int(feet))

def findFeet(comment):
    ftRegex = re.compile('[0-9]+ ft')
    feetRegex = re.compile('[0-9]+ feet')
    
    ftMatch = ftRegex.search(comment)
    feetMatch = feetRegex.search(comment)
    
    if (ftMatch == None and feetMatch == None):
        return
    
    elif (ftMatch != None):
        extractNumber(ftMatch.group())
    
    else: #means feetMatch !=None
        extractNumber(feetMatch.group())

def main():
    reddit = praw.Reddit('bot1')
    subreddit = reddit.subreddit('diariesfrom_me')
    
    for submission in subreddit.hot(limit = 25):
        for comment in submission.comments:
            findFeet(comment.body)

main()
