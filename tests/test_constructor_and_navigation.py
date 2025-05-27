from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from test_data.test_data import UserData
from helpers.data_helpers import DataHelper
from locators.all_locators import (
    HomePageLocators,
    LoginPageLocators,
    RegistrationPageLocators,
    AccountPageLocators
)

home_locators = HomePageLocators()
login_locators = LoginPageLocators()
registration_locators = RegistrationPageLocators()
account_locators = AccountPageLocators()

class TestNavigationAndConstructor:
    def test_navigate_to_personal_account(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)
        driver.get("https://stellarburgers.nomoreparties.site/login")
        user_data = UserData()

        login_input = wait.until(EC.visibility_of_element_located(login_locators.login_input))
        login_input.send_keys(user_data.email)
        password_input = wait.until(EC.visibility_of_element_located(login_locators.password_input))
        password_input.send_keys(user_data.password)
        login_button = wait.until(EC.element_to_be_clickable(login_locators.login_button))
        login_button.click()
        sleep(3)

        assert "stellarburgers.nomoreparties.site" in driver.current_url, "Авторизация не удалась"
        account_link = wait.until(EC.element_to_be_clickable(home_locators.account_link))
        account_link.click()
        sleep(3)

        assert wait.until(EC.visibility_of_element_located(account_locators.profile_section)), "Не удалось перейти в ЛК"
        assert "account" in driver.current_url, "URL не соответствует личному кабинету"
        account_name_input = wait.until(EC.visibility_of_element_located(account_locators.name_input))
        assert account_name_input.get_attribute("value") == user_data.name, "Имя пользователя не совпадает"

    def test_navigate_from_account_to_constructor_via_constructor_link(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)
        driver.get("https://stellarburgers.nomoreparties.site/")
        sleep(3)

        login_account_button = wait.until(EC.element_to_be_clickable(home_locators.login_account_button))
        login_account_button.click()
        login_input = wait.until(EC.visibility_of_element_located(login_locators.login_input))
        password_input = wait.until(EC.visibility_of_element_located(login_locators.password_input))
        user_data = UserData()
        login_input.send_keys(user_data.email)
        password_input.send_keys(user_data.password)
        login_button = wait.until(EC.element_to_be_clickable(login_locators.login_button))
        login_button.click()
        sleep(3)

        assert "stellarburgers.nomoreparties.site" in driver.current_url, "Авторизация не удалась"
        assert "login" not in driver.current_url, "Не произошел редирект после авторизации"
        account_button = wait.until(EC.element_to_be_clickable(home_locators.account_link))
        account_button.click()
        sleep(3)

        assert "account" in driver.current_url, "Не перешли в личный кабинет"
        constructor_button = wait.until(EC.element_to_be_clickable(home_locators.constructor_link))
        constructor_button.click()
        sleep(3)

        assert "stellarburgers.nomoreparties.site" in driver.current_url, "Неверный URL главной страницы"
        assert "account" not in driver.current_url, "Остались в личном кабинете"

    def test_navigate_from_account_to_constructor_via_logo(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)
        driver.get("https://stellarburgers.nomoreparties.site/login")
        user_data = UserData()

        login_input = wait.until(EC.visibility_of_element_located(login_locators.login_input))
        password_input = wait.until(EC.visibility_of_element_located(login_locators.password_input))
        login_input.send_keys(user_data.email)
        password_input.send_keys(user_data.password)
        login_button = wait.until(EC.element_to_be_clickable(login_locators.login_button))
        login_button.click()
        sleep(3)
        account_link = wait.until(EC.element_to_be_clickable(home_locators.account_link))
        account_link.click()
        sleep(3)
        logo = wait.until(EC.element_to_be_clickable(home_locators.logo))
        logo.click()
        sleep(3)

    def test_sauces_section_navigation(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)
        driver.get("https://stellarburgers.nomoreparties.site/")
        sauces_section = wait.until(EC.element_to_be_clickable(home_locators.sauces_section))
        sauces_section.click()
        active_section = wait.until(EC.visibility_of_element_located(home_locators.active_section))
        assert "Соусы" in active_section.text

    def test_fillings_section_navigation(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)
        driver.get("https://stellarburgers.nomoreparties.site/")
        fillings_section = wait.until(EC.element_to_be_clickable(home_locators.fillings_section))
        fillings_section.click()
        active_section = wait.until(EC.visibility_of_element_located(home_locators.active_section))
        assert "Начинки" in active_section.text

    def test_buns_section_navigation(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)
        driver.get("https://stellarburgers.nomoreparties.site/")
        sleep(3)

        sauces_section = wait.until(EC.element_to_be_clickable(home_locators.sauces_section))
        sauces_section.click()
        sleep(2)
        active_section = wait.until(EC.visibility_of_element_located(home_locators.active_section))
        assert "Соусы" in active_section.text, "Раздел 'Соусы' не активирован"

        buns_section = wait.until(EC.element_to_be_clickable(home_locators.buns_section))
        buns_section.click()
        sleep(2)
        active_section = wait.until(EC.visibility_of_element_located(home_locators.active_section))
        assert "Булки" in active_section.text, "Раздел 'Булки' не активирован"
        assert wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Булки')]")), "Не найдены элементы раздела 'Булки'")

