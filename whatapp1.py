
from selenium import webdriver
import streamlit as st
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import sys
import pyautogui
import datetime
import re
from time import *
from selenium import webdriver
from chromedriver_py import binary_path # this will get you the path variable
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com/")

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
st=time()
def eta(seconds):
    sec=seconds-st
    return "ETA: "+str(datetime.timedelta(seconds=sec))
def valid_date(datestring):
        try:
                mat=re.match('(\d{2})[/.-](\d{2})[/.-](\d{4})$', datestring)
                if mat is not None:
                        datetime.datetime(*(map(int, mat.groups()[-1::-1])))
                        return True
        except ValueError:
                pass
        return False
def scroll():
    for i in range(8):
        pyautogui.press('down')
        sleep(1)
def findmsg(name):
    sleep(2);partial=0
    try:
        driver.find_element_by_class_name('_1ays2').click()
    except:
        return None
    sleep(2)
    for i in range(40):
        sleep(1)
        pyautogui.press('up')
    msg=[name];prev='Unknown';
    sleep(8)
    htmlcode=(driver.page_source).encode('utf-8')
    soup = BeautifulSoup(htmlcode,features="html.parser")
    cnt=0
    for tag in soup.find_all('span'):
        classid=tag.get('class')
        if classid==['_F7Vk', 'selectable-text', 'invisible-space', 'copyable-text']:
            msg.append([tag.text.translate(non_bmp_map).replace('\n', '')])
        if classid==['_3fnHB']:
            try:
                if msg[-1][-1] in [1,2]:
                    msg[-1].append(tag.text)
            except:
                par
                tial=1
        if classid in [['EopGb', '_3HIqo'],['EopGb']]:
            try:
                msg[-1].append(len(classid))
            except:
                partial=1
        if classid == ['_F7Vk']:
            try:
                if tag.text in ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY', 'TODAY', 'YESTERDAY'] or valid_date(tag.text):
                    msg[-1].append(tag.text)
            except:
                if tag.text in ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY', 'TODAY', 'YESTERDAY'] or valid_date(tag.text):
                    prev=tag.text
                partial=1
    for i in msg:
        if len(i)>4:
            i=i[:4]
    
    for i in msg[1:]:
        if len(i)==3:
            i.append(prev)
        else:
            prev=i[-1]
    chats.append(msg)
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
sleep(13)
chats=[]
print("Chrome has been automated",eta(time()))

match=dict()
for i in contact:
    match[i.lower()]=i
contacts=[i.lower() for i in contact]
for i in range(len(contacts)):
    cnt=0
    for j in range(i):
        if contacts[i] in contacts[j]:
            cnt+=1
    rotate[match[contacts[i]]]=cnt
driver.find_element_by_class_name('qfKkX').click()
sleep(2)
scrap=0
for i in contact:
    driver.find_elements_by_class_name('_3j8Pd')[1].click()
    sleep(2)
    driver.find_element_by_class_name('_1XCAr').click()
    pyautogui.typewrite(i)
    sleep(2)
    for j in range(rotate[i]+1):
        pyautogui.press('down')
    pyautogui.press('enter')
    findmsg(i)
    try:
        driver.find_element_by_class_name('_1XCAr').click()
    except:
        pyautogui.press('esc')
        driver.find_element_by_class_name('_1XCAr').click()
    scrap+=1
    if scrap==1:
        print('['+i,"Success",eta(time()),end='')
    elif scrap==len(contact):
        print(','+i,"Success"+eta(time())+']')
    else:
        print(','+i,"Success",eta(time()),end='')