from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.all_locators import *
from helpers.data_helpers import DataHelper
from test_data.test_data import UserData
from urls import Urls


class TestLoginRegistration:
    def test_register_new_user(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        driver.get(Urls.MAIN_PAGE)
        wait.until(EC.element_to_be_clickable(HomePageLocators.login_account_button)).click()
        wait.until(EC.element_to_be_clickable(LoginPageLocators.registration_link)).click()

        user_data = {
            "name": DataHelper.generate_name(),
            "email": DataHelper.generate_login(),
            "password": DataHelper.generate_password()
        }

        wait.until(EC.visibility_of_element_located(RegistrationPageLocators.name_input)).send_keys(user_data["name"])
        wait.until(EC.visibility_of_element_located(RegistrationPageLocators.email_input)).send_keys(user_data["email"])
        wait.until(EC.visibility_of_element_located(RegistrationPageLocators.password_input)).send_keys(
            user_data["password"])
        wait.until(EC.element_to_be_clickable(RegistrationPageLocators.register_button)).click()


    def test_short_password_error(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        driver.get(Urls.MAIN_PAGE)
        wait.until(EC.element_to_be_clickable(HomePageLocators.login_account_button)).click()
        wait.until(EC.element_to_be_clickable(LoginPageLocators.registration_link)).click()

        wait.until(EC.visibility_of_element_located(RegistrationPageLocators.name_input)).send_keys(
            DataHelper.generate_name())
        wait.until(EC.visibility_of_element_located(RegistrationPageLocators.email_input)).send_keys(
            DataHelper.generate_login())
        wait.until(EC.visibility_of_element_located(RegistrationPageLocators.password_input)).send_keys("12345")
        wait.until(EC.element_to_be_clickable(RegistrationPageLocators.register_button)).click()

    def test_login_via_main_page_button(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        driver.get(Urls.MAIN_PAGE)

        login_button = wait.until(
            EC.element_to_be_clickable(HomePageLocators.login_account_button),
            "Кнопка 'Войти в аккаунт' не найдена или не кликабельна"
        )
        login_button.click()

        wait.until(
            EC.url_contains(Urls.LOGIN_PAGE),
            "Не произошел переход на страницу входа"
        )

        user = UserData()
        wait.until(
            EC.visibility_of_element_located(LoginPageLocators.login_input),
            "Поле ввода email не найдено"
        ).send_keys(user.email)

        wait.until(
            EC.visibility_of_element_located(LoginPageLocators.password_input),
            "Поле ввода пароля не найдено"
        ).send_keys(user.password)

        wait.until(
            EC.element_to_be_clickable(LoginPageLocators.login_button),
            "Кнопка 'Войти' не найдена или не кликабельна"
        ).click()

        wait.until(
            EC.url_contains(Urls.MAIN_PAGE),
            "Не произошел переход на главную страницу после входа"
        )

        assert wait.until(
            EC.visibility_of_element_located(HomePageLocators.account_link),
            "Кнопка перехода в ЛК не отображается после входа"
        ), "Авторизация не выполнена"
    def test_login_via_personal_account(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        driver.get(Urls.MAIN_PAGE)

        account_link = wait.until(
            EC.element_to_be_clickable(HomePageLocators.account_link),
            "Кнопка 'Войти в аккаунт' не найдена или не кликабельна"
        )
        account_link.click()

        wait.until(
            EC.url_contains(Urls.LOGIN_PAGE),
            "Не произошел переход на страницу входа"
        )

        user = UserData()
        wait.until(
            EC.visibility_of_element_located(LoginPageLocators.login_input),
            "Поле ввода email не найдено"
        ).send_keys(user.email)

        wait.until(
            EC.visibility_of_element_located(LoginPageLocators.password_input),
            "Поле ввода пароля не найдено"
        ).send_keys(user.password)

        wait.until(
            EC.element_to_be_clickable(LoginPageLocators.login_button),
            "Кнопка 'Войти' не найдена или не кликабельна"
        ).click()

        wait.until(
            EC.url_contains(Urls.MAIN_PAGE),
            "Не произошел переход на главную страницу после входа"
        )

        assert wait.until(
            EC.visibility_of_element_located(HomePageLocators.account_link),
            "Кнопка перехода в ЛК не отображается после входа"
        ), "Авторизация не выполнена"

    def test_logout_from_account(self, create_driver):
        """
        Тест выхода из аккаунта через кнопку 'Выход' в личном кабинете
        """
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        driver.get(Urls.LOGIN_PAGE)
        user = UserData()
        wait.until(EC.visibility_of_element_located(LoginPageLocators.login_input)).send_keys(user.email)
        wait.until(EC.visibility_of_element_located(LoginPageLocators.password_input)).send_keys(user.password)
        wait.until(EC.element_to_be_clickable(LoginPageLocators.login_button)).click()
        wait.until(EC.url_contains(Urls.MAIN_PAGE))


        wait.until(EC.element_to_be_clickable(HomePageLocators.account_link)).click()
        wait.until(EC.url_contains(Urls.ACCOUNT_PAGE))

        logout_button = wait.until(
            EC.element_to_be_clickable(AccountPageLocators.logout_button),
            "Кнопка 'Выход' не найдена или не кликабельна"
        )
        logout_button.click()

        wait.until(
            EC.url_contains(Urls.LOGIN_PAGE),
            "Не произошел переход на страницу входа после выхода"
        )


        assert wait.until(
            EC.visibility_of_element_located(LoginPageLocators.login_label),
            "Форма входа не отображается после выхода"
        )

        driver.get(Urls.MAIN_PAGE)
        assert wait.until(
            EC.visibility_of_element_located(HomePageLocators.login_account_button),
            "Кнопка 'Войти в аккаунт' не отображается после выхода"
        )

    def test_login_via_registration_page_from_main(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)

        driver.get(Urls.MAIN_PAGE)

        account_link = wait.until(
            EC.element_to_be_clickable(HomePageLocators.account_link),
            "Кнопка 'Личный кабинет' не найдена на главной странице"
        )
        account_link.click()

        wait.until(
            EC.url_contains(Urls.LOGIN_PAGE),
            "Не произошел переход на страницу входа после клика по ЛК"
        )

        register_link = wait.until(
            EC.element_to_be_clickable(LoginPageLocators.registration_link),
            "Ссылка 'Зарегистрироваться' не найдена на странице входа"
        )
        register_link.click()

        wait.until(
            EC.url_contains(Urls.REGISTER_PAGE),
            "Не произошел переход на страницу регистрации"
        )

        login_link = wait.until(
            EC.element_to_be_clickable(RegistrationPageLocators.login_link),
            "Ссылка 'Войти' не найдена на странице регистрации"
        )
        login_link.click()

        wait.until(
            EC.url_contains(Urls.LOGIN_PAGE),
            "Не произошел возврат на страницу входа"
        )

        user = UserData()
        wait.until(
            EC.visibility_of_element_located(LoginPageLocators.login_input),
            "Поле ввода email не найдено"
        ).send_keys(user.email)

        wait.until(
            EC.visibility_of_element_located(LoginPageLocators.password_input),
            "Поле ввода пароля не найдено"
        ).send_keys(user.password)

        wait.until(
            EC.element_to_be_clickable(LoginPageLocators.login_button),
            "Кнопка 'Войти' не найдена или не кликабельна"
        ).click()

        wait.until(
            EC.url_contains(Urls.MAIN_PAGE),
            "Не произошел переход на главную страницу после входа"
        )

        wait.until(EC.element_to_be_clickable(HomePageLocators.account_link)).click()
        wait.until(EC.url_contains(Urls.ACCOUNT_PAGE))

        account_name = wait.until(
            EC.visibility_of_element_located(AccountPageLocators.name_input),
            "Поле имени пользователя не найдено в ЛК"
        ).get_attribute("value")

        assert account_name == user.name, f"Ожидалось имя {user.name}, получено {account_name}"

    def test_login_via_password_recovery_flow(self, create_driver):

        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)
        user = UserData()

        driver.get(Urls.MAIN_PAGE)

        account_link = wait.until(
            EC.element_to_be_clickable(HomePageLocators.account_link),
            "Кнопка 'Личный кабинет' не найдена на главной странице"
        )
        account_link.click()

        wait.until(
            EC.url_contains(Urls.LOGIN_PAGE),
            "Не произошел переход на страницу входа после клика по ЛК"
        )

        recovery_link = wait.until(
            EC.element_to_be_clickable(LoginPageLocators.restore_password_link),
            "Ссылка 'Восстановить пароль' не найдена на странице входа"
        )
        recovery_link.click()

        wait.until(
            EC.url_contains(Urls.FORGOT_PASSWORD_PAGE),
            "Не произошел переход на страницу восстановления пароля"
        )

        login_link = wait.until(
            EC.element_to_be_clickable(PasswordRecoveryPageLocators.login_link),
            "Кнопка 'Войти' не найдена на странице восстановления пароля"
        )
        login_link.click()

        wait.until(
            EC.url_contains(Urls.LOGIN_PAGE),
            "Не произошел возврат на страницу входа"
        )

        email_field = wait.until(
            EC.visibility_of_element_located(LoginPageLocators.login_input),
            "Поле ввода email не найдено"
        )
        email_field.send_keys(user.email)

        password_field = wait.until(
            EC.visibility_of_element_located(LoginPageLocators.password_input),
            "Поле ввода пароля не найдено"
        )
        password_field.send_keys(user.password)

        login_button = wait.until(
            EC.element_to_be_clickable(LoginPageLocators.login_button),
            "Кнопка 'Войти' не найдена или не кликабельна"
        )
        login_button.click()

        wait.until(
            EC.url_contains(Urls.MAIN_PAGE),
            "Не произошел переход на главную страницу после входа"
        )

        wait.until(EC.element_to_be_clickable(HomePageLocators.account_link)).click()
        wait.until(EC.url_contains(Urls.ACCOUNT_PAGE))

        account_name = wait.until(
            EC.visibility_of_element_located(AccountPageLocators.name_input),
            "Поле имени пользователя не найдено в ЛК"
        ).get_attribute("value")

        assert account_name == user.name, f"Ожидалось имя {user.name}, получено {account_name}"







