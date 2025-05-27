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
    AccountPageLocators,
    PasswordRecoveryPageLocators
)

home_locators = HomePageLocators()
login_locators = LoginPageLocators()
registration_locators = RegistrationPageLocators()
account_locators = AccountPageLocators()
recovery_locators = PasswordRecoveryPageLocators()

class TestLoginRegistration:
    def test_register_new_user(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)
        driver.get("https://stellarburgers.nomoreparties.site/")
        sleep(3)

        login_account_button = wait.until(EC.element_to_be_clickable(home_locators.login_account_button))
        login_account_button.click()
        sleep(3)

        registration_link = wait.until(EC.element_to_be_clickable(login_locators.registration_link))
        registration_link.click()
        sleep(3)

        name_data = DataHelper.generate_name()
        email_data = DataHelper.generate_login()
        password_data = DataHelper.generate_password()

        register_name_input = wait.until(EC.visibility_of_element_located(registration_locators.name_input))
        register_email_input = wait.until(EC.visibility_of_element_located(registration_locators.email_input))
        register_password_input = wait.until(EC.visibility_of_element_located(registration_locators.password_input))
        register_name_input.send_keys(name_data)
        register_email_input.send_keys(email_data)
        register_password_input.send_keys(password_data)

        register_button = wait.until(EC.element_to_be_clickable(registration_locators.register_button))
        register_button.click()
        sleep(3)

        login_input = wait.until(EC.visibility_of_element_located(login_locators.login_input))
        password_input = wait.until(EC.visibility_of_element_located(login_locators.password_input))
        login_input.send_keys(email_data)
        password_input.send_keys(password_data)
        login_button = wait.until(EC.element_to_be_clickable(login_locators.login_button))
        login_button.click()
        sleep(3)

        account_link = wait.until(EC.element_to_be_clickable(home_locators.account_link))
        account_link.click()
        sleep(3)

        account_name_input = wait.until(EC.visibility_of_element_located(account_locators.name_input))
        account_login_input = wait.until(EC.visibility_of_element_located(account_locators.login_input))
        assert account_name_input.get_attribute("value") == name_data
        assert account_login_input.get_attribute("value") == email_data

        logout_button = wait.until(EC.element_to_be_clickable(account_locators.logout_button))
        logout_button.click()
        sleep(3)

    def test_login_main_page(self, create_driver):
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

        account_link = wait.until(EC.element_to_be_clickable(home_locators.account_link))
        account_link.click()
        sleep(3)

        account_name_input = wait.until(EC.visibility_of_element_located(account_locators.name_input))
        account_login_input = wait.until(EC.visibility_of_element_located(account_locators.login_input))
        assert account_name_input.get_attribute("value") == user_data.name
        assert account_login_input.get_attribute("value") == user_data.email
        sleep(3)

    def test_login_personal_account(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)
        driver.get("https://stellarburgers.nomoreparties.site/")
        sleep(3)

        account_link = wait.until(EC.element_to_be_clickable(home_locators.account_link))
        account_link.click()
        sleep(3)

        login_input = wait.until(EC.visibility_of_element_located(login_locators.login_input))
        password_input = wait.until(EC.visibility_of_element_located(login_locators.password_input))
        user_data = UserData()
        login_input.send_keys(user_data.email)
        password_input.send_keys(user_data.password)

        login_button = wait.until(EC.element_to_be_clickable(login_locators.login_button))
        login_button.click()
        sleep(3)

    def test_logout_from_account(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=15)
        driver.get("https://stellarburgers.nomoreparties.site/login")
        user_data = UserData()

        email_field = wait.until(EC.visibility_of_element_located(login_locators.login_input))
        email_field.send_keys(user_data.email)
        password_field = wait.until(EC.visibility_of_element_located(login_locators.password_input))
        password_field.send_keys(user_data.password)

        login_button = wait.until(EC.element_to_be_clickable(login_locators.login_button))
        login_button.click()
        sleep(3)

        account_button = wait.until(EC.element_to_be_clickable(home_locators.account_link))
        account_button.click()
        sleep(3)

        logout_button = wait.until(EC.element_to_be_clickable(account_locators.logout_button))
        logout_button.click()
        sleep(3)

        assert "login" in driver.current_url.lower(), "Не произошел переход на страницу входа"
        assert wait.until(EC.visibility_of_element_located(login_locators.login_label)), "Не отображается форма входа"

        driver.get("https://stellarburgers.nomoreparties.site/")
        assert wait.until(EC.visibility_of_element_located(home_locators.login_account_button)), "Кнопка входа не отображается"

    def test_login_from_registration_page(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)
        driver.get("https://stellarburgers.nomoreparties.site/")
        sleep(3)

        account_link = wait.until(EC.element_to_be_clickable(home_locators.account_link))
        account_link.click()
        sleep(3)

        registration_link = wait.until(EC.element_to_be_clickable(login_locators.registration_link))
        registration_link.click()
        sleep(3)

        login_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/login')]")))
        login_link.click()
        sleep(3)

        assert "login" in driver.current_url, "Не произошел переход на страницу входа"
        login_input = wait.until(EC.visibility_of_element_located(login_locators.login_input))
        password_input = wait.until(EC.visibility_of_element_located(login_locators.password_input))
        user_data = UserData()
        login_input.send_keys(user_data.email)
        password_input.send_keys(user_data.password)

        login_button = wait.until(EC.element_to_be_clickable(login_locators.login_button))
        login_button.click()
        sleep(3)

        assert "stellarburgers" in driver.current_url, "Не произошла авторизация"
        assert "login" not in driver.current_url, "Остались на странице входа"

    def test_login_from_password_recovery_page(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=15)
        driver.get("https://stellarburgers.nomoreparties.site/")
        assert "stellarburgers" in driver.current_url, "Главная страница не открылась"
        sleep(2)

        account_link = wait.until(EC.element_to_be_clickable(home_locators.account_link))
        account_link.click()
        sleep(2)
        assert "login" in driver.current_url, "Не перешли на страницу входа"

        recovery_link = wait.until(EC.element_to_be_clickable(login_locators.restore_password_link))
        recovery_link.click()
        sleep(3)
        assert "forgot-password" in driver.current_url, "Не перешли на страницу восстановления пароля"

        login_link = wait.until(EC.element_to_be_clickable(recovery_locators.login_link))
        assert login_link.is_displayed(), "Кнопка 'Войти' не отображается"
        login_link.click()
        sleep(3)
        assert "login" in driver.current_url, "Не вернулись на страницу входа"

        user_data = UserData()
        assert wait.until(EC.visibility_of_element_located(login_locators.login_label)), "Форма входа не отображается"

        email_field = wait.until(EC.visibility_of_element_located(login_locators.login_input))
        email_field.send_keys(user_data.email)
        password_field = wait.until(EC.visibility_of_element_located(login_locators.password_input))
        password_field.send_keys(user_data.password)

        login_button = wait.until(EC.element_to_be_clickable(login_locators.login_button))
        login_button.click()
        sleep(3)

        assert "stellarburgers" in driver.current_url, "Не произошла авторизация"
        assert "login" not in driver.current_url, "Остались на странице входа"

    def test_short_password_error(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        try:
            driver.get("https://stellarburgers.nomoreparties.site/")
            sleep(2)

            login_account_button = wait.until(EC.element_to_be_clickable(home_locators.login_account_button))
            login_account_button.click()
            sleep(3)

            registration_link = wait.until(EC.element_to_be_clickable(login_locators.registration_link))
            registration_link.click()
            sleep(3)

            test_name = "TestUser"
            test_email = DataHelper.generate_login()
            short_password = "12345"

            wait.until(EC.visibility_of_element_located(RegistrationPageLocators.name_input)).send_keys(test_name)
            wait.until(EC.visibility_of_element_located(RegistrationPageLocators.email_input)).send_keys(test_email)
            password_field = wait.until(EC.visibility_of_element_located(RegistrationPageLocators.password_input))
            password_field.send_keys(short_password)

            register_button = wait.until(EC.element_to_be_clickable(RegistrationPageLocators.register_button))
            register_button.click()
            sleep(2)

            error_message = wait.until(EC.visibility_of_element_located(
                (By.XPATH,
                 "//p[contains(text(), 'Некорректный пароль') or contains(text(), 'Минимальная длина пароля 6 символов')]")
            ))
            assert error_message.is_displayed(), "Сообщение об ошибке не отобразилось"
            assert "register" in driver.current_url, "Произошел неожиданный редирект"

        finally:
            driver.quit()

