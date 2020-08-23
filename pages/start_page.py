import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class StartPage(BasePage):

    button_login = (By.XPATH, '//*[@id="login"]')
    profile_button = (By.CSS_SELECTOR, 'button.btn.btn_medium.btn_navbar_user-dropdown')
    year_button = (By.XPATH, '//a[@title="Лучшие публикации за год"]')
    post_time = (By.CSS_SELECTOR, 'span.post__time')
    list_service_button = (By.CSS_SELECTOR, 'span#dropdown-control')
    button_user_info = (By.CSS_SELECTOR, 'a.dropdown__user-info.user-info')
    button_read_more = (By.XPATH, '//article/div/a')
    title_post = (By.XPATH, '//article/h2/a')
    search_button = (By.ID, 'search-form-btn')
    search_form_field = (By.ID, 'search-form-field')
    search_form_button = (By.ID, 'search-form-btn')
    english_radiobutton = (By.XPATH, '//label[contains(text(), "English")]')
    language_settings_button = (By.CSS_SELECTOR, 'button.btn.btn_medium.btn_navbar_lang.js-show_lang_settings')
    language_settings_form_header = (By.CSS_SELECTOR, 'span.popup__head-title.js-popup_title')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_form_authorization(self):
        with allure.step('Открываетм форму авторизации'):
            self.find_element(self.driver, self.button_login).click()
            self.logger.info(f'Нажали кнопку "Войти" {self.button_login}')

    def open_posts_from_year(self):
        with allure.step('Открываем Лучшие публикации за год'):
            self.find_element(self.driver, self.year_button).click()
            self.logger.info(f'Нажали кнопку "Год" {self.year_button}')

    def open_all_habr_services(self):
        with allure.step('Открываем список сервисов Хабра'):
            self.find_element(self.driver, self.list_service_button).click()
            self.logger.info(f'Нажали кнопку открытия списка сервисов Хабра {self.list_service_button}')

    def open_service_habr(self, number_service):
        self.open_all_habr_services()
        with allure.step(f'Открываем сервис под номером "{number_service}"'):
            self.find_element(self.driver, (By.XPATH, f'//*[@id="dropdown"]/a[{number_service}]/p')).click()
            self.logger.info(f'Нажали кнопку открытия сервиса под номером {number_service}')

    def choose_a_company(self, number_company):
        with allure.step('Выбираем компанию рандомную компанию'):
            company = self.find_element(self.driver, (By.XPATH, f'//li[{number_company}]/div[1]/a[2]'))
            self.name_company = company.get_attribute('textContent')
            company.click()
            self.logger.info(f'Нажали на компанию {self.name_company}')

    def open_profile_menu(self):
        self.find_element(self.driver, self.profile_button).click()
        self.logger.info(f'Нажали на кнопку открытия меню профиля {self.profile_button}')

    def open_user_profile(self):
        with allure.step('Открываем страницу профиля пользователя'):
            self.open_profile_menu()
            self.find_element(self.driver, self.button_user_info).click()
            self.logger.info(f'Нажали на кнопку открытия страницы профиля пользователя {self.button_user_info}')

    def open_post(self):
        with allure.step('Открываем первый пост'):
            item = self.find_element(self.driver, self.title_post)
            self.name_post = item.get_attribute('textContent')
            self.find_element(self.driver, self.button_read_more).click()
            self.logger.info(f'Нажали на кнопку "Читать дальше" {self.button_read_more}')

    def input_text_in_search(self, word):
        with allure.step(f'Вводим в поле поска слово "{word}"'):
            self.find_element(self.driver, self.search_button).click()
            self.find_element(self.driver, self.search_form_field).send_keys(word)
            action = ActionChains(self.driver)
            action.key_down(Keys.ENTER).perform()
            self.logger.info(f'Ищем слово {word}')

    def open_language_settings(self):
        with allure.step('Открываем форму настройи языка'):
            self.find_element(self.driver, self.language_settings_button).click()
            self.logger.info(f'Нажали на кнопку открытия настроек языка {self.language_settings_button}')

    def set_english_language(self):
        self.open_language_settings()
        with allure.step('Устанавливаем английский язык'):
            self.find_element(self.driver, self.english_radiobutton).click()
            self.logger.info(f'Поставили радиобатон на английский язык {self.english_radiobutton}')
