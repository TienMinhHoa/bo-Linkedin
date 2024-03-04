import time
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import re
from BaseConnection import GetConnect
from BaseConnection import log

def ConnectToLinkedin():
    connection = GetConnect("https://www.linkedin.com","https://www.linkedin.com/feed/?trk=homepage-basic_sign-in-submit",3)
    connection.getConnection()
    return connection

def ClickButton(source,connection,by):
    ## Click on the post button
    try:
        connection.findElement(by,source)
        connection.element.click()
    except Exception as e:
        log(e)

def sendKeys(source,connection,text,by):
    ## Send keys to the text box
    try:
        connection.findElement(by,source)
        connection.element.send_keys(text)
    except Exception as e:
        log(e)
        

if __name__ == "__main__":
    i = int(input())
    connection = ConnectToLinkedin()
    time.sleep(connection.global_delay)
    
    for _ in range(i):
        buttonShare = "share-box-feed-entry__trigger"
        buttonAddImage = "/html/body/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div/section/div[2]/ul/li[2]/div/div/span/button/span"
        buttonNext = "/html/body/div[3]/div/div/div/div[2]/div/div/div[2]/div/button[2]"
        buttonPost = "/html/body/div[3]/div/div/div/div[2]/div/div/div[2]/div[4]/div/div[2]/button"
        
        textBox = "ql-editor"
        imageSource = "media-editor-file-selector__file-input"
        
        
        ClickButton(buttonShare,connection,"class name")
        time.sleep(connection.global_delay)
        
        ClickButton(buttonAddImage,connection,"xpath")
        time.sleep(connection.global_delay)
        
        sendKeys(imageSource,connection,"D:/Temp/bot-linkedin/maxresdefault.jpg","id")
        time.sleep(connection.global_delay)
        
        ClickButton(buttonNext,connection,"xpath")
        time.sleep(connection.global_delay)
        
        sendKeys(textBox,connection,"emaidasfdasl","class name")
        time.sleep(connection.global_delay)
        
        ClickButton(buttonPost,connection,"xpath")
        time.sleep(connection.global_delay)
        
        
        window = tk.Tk()
        window.title("Twitter Follow and Tweet Bot")
        window.geometry("400x350")
        window.mainloop()