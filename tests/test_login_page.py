from locators import *
from urls import *

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_login_from_button_login_to_account(driver):
    driver.get(main_page)

    # Ожидаем пока главная страница не прогрузится
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be((main_page)))

    # Нажатие по кнопке "Войти в аккаунт"
    driver.find_element(By.CLASS_NAME, login_button).click()

    # Ожидаем пока  страница авторизации не прогрузится
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be((login_page)))

    # Заполнение поля Email на странице входа
    driver.find_element(By.CSS_SELECTOR, email).send_keys("Denis_kvartych_15_333@yandex.ru")

    # Заполнение поля Пароль на странице входа
    driver.find_element(By.CSS_SELECTOR, password).send_keys("555999")

    # Нажатие на кнопку Войти на странице входа
    driver.find_element(By.CLASS_NAME, login_button).click()

    # Ожидаем пока главная страница не прогрузится
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be((main_page)))

    # Проверяем, что после авторизации произошел перевод на главную страницу и отображается кнопка "Оформить заказ"
    assert driver.current_url == main_page and driver.find_element(By.CLASS_NAME, order_button).text == "Оформить заказ"

    driver.quit()

def test_login_from_button_personal_account(driver):
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

    # Ожидаем пока главная страница не прогрузится
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be((main_page)))

    # Проверяем, что после авторизации произошел перевод на главную страницу и отображается кнопка "Оформить заказ"
    assert driver.current_url == main_page and driver.find_element(By.CLASS_NAME, order_button).text == "Оформить заказ"

    driver.quit()


def test_login_from_registration_page(driver):
    driver.get(registration_page)

    # Ожидаем пока страница регистрации не прогрузится
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be((registration_page)))

    # Нажатие по кнопке "Войти" на странице регистрации
    driver.find_element(By.XPATH, login_button_registration_page).click()

    # Ожидаем пока  страница авторизации не прогрузится
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be((login_page)))

    # Заполнение поля Email на странице входа
    driver.find_element(By.CSS_SELECTOR, email).send_keys("Denis_kvartych_15_333@yandex.ru")

    # Заполнение поля Пароль на странице входа
    driver.find_element(By.CSS_SELECTOR, password).send_keys("555999")

    # Нажатие на кнопку Войти на странице входа
    driver.find_element(By.CLASS_NAME, login_button).click()

    # Ожидаем пока главная страница не прогрузится
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be((main_page)))

    # Проверяем, что после авторизации произошел перевод на главную страницу и отображается кнопка "Оформить заказ"
    assert driver.current_url == main_page and driver.find_element(By.CLASS_NAME, order_button).text == "Оформить заказ"

    driver.quit()


def test_login_from_password_recovery_page(driver):
    driver.get(forgot_password_page)

    # Ожидаем пока  страница воссатановления пароля не прогрузится
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be((forgot_password_page)))

    # Нажатие по кнопке "Войти" на странице восстановления пароля
    driver.find_element(By.XPATH, login_button_registration_page).click()

    # Ожидаем пока  страница авторизации не прогрузится
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be((login_page)))

    # Заполнение поля Email на странице входа
    driver.find_element(By.CSS_SELECTOR, email).send_keys("Denis_kvartych_15_333@yandex.ru")

    # Заполнение поля Пароль на странице входа
    driver.find_element(By.CSS_SELECTOR, password).send_keys("555999")

    # Нажатие на кнопку Войти на странице входа
    driver.find_element(By.CLASS_NAME, login_button).click()

    # Ожидаем пока главная страница не прогрузится
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be((main_page)))

    # Проверяем, что после авторизации произошел перевод на главную страницу и отображается кнопка "Оформить заказ"
    assert driver.current_url == main_page and driver.find_element(By.CLASS_NAME, order_button).text == "Оформить заказ"

    driver.quit()