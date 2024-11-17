from locators import *
from urls import *

from login_generator import generate_login

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_registration_input_correct_data(driver):
    driver.get(registration_page)

    # Ввод имени в поле Имя
    driver.find_element(By.XPATH, name_registration).send_keys("Denis")

    # Ввод почты в поле Email
    driver.find_element(By.XPATH, email_registation).send_keys(generate_login())

    # Ввод пароля в поле Пароль
    driver.find_element(By.CSS_SELECTOR, password_registration).send_keys("555999")

    # Нажатие на кнопку Регистрация
    driver.find_element(By.XPATH, registration_button).click()

    # Ожидаем что урл сменился
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be((login_page)))

    # Проверяем, что после нажатия на кнопку "регистрация" мы переходим на страницу входа
    assert driver.current_url == login_page

    # Закрываем браузер
    driver.quit()

def test_registration_input_password_with_lenght_less_then_six(driver):
    driver.get(registration_page)

    # Ввод имени в поле Имя
    driver.find_element(By.XPATH, name_registration).send_keys("Denis")

    # Ввод почты в поле Email
    driver.find_element(By.XPATH, email_registation).send_keys(generate_login())

    # Ввод пароля с 3 символами в поле Пароль
    driver.find_element(By.CSS_SELECTOR, password_registration).send_keys("555")

    # Нажатие на кнопку Регистрация
    driver.find_element(By.XPATH, registration_button).click()

    # Ожидаем появления ошибки
    WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, password_error)))

    # Проверяем, что  текст ошибки  "Некорректный пароль"
    assert driver.find_element(By.CLASS_NAME, password_error).text == "Некорректный пароль"

    # Закрываем браузер
    driver.quit()