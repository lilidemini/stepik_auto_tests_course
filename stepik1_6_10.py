from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#pytest stepik1_6_10.py
link = " http://suninjuly.github.io/registration1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    elements = browser.find_elements(By.CSS_SELECTOR, 'div.first_block>div[class*="form-group"]>input[class*="form-control"]')
    for element in elements:
        element.send_keys("Мой ответ")


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
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


