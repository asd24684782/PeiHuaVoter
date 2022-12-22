import time
import os
import platform
import logging

import undetected_chromedriver as uc

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


logger = logging.getLogger()

class Voter:
    def __init__(self):
        self.driver = self.setBrowser()

    def setBrowser(self):
        try: 
            system = platform.platform().lower()
            print(system)

            if system.startswith('linux'):
                browserPath = os.path.normpath('/opt/google/chrome/chrome')
            
            elif system.startswith('windows'):
                browserPath = os.path.normpath('C:\Program Files\Google\Chrome\Application\chrome.exe')
            
            return uc.Chrome(browser_executable_path = browserPath)

        except Exception as e:
            print(e)
        
    def loginGoogle(self, url, email, password):
        try:
            self.driver.get(url)
            time.sleep(1)
            self.driver.find_element(By.XPATH, "//input[@type='email']").send_keys(email)
            self.driver.find_element(By.XPATH, '//*[@id="identifierNext"]').click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
            self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys(Keys.ENTER)
            time.sleep(15)

        except Exception as e:
            print(e)
    
    def vote(self, url):
        try:
            self.driver.get(url)
            self.driver.find_element(By.CLASS_NAME, 'button-2').click()
            time.sleep(3)

        except Exception as e:
            print(e)


    