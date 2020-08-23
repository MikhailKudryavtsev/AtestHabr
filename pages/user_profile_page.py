import os
import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class UserProfilePage(BasePage):

    button_settings_profile = (By.CSS_SELECTOR, 'a.btn.btn_blue.btn_x-large')
    user_avatar = (By.CSS_SELECTOR, 'img.user-avatar__image')
    loading_img_avatar = (By.CSS_SELECTOR, 'div.form-fileupload__image.is-loading')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_settings_profile(self):
        with allure.step('Открываем настройки профиля'):
            self.find_element(self.driver, self.button_settings_profile).click()
            self.logger.info(f'Нажали кнопку открытия настроек профиля {self.button_settings_profile}')

    def upload_avatar(self):
        with allure.step('Загружаем изображение для аватра пользователя'):
            cwd = os.getcwd()
            file = f'{cwd}/tests/1.png'
            el = self.driver.execute_script('return document.getElementsByClassName("form-fileupload__input");')
            self.button_load_avatar = el[0]
            self.button_load_avatar.send_keys(file)
            self.logger.info(f'Загрузили изображение {file}')
