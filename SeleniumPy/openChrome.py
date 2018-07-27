import os
import time
from selenium import webdriver

chrome_path = "/Users/sthiyag/IdeaProjects/SeleniumPy/chromedriver"

driver = webdriver.Chrome(chrome_path)

driver.maximize_window()

driver.implicitly_wait(30)
driver.get('http://www.sunnxt.com/live/')

play_button = driver.find_elements_by_xpath('//*[@class="movie_details-btn-div user_chk"]//*[contains(text(),"Play")]')[0]
play_button.click()

user_name = driver.find_elements_by_xpath('//*[@id="email-up"]')[0]
password = driver.find_elements_by_xpath('//*[@id="password"]')[0]
login_button = driver.find_elements_by_xpath('//*[text()="login"]')[0]

user_name.send_keys(9994237875)
time.sleep(2)
password.send_keys("1234qwer$")
time.sleep(3)
login_button.click()

time.sleep(5)

live_tv = driver.find_element_by_xpath('(//*[@href="/live/"])[1]')
live_tv.click()

time.sleep(5)

maximize = driver.find_element_by_xpath('//*[@class="fp-fullscreen fp-icon"]')
maximize.click()
