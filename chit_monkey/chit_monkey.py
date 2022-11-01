import time
from bs4 import BeautifulSoup
from selenium import webdriver
import pyautogui

url = "https://monkeytype.com/"
driver = webdriver.Firefox(executable_path="geckodriver")
driver.get(url=url)

driver.find_element_by_xpath('//*[@id="cookiePopup"]/div[2]/div[2]/div[1]').click()
# driver.find_element_by_xpath('/html/body/div[8]/div[2]/div[2]/div[2]/div[1]/div/div[3]/div[2]').click()
time.sleep(2)
element = driver.find_element_by_id('words')
soup = BeautifulSoup(element.get_attribute('innerHTML'), 'html.parser')
words = soup.find_all('div', 'word')
text_block = ' '.join(word.text for word in words)

flag = True
while flag:
    try:
        pyautogui.moveTo(800, 1000)
        pyautogui.click()
        pyautogui.click()
        pyautogui.write(text_block)

        old_text_block = text_block
        search_string = old_text_block[-10:]

        element = driver.find_element_by_id('words')
        soup = BeautifulSoup(element.get_attribute('innerHTML'), 'html.parser')
        words = soup.find_all('div', 'word')
        text_block = ' '.join(word.text for word in words)
        text_block = text_block[text_block.index(search_string):].replace(search_string, '')

    except Exception:
        print(Exception)
        flag = False
        driver.save_screenshot('result.png')
