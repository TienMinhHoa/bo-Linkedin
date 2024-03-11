import time
import datetime
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import re


    
# def ConnectToLinkedin():
#     connection = GetConnect("https://www.linkedin.com","https://www.linkedin.com/feed/?trk=homepage-basic_sign-in-submit",3)
#     connection.getConnection()
#     return connection

def ClickButton(source,driver,by):
    ## Click on the post button
    try:
        element = driver.find_element(by,source)
        driver.execute_script("arguments[0].click();", element)
        element.click()
    except Exception as e:
        log(e)

def sendKeys(source,driver,text,by):
    ## Send keys to the text box
    try:
        element = driver.find_element(by,source)
        element.send_keys(text)
    except Exception as e:
        log(e)
        
def readInput(start,end):
    df = pd.read_excel("tmp.xlsx")
    infos = []
    for i in range(start,end+1):
        data = df[df["ID"] ==   (i)]
        if str(data['content']).strip() == "":
            continue
        info = {}
        content = str(data['content'].values[0])
        info['content'] = content
        tag = re.split(r'[, \s \n]+',str(data['TAG'].values[0]))
        info['tag'] = tag if tag[0] != 'nan' else ""
        hashtag = re.split(r'[,\s\n]+',str(data['HASHTAG'].values[0]))
        info['hashtag'] = hashtag if hashtag[0] != 'nan' else ""
        image = (data['IMAGE'].values).tolist()
        info['image'] = image[0] if str(image[0]) != 'nan' else ""
        infos.append(info)
    return infos
global_delay = 3
def interact(driver):
    driver.get("https://www.linkedin.com/feed/?trk=homepage-basic_sign-in-submit")
    iloc_start = int(iloc_start_entry.get())
    iloc_end = int(iloc_end_entry.get())
    infos = readInput(iloc_start,iloc_end)
    buttonShare = "share-box-feed-entry__trigger"
    buttonAddImage = "/html/body/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div/section/div[2]/ul/li[2]/div/div/span/button/span"
    buttonNext = "/html/body/div[3]/div/div/div/div[2]/div/div/div[2]/div/button[2]"
    buttonPost = "/html/body/div[3]/div/div/div/div[2]/div/div/div[2]/div[4]/div/div[2]/button"
    
    textBox = "ql-editor"
    imageSource = "media-editor-file-selector__file-input"
    
    for i in range(len(infos)):
        driver.get("https://www.linkedin.com/feed/?trk=homepage-basic_sign-in-submit")
        info = infos[i]
        content = info['content']
        tags = info['tag']
        tag = ""
        for tmp in tags:
            tag+="@"+tmp+" "
        hashtags = info['hashtag']
        hashtag = ""
        for tmp in hashtags:
            hashtag+="#"+tmp+" "
        tag+="\n"
        hashtag+="\n"
        image = info['image']
        log(image)
        content = tag+hashtag+content
        if content.strip() == "nan":
            return
        ClickButton(buttonShare,driver,"class name")
        time.sleep(global_delay)
        if image!="":
            ClickButton(buttonAddImage,driver,"xpath")
            time.sleep(global_delay)
    
            sendKeys(imageSource,driver,image,"id")
            time.sleep(global_delay)
    
            ClickButton(buttonNext,driver,"xpath")
            time.sleep(global_delay)
        else:
            buttonPost = "/html/body/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/button"
        sendKeys(textBox,driver,content,"class name")
        time.sleep(global_delay)
        
        ClickButton(buttonPost,driver,"xpath")
        time.sleep(global_delay)

def log(message):
    print(message)
    ctime = datetime.datetime.now()
    with open("log.txt","a") as file:
        file.write(str(ctime) +": " +str(message) + "\n")

# connection = ConnectToLinkedin()
driver = webdriver.Chrome()
driver.get("https://www.linkedin.com")
try:
    WebDriverWait(driver, 90).until(EC.url_to_be("https://www.linkedin.com/feed/?trk=homepage-basic_sign-in-submit"))
    log("Logged in!")
except Exception as e:
    log(e)
def run():
    interact(driver)

window = tk.Tk()
window.title("Linkedin Bot")
window.geometry("400x350")


# iloc start entry
iloc_start_label = tk.Label(window, text="Starting Row:")
iloc_start_label.pack()
iloc_start_entry = tk.Entry(
    window,
    width=10,
    justify="center",
)
iloc_start_entry.pack()
# iloc end entry
iloc_end_label = tk.Label(window, text="Ending Row:")
iloc_end_label.pack()
iloc_end_entry = tk.Entry(window, width=10, justify="center")
iloc_end_entry.pack(pady=10)

# follow and tweet button
run = tk.Button(
    window, text="Run", command= run
)
run.pack(pady=10)
window.mainloop()