import pytest
from selenium import webdriver

@pytest.fixture # фикстура, которая создает экземпляр webdriver
def driver():
    driver = webdriver.Chrome()

    return driver