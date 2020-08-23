import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CompanyPage(BasePage):

    title_company = (By.CSS_SELECTOR, 'a.page-header__info-title')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_name_company_from_profile(self):
        with allure.step(f'Получаем название компании из профиля компании'):
            item = self.find_element(self.driver, self.title_company)
            self.name_company = item.get_attribute('textContent')
            self.logger.info(f'Название компании, которое указано в профиле "{self.name_company}"')