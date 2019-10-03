from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

import os
import time

class InstagramBot:
    def __init__(self):
        self.instaUrl = 'https://instagram.com'
        self.email = "" if os.getenv("instaEmail") is None else os.getenv("instaEmail")
        self.pwd = "" if os.getenv("instaPwd") is None else os.getenv("instaPwd")
        self.bot = webdriver.Firefox()

    def login(self):
        try:
            self.bot.get(self.instaUrl)
            #WebDriverWait(self.bot, 10).until(EC.title_contains("Instagram"))
            time.sleep(6)
            login_link = self.bot.find_element_by_link_text('Log in')
            login_link.send_keys(Keys.RETURN)
            time.sleep(6)
            
            email = self.bot.find_element_by_name('username')
            pwd = self.bot.find_element_by_name('password')
            #login_btn = self.bot.find_elements_by_class_name('sqdOP')

            email.send_keys(self.email)
            pwd.send_keys(self.pwd)
            pwd.send_keys(Keys.RETURN)
            time.sleep(5)

            notNowBtn = self.bot.find_element_by_class_name('HoLwm')
            notNowBtn.send_keys(Keys.RETURN)
            time.sleep(1)
         
        finally:
            #self.bot.quit()
            print('logged in')

    def doSearch(self,searchText):
        '''
        search_text = self.bot.find_element_by_class_name('XTCLo')
        search_text.send_keys(searchText)
        search_text.send_keys(Keys.RETURN)
        time.sleep(2)
        search_results = self.bot.find_element_by_class_name('yCE8d')
        search_results.send_keys(Keys.RETURN)
        time.sleep(2)
        '''
        self.bot.get(self.instaUrl+'/explore/tags/'+searchText+'/')
        time.sleep(5)
        print('search completed')
    
    def doLike(self):
        img_list = self.bot.find_elements_by_tag_name('a') #('v1NH3')
        #img_list = self.bot.find_elements_by_class_name('v1NH3')
        links = [element.get_attribute('href') for element in img_list]
        i=0
        for link in links:
            if 'https://www.instagram.com/p/' in link:
                self.bot.get(link)
                time.sleep(random.randint(12,36))
                self.bot.find_element_by_class_name('dCJp8').send_keys(Keys.RETURN)
                time.sleep(random.randint(3,12))
                i+=1
                print(i)
        print(links)


        
