from locators import *
from urls import *

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_click_on_sauce_section(driver):
    driver.get(main_page)

    # Ожидаем пока главная страница не прогрузится
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be((main_page)))

    #Кликаем на кнопку "Соусы"
    driver.find_element(By.XPATH, sauce).click()


    # Проверяем, что раздел "соусы" после клика по кнопке получили Класс "tab_tab_type_current__2BEPc"
    assert driver.find_element(By.XPATH, sauce_result).text == "Соусы"


def test_click_on_fillings_section(driver):
    driver.get(main_page)

    # Ожидаем пока главная страница не прогрузится
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be((main_page)))

    #Кликаем на кнопку "Начинки"
    driver.find_element(By.XPATH, fillings).click()



    # Проверяем, что раздел "Начинки" после клика по кнопке получили Класс "tab_tab_type_current__2BEPc"
    assert driver.find_element(By.XPATH, fillings_result).text == "Начинки"


def test_click_on_bun_section(driver):
    driver.get(main_page)

    # Ожидаем пока главная страница не прогрузится
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be((main_page)))

    #Кликаем на кнопку "Начинки", так как раздел "Булки" выбран по дефолту
    driver.find_element(By.XPATH, fillings).click()

    # Кликаем на кнопку "Булки"
    driver.find_element(By.XPATH, bun).click()

    # Проверяем, что раздел "Булки" после клика по кнопке получили Класс "tab_tab_type_current__2BEPc"
    assert driver.find_element(By.XPATH, bun_result).text == "Булки"
