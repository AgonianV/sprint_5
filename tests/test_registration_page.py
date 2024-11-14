import time
from login_generator import generate_login
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_registration_input_correct_data():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Ввод имени в поле Имя
    driver.find_element(By.XPATH, "//fieldset[1]/div/div/input").send_keys("Denis")

    # Ввод почты в поле Email
    driver.find_element(By.XPATH, "//fieldset[2]/div/div/input").send_keys(generate_login())

    # Ввод пароля в поле Пароль
    driver.find_element(By.CSS_SELECTOR, "[name = 'Пароль']").send_keys("555999")

    # Нажатие на кнопку Регистрация
    driver.find_element(By.XPATH, "//button").click()

    time.sleep(3)
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    driver.quit()

def test_registration_input_password_with_lenght_less_then_six():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Ввод имени в поле Имя
    driver.find_element(By.XPATH, "//fieldset[1]/div/div/input").send_keys("Denis")

    # Ввод почты в поле Email
    driver.find_element(By.XPATH, "//fieldset[2]/div/div/input").send_keys(generate_login())

    # Ввод пароля с 3 символами в поле Пароль
    driver.find_element(By.CSS_SELECTOR, "[name = 'Пароль']").send_keys("555")

    # Нажатие на кнопку Регистрация
    driver.find_element(By.XPATH, "//button").click()
    time.sleep(1)

    assert driver.find_element(By.CLASS_NAME, "input__error").text == "Некорректный пароль"

    driver.quit()