from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


url = "https://yummyanime.org/"
driver = webdriver.Chrome(executable_path="/Users/sasha/Desktop/sosiska/chromedriver")

try:
    driver.get(url=url)
    time.sleep(5)
    log = driver.find_element_by_xpath('/html/body/div[1]/div/header/div[2]').click()
    time.sleep(2)
    login = driver.find_element_by_xpath('//*[@id="login_name"]')
    login.send_keys("SaveOk")
    pwd = driver.find_element_by_xpath('//*[@id="login_password"]')
    pwd.send_keys("bushuev2003")
    pwd.send_keys(Keys.ENTER)
    time.sleep(7)
    janr = driver.find_element_by_xpath('/html/body/div[1]/div/div/aside/div[1]/ul/li[1]/a').click()
    det = driver.find_element_by_xpath('/html/body/div[1]/div/div/aside/div[1]/ul/li[1]/ul/li[18]/a').click()
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    page = driver.find_element_by_xpath('//*[@id="pagination"]/div/a[5]').click()
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    anime = driver.find_element_by_xpath('//*[@id="dle-content"]/a[8]/div[2]/h3').click()
    time.sleep(3)
    driver.switch_to.default_content()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    com = driver.find_element_by_xpath('//*[@id="comments_ifr"]')
    com.click()
    a = "J"
    com.send_keys(a)
    time.sleep(3)
    button = driver.find_element_by_xpath('//*[@id="add-comments-form"]/div[2]/div/button').click()
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
