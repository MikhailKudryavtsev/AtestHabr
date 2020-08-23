import allure
import logging
import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://habr.com/ru/'
        self.logger = logging.getLogger(type(self).__name__)

    def open_habr(self):
        with allure.step('Переход на habr.com'):
            self.driver.get(self.url)
            self.logger.info(f'Открыли страницу {self.url}')

    @staticmethod
    def find_element(driver, locator):
        return WebDriverWait(driver, 15).until(ec.visibility_of_element_located(locator),
                                               message=f"Can't find element by locator {locator}")

    @staticmethod
    def find_elements(driver, locator):
        return WebDriverWait(driver, 15).until(ec.visibility_of_all_elements_located(locator),
                                               message=f"Can't find elements by locator {locator}")

    @staticmethod
    def element_disappearance(driver, locator):
        return WebDriverWait(driver, 15).until(ec.invisibility_of_element(locator),
                                               message=f"Didn't wait for element to disappear by {locator}")

    def determine_last_year(self):
        self.year = datetime.datetime.today().strftime("%Y")
        self.last_year = int(self.year) - 1

    def get_title(self):
        self.my_title = self.driver.title
        self.logger.info(f'Получаем title страницы {self.my_title}')
