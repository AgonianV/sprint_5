import pytest
import  random
from selenium import webdriver

@pytest.fixture # фикстура, которая создает экземпляр webdriver
def driver():
    driver = webdriver.Chrome()

    return driver

@pytest.fixture # фикстура, которая создает рандомную почту для регистрации
def generate_login():
    generate_login = f"Denis_kvartych_15_{random.randint(100,999)}@yandex.ru"

    return generate_login