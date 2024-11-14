import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_click_on_sauce_section():
    driver = webdriver.Chrome()

    driver.get("https://stellarburgers.nomoreparties.site/")

    #Кликаем на кнопку "Соусы"
    driver.find_element(By.XPATH, "//section[1]/div[1]/div[2]").click()

    # Находим раздел "соусы"
    element = driver.find_element(By.XPATH, "//main/section[1]/div[2]/h2[2]")
    time.sleep(2)
    #Узнаем нынешние координаты раздела
    section_location = element.location

    # Проверяем, что раздел "соусы" после клика по кнопке переместились наверх
    assert section_location == {'x': 0, 'y': 244}

    driver.quit()

def test_click_on_fillings_section():
    driver = webdriver.Chrome()

    driver.get("https://stellarburgers.nomoreparties.site/")

    #Кликаем на кнопку "Начинки"
    driver.find_element(By.XPATH, "//section[1]/div[1]/div[3]").click()

    # Находим раздел "начинки"
    element = driver.find_element(By.XPATH, "//main/section[1]/div[2]/h2[3]")
    time.sleep(2)
    #Узнаем нынешние координаты раздела
    section_location = element.location

    # Проверяем, что раздел "начинки" после клика по кнопке переместились наверх
    assert section_location == {'x': 0, 'y': 244}

    driver.quit()


def test_click_on_bun_section():
    driver = webdriver.Chrome()

    driver.get("https://stellarburgers.nomoreparties.site/")

    #Кликаем на кнопку "Начинки", чтобы сместить раздел с булками на странице
    driver.find_element(By.XPATH, "//section[1]/div[1]/div[3]").click()

    time.sleep(2)

    # Кликаем на кнопку "Булки"
    driver.find_element(By.XPATH, "//section[1]/div[1]/div[1]").click()

    # Находим раздел "булки"
    element = driver.find_element(By.XPATH, "//main/section[1]/div[2]/h2[1]")
    time.sleep(2)
    #Узнаем нынешние координаты раздела
    section_location = element.location

    # Проверяем, что раздел "булки" после клика по кнопке переместились наверх
    assert section_location == {'x': 0, 'y': 244}

    driver.quit()