import allure
import os
import pytest

username = os.getenv('username')
email = os.getenv('email')
password = os.getenv('password')


@allure.feature("UI")
@allure.story("Проверка авторизации")
@allure.title("Тест успешной авторизации")
def test_login_with_valid_data(start_page, auth_page):
    try:
        start_page.open_habr()
        start_page.open_form_authorization()
        auth_page.enter_in_account(email, password)
        with allure.step('Проверяем, что в title кнопки профайла наш username'):
            button = start_page.find_element(start_page.driver, start_page.profile_button)
            assert username == button.get_attribute('title')
    except AssertionError as e:
        allure.attach(body=start_page.driver.get_screenshot_as_png(),
                      name='screenshot_image',
                      attachment_type=allure.attachment_type.PNG)
        pytest.fail(str(e))
