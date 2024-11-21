from locators import *
from urls import *

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_click_on_logo_from_personal_account(driver):
    driver.get(main_page)

    # Ожидаем пока главная страница не прогрузится
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be((main_page)))

    # Нажатие по кнопке "Личный кабинет"
    driver.find_element(By.XPATH, personal_account).click()

    # Ожидаем пока  страница авторизации не прогрузится
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be((login_page)))

    # Заполнение поля Email на странице входа
    driver.find_element(By.CSS_SELECTOR, email).send_keys("Denis_kvartych_15_333@yandex.ru")

    # Заполнение поля Пароль на странице входа
    driver.find_element(By.CSS_SELECTOR, password).send_keys("555999")

    # Нажатие на кнопку Войти на странице входа
    driver.find_element(By.CLASS_NAME, login_button).click()

    # Ожидаем пока  главная страница не откроется
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be((main_page)))

    # После авторизации нажимаем на кнопку "Личный кабинет"
    driver.find_element(By.XPATH, personal_account).click()

    # Ожидаем пока  страница профиля не откроется
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be((profile_page)))

    #Нажимаем на логотип со страницы Личного кабинета
    driver.find_element(By.CLASS_NAME, logo).click()

    # Проверяем, что при клике на лого произошел переход на главную страницу
    assert driver.current_url == main_page



def test_click_on_costructor_from_personal_account(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Ожидаем пока главная страница не прогрузится
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be((main_page)))

    # Нажатие по кнопке "Личный кабинет"
    driver.find_element(By.XPATH, personal_account).click()

    # Ожидаем пока  страница авторизации не прогрузится
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be((login_page)))

    # Заполнение поля Email на странице входа
    driver.find_element(By.CSS_SELECTOR, email).send_keys("Denis_kvartych_15_333@yandex.ru")

    # Заполнение поля Пароль на странице входа
    driver.find_element(By.CSS_SELECTOR, password).send_keys("555999")

    # Нажатие на кнопку Войти на странице входа
    driver.find_element(By.CLASS_NAME, login_button).click()

    # Ожидаем пока  главная страница не откроется
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be((main_page)))

    # После авторизации нажимаем на кнопку "Личный кабинет"
    driver.find_element(By.XPATH, personal_account).click()

    # Ожидаем пока  страница профиля не откроется
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be((profile_page)))

    # Нажимаем на конструктор со страницы Личного кабинета
    driver.find_element(By.XPATH, costructor).click()

    # Проверяем, что при клике на раздел "Конструктор" произошел переход на главную страницу
    assert driver.current_url == main_page
