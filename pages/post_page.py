import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class PostPage(BasePage):

    post_title = (By.CSS_SELECTOR, 'span.post__title-text')
    searched_item = (By.CSS_SELECTOR, 'em.searched-item')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_post_title(self):
        item = self.find_element(self.driver, self.post_title)
        self.name_post = item.get_attribute('textContent')
        self.logger.info(f'Получили название открывшегося поста "{self.name_post}"')
