from locators import *
from urls import *

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_click_on_logo_from_personal_account(driver):
    driver.get(main_page)

    # Нажатие по кнопке "Личный кабинет"
    driver.find_element(By.XPATH, personal_account).click()

    # Ожидаем пока страница Личного кабинета не прогрузится
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be((login_page)))

    # Заполнение поля Email на странице входа
    driver.find_element(By.CSS_SELECTOR, email).send_keys("Denis_kvartych_15_333@yandex.ru")

    # Заполнение поля Пароль на странице входа
    driver.find_element(By.CSS_SELECTOR, password).send_keys("555999")

    # Нажатие на кнопку Войти на странице входа
    driver.find_element(By.CLASS_NAME, login_button).click()

    # Ожидаем пока главная страница не прогрузится
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be((main_page)))

    # После авторизации нажимаем на кнопку "Личный кабинет"
    driver.find_element(By.XPATH, personal_account).click()

    # Ожидаем пока страница Личного кабинета не прогрузится
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be((profile_page)))

    #Нажимаем на кнопку Выйти
    driver.find_element(By.CLASS_NAME, logout_button).click()

    WebDriverWait(driver, 5).until(expected_conditions.url_to_be((login_page)))
    #Переходим на главную страницу
    driver.get(main_page)

    #Переходим в личный кабинет
    driver.find_element(By.XPATH, personal_account).click()

    #Проверяем, что после разлогина, при переходе в личный кабинет, открывается страница авторизации
    assert driver.current_url == login_page
