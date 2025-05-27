from selenium.webdriver.common.by import By


class HomePageLocators:
    login_account_button = (By.XPATH, "//button[text()='Войти в аккаунт']")
    account_link = (By.XPATH, "//a[@href='/account']")
    constructor_link = (By.XPATH, "//a[@href='/']")
    logo = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")
    buns_section = (By.XPATH, "//span[text()='Булки']/..")
    sauces_section = (By.XPATH, "//span[text()='Соусы']/..")
    fillings_section = (By.XPATH, "//span[text()='Начинки']/..")
    active_section = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")


class LoginPageLocators:
    login_label = (By.XPATH, "//h2[text()='Вход']")
    login_input = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    password_input = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    login_button = (By.XPATH, "//button[text()='Войти']")
    registration_link = (By.XPATH, "//a[@href='/register']")
    restore_password_link = (By.XPATH, "//a[@href='/forgot-password']")


class RegistrationPageLocators:
    name_input = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    email_input = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    password_input = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    register_button = (By.XPATH, "//button[text()='Зарегистрироваться']")
    password_error = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")
    login_link = (By.XPATH, "//a[contains(@href, '/login')]")


class AccountPageLocators:
    name_input = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    login_input = (By.XPATH, "//label[text()='Логин']/following-sibling::input")
    password_input = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    logout_button = (By.XPATH, "//button[contains(text(),'Выход')]")
    profile_section = (By.XPATH, "//a[text()='Профиль']")


class PasswordRecoveryPageLocators:
    login_link = (By.XPATH, "//a[contains(@href, '/login')]")









