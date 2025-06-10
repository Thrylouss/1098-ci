from selenium import webdriver
import pytest

@pytest.fixture
def driver_chrome():
    driver = webdriver.Chrome()
    driver.get("https://my.proweb.uz/log-in")
    yield driver
