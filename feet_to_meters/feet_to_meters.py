#!/usr/bin/env python3

import praw
import re

def convertToMeter(feet):
    meters = feet * 3.28084

def extractNumber(feetString): #Extracting number(#) from the regular expression: '# ft/feet' and then sending number to conversion
    feet = ''
    i = 0
    
    while(str.isdigit(feetString[i])):
        feet += feetString[i]
        i += 1

    convertToMeter(int(feet))

def findFeetRegex(comment): #Finding if there is some text saying '# ft/feet' in the comment and then sending it to extractNumber
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

def idListFill(): #Adding the id's stored in a text file to idList
    idList = []

def main():
    reddit = praw.Reddit('bot1')
    subreddit = reddit.subreddit('diariesfrom_me')
    idList = idListFill()
    
    for submission in subreddit.hot(limit = 25):
        for comment in submission.comments:
            if(comment.id() not in idList):
                #add to list file
                findFeetRegex(comment)

main()
