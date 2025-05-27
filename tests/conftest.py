import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def create_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()