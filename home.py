# python automation for home setup
# TODO: Build in root 
#
#
#
import os 
import sys 
import time 
import gtts
from requests_html import HTMLSession 
import requests
import colorama 
from colorama import Fore
from colorama import init

init()
init(autoreset=True)




os.system(' clear ')
print(" ---> hello there <--- ")
time.sleep(1)
os.system(' clear ')
os.system(' figlet update ')
time.sleep(1)
os.system(' sudo apt-get update && sudo apt-get upgrade --full ')
time.sleep(1)
os.system(' clear ')
os.system(' mpg123 hello.mp3')
time.sleep(1)
os.system(' clear ')
os.system(' mpg123 news.mp3')
os.system(' clear ')
os.system(' mpg123 scrapecyber.mp3')
session = HTMLSession()
url = 'https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNREl5ZUY4U0FtVnVLQUFQAQ?hl=en-US&gl=US&ceid=US%3Aen'
r = session.get(url)
r.html.render(sleep=1, scrolldown=1)
articles = r.html.find('article') 
newslist = []
for item in articles:
    try:
        newsitem = item.find('h3', first=True)
        newslist.append(f"{newsitem.text}\n{newsitem.absolute_links}\n")
    except:
        pass       
print(len(newslist))          
for x in newslist:
    print(x)
time.sleep(1)
print(Fore.CYAN+"")
print("="*90)
os.system(' mpg123 scrapeG.mp3 ')
print("="*90)
url = " https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en " 
try:
    session = HTMLSession()
    response = session.get(url)
except requests.exceptions.RequestException as e:
    print(e)
r = session.get(url)
r.html.render(sleep=1, scrolldown=50)
articles = r.html.find('article') 
newslist = []
for item in articles:
    try:
        newsitem = item.find('h3', first=True)
        newslist.append(f"{newsitem.text}\n{newsitem.absolute_links}\n")
    except:
        pass        
print(len(newslist))          
for x in newslist:
    print(x)                   
os.system(' mpg123 LMK.mp3')
print("-"*90)
print(" press enter to continue ")
A = str(input(" => "))
print("-"*90)
time.sleep(1)
os.system(' clear && mpg123 discord.mp3 ')
os.system(' clear')
B = str(input(" yes/no => ")) 

if 'yes' in B:
         os.system(' mpg123 disauth.mp3 ')
         time.sleep(1)




elif 'no' in B:
          time.sleep(1)    
          print("ok")
          os.system(' clear ')


os.system(' mpg123 weather.mp3 ')
os.system(' clear ')
os.system(' weather Port Saint Lucie Florida')
time.sleep(15)
print("="*40)
os.system(' mpg123 open.mp3 ')
time.sleep(1)
os.system(' clear ')
os.system(' open https://google.com ')
os.system(' open https://youtube.com ')
os.system(' clear ')
os.system(' mpg123 end.mp3 ')
os.system(' clear ')
sys.exit()
#feelTemp()

# get time 
# then have ai speak certian voice or message after a given time or seen/scrapped time 
