import time
import os
import platform
import logging
import base64

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import ddddocr


logger = logging.getLogger()

def getVertificationCodeImgBase64(driver):
    captcha = driver.execute_async_script(
        """
        var canvas = document.createElement('canvas');
        var context = canvas.getContext('2d');
        var img = document.querySelector('#captcha img');
        canvas.height = img.naturalHeight;
        canvas.width = img.naturalWidth;
        context.drawImage(img, 0, 0);
        
        callback = arguments[arguments.length - 1];
        callback({ 'base64': canvas.toDataURL(), 'height': img.naturalHeight, 'width': img.naturalWidth});
        """
    )
    captchaBase64 = captcha['base64']
    verificationCodeImgBase64 = base64.b64decode(captchaBase64.split(',')[1])

    return verificationCodeImgBase64

def verifyCode(img):
    ocr = ddddocr.DdddOcr()
    res = ocr.classification(img)
    print(res)

    return res



class Voter:
    def __init__(self):
        self.resetBrowser()

    def resetBrowser(self):
        try: 
            system = platform.platform().lower()
            print(system)

            if system.startswith('linux'):
                #browserPath = os.path.normpath('/opt/google/chrome/chrome')
                browserPath = 'chromedriver'
            
            elif system.startswith('windows'):
                browserPath = os.path.normpath('C:\Program Files\Google\Chrome\Application\chrome.exe')
            
            self.driver = uc.Chrome(browser_executable_path = browserPath)

        except Exception as e:
            print(e)
        
    # use google third party login
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
    
    # use peihua own login
    def loginPeiHua(self, url, email, password):
        try:
            while True:
                self.driver.get(url)
                time.sleep(1)
                verificationCodeImgBase64 = getVertificationCodeImgBase64(self.driver)
                code = verifyCode(verificationCodeImgBase64)
                if len(code) != 5:
                    continue

                self.driver.find_element(By.XPATH, '//*[@id="container"]/div/form/ul/li[1]/input').send_keys(email)
                self.driver.find_element(By.XPATH, '//*[@id="container"]/div/form/ul/li[2]/input').send_keys(password)
                self.driver.find_element(By.XPATH, '//*[@id="container"]/div/form/ul/li[3]/input').send_keys(code)
                self.driver.find_element(By.XPATH, '//*[@id="container"]/div/form/ul/li[3]/input').send_keys(Keys.ENTER)
                time.sleep(5)
                emailCheckLogin = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/form/ul[2]/li[2]/input').get_attribute('value')
                print(emailCheckLogin)
                if emailCheckLogin:
                    break

        except Exception as e:
            print(e)
            self.loginPeiHua(url, email, password)

    def vote(self, url):
        try:
            self.driver.get(url)
            self.driver.find_element(By.CLASS_NAME, 'button-2').click()
            time.sleep(3)

        except Exception as e:
            print(e)

if __name__ == '__main__':
    pass
    