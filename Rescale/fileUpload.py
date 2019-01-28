'''
@author: siddardha.teegela
'''

import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions, Chrome
import autoit

def rescale_upload():
    user = "xxxxxx"
    pwd = "xxxxxx"
    
    # For Chrome
    opts = ChromeOptions()
    opts.add_experimental_option("detach", True)
    
    driver = webdriver.Chrome("<chromedriver-path>",options=opts)
    driver.get("https://platform.rescale.com/")
    
    #Find login
    element = driver.find_element_by_id("id_username")
    element.send_keys(user)
    
    element = driver.find_element_by_id("id_password")
    element.send_keys(pwd)
    
    element.send_keys(Keys.RETURN)
    
    time.sleep(3)
    #file_click = driver.find_element_by_id("menuFiles")
    file_click = driver.find_element_by_xpath("//*[@id='menuFiles']/a")
    file_click.click()
    
    time.sleep(10)
    
    try:
        upload_file = driver.find_element_by_xpath("//*[@id='filesPageDropZone']")
        upload_file.click()
        time.sleep(5)
        autoit.win_active("Open")
        autoit.control_send("Open", "Edit1",r"<file-path>")
        autoit.control_send("Open","Edit1","{ENTER}")
    except Exception as e:
        print('Could not upload file')
    
    time.sleep(50)
    
    #driver.close()

if __name__ == '__main__':
    #pass
    rescale_upload()
