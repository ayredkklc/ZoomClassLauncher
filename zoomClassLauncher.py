#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 11:51:47 2021

@author: deryakilic
"""


from webbot import Browser 
import datetime
import os
import time

def goToZoom(myTime):
    classTime301 = datetime.datetime(2021, 11, 12, 13, 9).time().hour
    classTime211 = datetime.datetime(2021, 11, 12, 14, 9).time().hour
    classTime455 = datetime.datetime(2021, 11, 12, 10, 9).time().hour
    if(myTime == classTime301):
       title = "Comp 301 class itme"
       message = "class zoom will be launched in 25 minutes"
       command = f'''
       osascript -e 'display notification "{message}" with title "{title}"'
       '''
       os.system(command)
       #wait 25 minutes
       time.sleep(25 * 60)
       web = Browser()
       web.go_to('https://unc.zoom.us/j/97164010235')
       '''path = "/Applications/zoom.us.app"
       os.system(f"open {path}")
       break''' 
       # lecture lenght
       time.sleep(60 * 60 )
    elif(myTime == classTime211):
       title = "Comp 211 class time"
       message = "class zoom will be launched in 25 minutes"
       command = f'''
       osascript -e 'display notification "{message}" with title "{title}"'
       '''
       os.system(command)
       #wait 25 minutes
       time.sleep(25 * 60)
       web = Browser()
       web.go_to('https://unc.zoom.us/j/98727621599')
       '''path = "/Applications/zoom.us.app"
       os.system(f"open {path}")
       break''' 
       time.sleep(60 * 60 )
    elif(myTime == classTime455):
       title = "Comp 455 class time"
       message = "class zoom will be launched in  60 minutes"
       command = f'''
       osascript -e 'display notification "{message}" with title "{title}"'
       '''
       os.system(command)
       #wait 25 minutes
       time.sleep(60 * 60)
       web = Browser()
       web.go_to('https://unc.zoom.us/j/92258715029')
       '''path = "/Applications/zoom.us.app"
       os.system(f"open {path}")
       break''' 
       time.sleep(60 * 60 )
    else:
       myTime = datetime.datetime.now().time().hour
       #wait an hour before going through the method again
       #because I have 1 class every hour if I dont have class 
       #this minute I wont have till anouther hour
       time.sleep(60 * 60 )
       goToZoom(myTime)
        
       
if __name__ == "__main__":
    myTime = datetime.datetime.now().time().hour
    goToZoom(myTime)
        
        
        
        



    
   