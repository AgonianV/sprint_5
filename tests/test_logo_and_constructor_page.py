import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_click_on_logo_from_personal_account():
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
    #Нажимаем на логотип со страницы Личного кабинета
    driver.find_element(By.CLASS_NAME, "AppHeader_header__logo__2D0X2").click()

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    driver.quit()

def test_click_on_costructor_from_personal_account():
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
    # Нажимаем на конструктор со страницы Личного кабинета
    driver.find_element(By.XPATH, "//ul/li[1]/a").click()

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    driver.quit()