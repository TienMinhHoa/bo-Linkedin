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

def log(message):
    print(message)
    ctime = datetime.datetime.now()
    with open("log.txt","a") as file:
        file.write(str(ctime) +": " +str(message) + "\n")
class GetConnect:
    def __init__(self,urlBeforeLogin,urlAfterLogin,global_delay,element = None):
        self.urlBeforeLogin = urlBeforeLogin
        self.urlAfterLogin = urlAfterLogin
        self.global_delay = global_delay
        self.driver = webdriver.Chrome()
        self.element = element
        
    def getConnection(self):
        try:
            self.driver.get(self.urlBeforeLogin)
            log("Start")
        except Exception as e:
            log(e)
        
        try:
            WebDriverWait(self.driver, 90).until(EC.url_to_be(self.urlAfterLogin))
            log("Logged in!")
            return self.driver
        except Exception as e:
            log(e)
    
    def findElement(self,by,key):
        try:
            tmp_element = self.driver.find_element(by,key)
            self.element = tmp_element
            return 1
        except Exception as e:
            log("Cannot find the element "+key)
            log(e)
    
        
            
        