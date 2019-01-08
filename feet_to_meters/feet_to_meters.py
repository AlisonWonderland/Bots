#!/usr/bin/env python3

import praw
import re
import os

def convertToMeter(feet):
    meters = feet * 3.28084
    return meters

def extractNumber(feetString): #Extracting number(#) from the regular expression: '# ft/feet' and then sending number to conversion
    feet = ''
    i = 0
    
    while(str.isdigit(feetString[i])):
        feet += feetString[i]
        i += 1

    return convertToMeter(int(feet))

def findFeetRegex(comment): #Finding if there is some text saying '# ft/feet' in the comment and then sending it to extractNumber
    ftRegex = re.compile('[0-9]+ ft')
    feetRegex = re.compile('[0-9]+ feet')
    
    ftMatch = ftRegex.search(comment)
    feetMatch = feetRegex.search(comment)
    
    if (ftMatch == None and feetMatch == None): 
        return
    
    elif (ftMatch != None):
       return extractNumber(ftMatch.group())
    
    else: #means feetMatch !=None
        return extractNumber(feetMatch.group())

def idListFill(): #Adding the id's stored in a text file to idList
    if not os.path.isfile("comments_replied_to.txt"):
        idList = []
    
    else:
        with open("comments_replied_to.txt", "r") as f:
            idList = f.read()
            idList = idList.split("\n")
            idList = list(filter(None, idList)) #Making sure  there are no empty values stored in the list
    
    return idList
    
def main():
    reddit = praw.Reddit('bot1')
    subreddit = reddit.subreddit('diariesfrom_me')
    idList = idListFill()
    
    for submission in subreddit.hot(limit = 25):
        for comment in submission.comments:
            if(comment.id not in idList):
                comment.reply(findFeetRegex(comment.body)) #add returns to functions
                idList.append(comment.id)
    
    with open("comments_replied_to.txt", "w") as f:
        for comment_id in idList:
            f.write(comment_id + "\n")

main()
