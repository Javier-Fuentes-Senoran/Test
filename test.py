from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait #(html slower)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

    ##OPTIONS#
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

    ##DRIVER
driver_path="F:\chromedriver.exe"

    ##WEB
driver=webdriver.Chrome(executable_path=driver_path,chrome_options=options)
driver.get("https://www.skyvegas.com/")
time.sleep(10)

    ##CLOSE COOKIES 
    
#XPath

#WebDriverWait(driver, 5)\
#    .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')))\
#    .click()
#time.sleep(3)       
    
#Full XPath

#WebDriverWait(driver, 5)\
#    .until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div[2]/div/div[1]/div/div[2]/div/button[3]")))\
#    .click()
#time.sleep(3)
    
#Navigating elements
    
#WebDriverWait(driver, 5)\
#    .until(EC.element_to_be_clickable((By.XPATH, "//html/body/div/div/div/div/div/div/div/button[@id='onetrust-accept-btn-handler']")))\
#    .click()
#time.sleep(3)


#Navigating elements, finding for name inside atributte,this case finding element, Acept cookies


WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH, '//html/body/div/div/div/div/div/div/div/button[contains(text(),"Acept")]')))\
    .click()
    
time.sleep(3)
    

#Gold_Frenzy_250_Current_Value=driver.find_element(By.XPATH,
#                                                  '//html/body/div/div/div/div/div/div/div/button[contains(text(),"Acept")]').text

#print(Gold_Frenzy_250_Current_Value)
    
    
