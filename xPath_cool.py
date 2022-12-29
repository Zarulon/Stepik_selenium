
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    url = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(url)

    # Ваш код, который заполняет обязательные поля

    link = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'first')]")
    link.click()
    input1 = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'first')]")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'last')]")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'email')]")
    input3.send_keys("test@test.ru")
    input3 = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'phone')]")
    input3.send_keys("9998885522")
    input4 = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'address')]")
    input4.send_keys("Russia")
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()