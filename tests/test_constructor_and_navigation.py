from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.all_locators import HomePageLocators, LoginPageLocators, AccountPageLocators
from test_data.test_data import UserData
from urls import Urls


class TestNavigationAndConstructor:
    def test_navigate_to_personal_account(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)
        driver.get(Urls.LOGIN_PAGE)
        user = UserData()
        email_field = wait.until(EC.visibility_of_element_located(LoginPageLocators.login_input))
        email_field.send_keys(user.email)
        password_field = wait.until(EC.visibility_of_element_located(LoginPageLocators.password_input))
        password_field.send_keys(user.password)
        login_button = wait.until(EC.element_to_be_clickable(LoginPageLocators.login_button))
        login_button.click()
        wait.until(EC.url_contains(Urls.MAIN_PAGE))
        account_button = wait.until(EC.element_to_be_clickable(HomePageLocators.account_link))
        account_button.click()
        wait.until(EC.url_contains(Urls.ACCOUNT_PAGE))
        assert wait.until(
            EC.visibility_of_element_located(AccountPageLocators.profile_section)), "Раздел 'Профиль' не отображается"
        name_field = wait.until(EC.visibility_of_element_located(AccountPageLocators.name_input))
        assert name_field.get_attribute("value") == user.name, "Неверное имя пользователя"

    def test_navigate_from_account_to_constructor_via_constructor_link(self, create_driver):
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
        constructor_button = wait.until(EC.element_to_be_clickable(HomePageLocators.constructor_link))
        constructor_button.click()
        wait.until(EC.url_contains(Urls.MAIN_PAGE))
        assert "account" not in driver.current_url, "Не произошел выход из ЛК"

    def test_navigate_from_account_to_constructor_via_logo(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)
        driver.get(Urls.LOGIN_PAGE)
        user = UserData()
        wait.until(EC.visibility_of_element_located(LoginPageLocators.login_input)).send_keys(user.email)
        wait.until(EC.visibility_of_element_located(LoginPageLocators.password_input)).send_keys(user.password)
        wait.until(EC.element_to_be_clickable(LoginPageLocators.login_button)).click()
        wait.until(EC.element_to_be_clickable(HomePageLocators.account_link)).click()
        wait.until(EC.url_contains(Urls.ACCOUNT_PAGE))
        logo = wait.until(EC.element_to_be_clickable(HomePageLocators.logo))
        logo.click()
        wait.until(EC.url_contains(Urls.MAIN_PAGE))
        assert "account" not in driver.current_url, "Не произошел выход из ЛК"

    def test_sauces_section_navigation(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)
        driver.get(Urls.MAIN_PAGE)
        sauces_button = wait.until(EC.element_to_be_clickable(HomePageLocators.sauces_section))
        sauces_button.click()
        active_tab = wait.until(EC.visibility_of_element_located(HomePageLocators.active_section))
        assert "Соусы" in active_tab.text, "Раздел 'Соусы' не активирован"

    def test_fillings_section_navigation(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)
        driver.get(Urls.MAIN_PAGE)
        fillings_button = wait.until(EC.element_to_be_clickable(HomePageLocators.fillings_section))
        fillings_button.click()
        active_tab = wait.until(EC.visibility_of_element_located(HomePageLocators.active_section))
        assert "Начинки" in active_tab.text, "Раздел 'Начинки' не активирован"

    def test_buns_section_navigation(self, create_driver):
        driver = create_driver
        wait = WebDriverWait(driver, timeout=10)
        driver.get(Urls.MAIN_PAGE)
        sauces_button = wait.until(EC.element_to_be_clickable(HomePageLocators.sauces_section))
        sauces_button.click()

        buns_button = wait.until(EC.element_to_be_clickable(HomePageLocators.buns_section))
        buns_button.click()