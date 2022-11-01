from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
import time


url = "https://store.steampowered.com/"
driver = webdriver.Chrome(executable_path="/Users/sasha/Desktop/sosiska/chromedriver")

try:
    driver.get(url=url)
    time.sleep(5)
    search = driver.find_element_by_id('store_nav_search_term')
    search.send_keys("action")
    #для одного игрока только виар

    search.send_keys(Keys.ENTER)
    time.sleep(5)
    for_one_player = driver.find_element_by_xpath('//*[@id="TagFilter_Container"]/div[3]/span[1]/span/span[1]')
    for_one_player.click()
    time.sleep(3)
    vr = driver.find_element_by_xpath('//*[@id="additional_search_options"]/div[8]/div[1]')
    vr.click()
    time.sleep(3)
    button = driver.find_element_by_xpath('//*[@id="narrow_byVR"]/div[1]/span[1]/span/span[1]')
    button.click()
    time.sleep(3)
    html = driver.find_element_by_xpath('//*[@id="advsearchform"]/div[1]/div/div[1]/div[1]/div[1]/div[1]').click()
    time.sleep(2)
    driver.save_screenshot('gg1.png')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.save_screenshot('gg2.png')
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.save_screenshot('gg3.png')
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.save_screenshot('gg4.png')
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.save_screenshot('gg5.png')
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.save_screenshot('gg6.png')
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.save_screenshot('gg7.png')
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.save_screenshot('gg8.png')
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.save_screenshot('gg9.png')
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
    # авторизация
    # десткое
    # 6 стр
    # 3 аниме во второй строке
    # зайти
    # комент



