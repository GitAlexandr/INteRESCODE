import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from config import *

record = int(input("введите количество секунд которое хотите набрать: "))

# driver = webdriver.Chrome(options=options, executable_path="/Users/sasha/Desktop/gg/chromedriver")
driver = webdriver.Firefox(executable_path="geckodriver")

driver.get("https://www.invokergame.com/")

# login
driver.find_element_by_xpath('//*[@id="form1"]/div[3]/div[5]/div[2]/a/img').click() # button login steam
time.sleep(5)
login  = driver.find_element_by_xpath('//*[@id="steamAccountName"]') # input login
login.send_keys('LOGIN')
password = driver.find_element_by_xpath('//*[@id="steamPassword"]') # input password
password.send_keys('PASSWORD')
driver.find_element_by_xpath('//*[@id="imageLogin"]').click() # button login
time.sleep(5)

# start game
driver.find_element(By.XPATH, '//*[@id="GameMenu"]/div/table/tbody/tr[2]/td[1]/input').click()

body = driver.find_element(By.XPATH, "/html/body")
pyautogui.press('ENTER')

start = time.time()

# click button
while True:
    body.send_keys("QQQRD", 'QQWRD', 'QQERD', 'WWWRD', 'WWERD', 'WWQRD', 'EEERD', 'EEQRD', 'EEWRD', 'QWERD')

    end = time.time()
    if end - start > record:
        break

link = driver.find_element(By.ID, 'statsKeysPressed').get_attribute('value')
print(link)