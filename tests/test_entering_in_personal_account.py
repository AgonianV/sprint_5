import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_from_button_personal_account():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    time.sleep(1)
    # Нажатие по кнопке "Личный кабинет"
    driver.find_element(By.XPATH, "//*[text() = 'Личный Кабинет']").click()
    time.sleep(1)
    # Заполнение поля Email на странице входа
    driver.find_element(By.CSS_SELECTOR, "[name = 'name']").send_keys("Denis_kvartych_15_333@yandex.ru")

    # Заполнение поля Пароль на странице входа
    driver.find_element(By.CSS_SELECTOR, "[name = 'Пароль']").send_keys("555999")

    # Нажатие на кнопку Войти на странице входа
    driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()
    time.sleep(1)

    # После авторизации нажимаем на кнопку "Личный кабинет"
    driver.find_element(By.XPATH, "//*[text() = 'Личный Кабинет']").click()

    time.sleep(1)
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"

    driver.quit()