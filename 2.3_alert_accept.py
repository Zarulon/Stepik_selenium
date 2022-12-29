import time
import os
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
url = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(url)
button = browser.find_element(By.TAG_NAME, 'button')
button.click()
alert = browser.switch_to.alert
alert.accept()
x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
y = calc(x)
input1 = browser.find_element(By.ID, 'answer')
input1.send_keys(y)
button = browser.find_element(By.TAG_NAME, 'button')
button.click()

  #button = browser.find_element(By.CSS_SELECTOR, "button.btn")
  #button.click()

#finally:
time.sleep(100)
browser.quit()