import os
import allure
import pytest
from selenium.common.exceptions import TimeoutException

email = os.getenv('email')
password = os.getenv('password')


@allure.feature("UI")
@allure.story("Проверка UI на странице профиля пользователя")
@allure.title('Тест загрузки изображения для пользователя')
def test_upload_avatar(start_page, auth_page, user_profile_page):
    start_page.open_habr()
    start_page.open_form_authorization()
    auth_page.enter_in_account(email, password)
    start_page.open_user_profile()
    user_profile_page.open_settings_profile()
    user_profile_page.upload_avatar()
    try:
        with allure.step('Ожидаем появления изображения, которое было загружено'):
            user_profile_page.element_disappearance(user_profile_page.driver, user_profile_page.loading_img_avatar)
            user_profile_page.find_element(user_profile_page.driver, user_profile_page.user_avatar)
    except TimeoutException as e:
        allure.attach(body=start_page.driver.get_screenshot_as_png(),
                      name='screenshot_image',
                      attachment_type=allure.attachment_type.PNG)
        pytest.fail(str(e))
