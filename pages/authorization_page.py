import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AuthorizationPage(BasePage):

    input_email = (By.XPATH, '//*[@id="email_field"]')
    input_password = (By.XPATH, '//*[@id="password_field"]')
    button_enter = (By.XPATH, '//button[contains(text(), "Войти")]')
    notice_text = (By.CSS_SELECTOR, 'div.notice__text')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_in_account(self, email, password):
        with allure.step('Заполняем форму авторизации и входим в аккаунт'):
            self.find_element(self.driver, self.input_email).send_keys(email)
            self.logger.info(f'Ввели email в поле {self.input_email}')
            self.find_element(self.driver, self.input_password).send_keys(password)
            self.logger.info(f'Ввели пароль в поле {self.input_password}')
            self.find_element(self.driver, self.button_enter).click()
            self.logger.info(f'Нажали на кнопку "Войти"{self.button_enter}')
