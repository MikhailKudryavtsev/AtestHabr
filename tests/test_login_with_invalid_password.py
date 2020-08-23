import allure
import os
from selenium.common.exceptions import TimeoutException

email = os.getenv('email')


@allure.feature("UI")
@allure.story("Проверка авторизации")
@allure.title("Тест авторизации с неверным паролем")
def test_login_with_invalid_password(start_page, auth_page):
    try:
        start_page.open_habr()
        start_page.open_form_authorization()
        auth_page.enter_in_account(email, 'test')
        with allure.step('Проверяем, что появилось сообщение об ошибке'):
            auth_page.find_element(auth_page.driver, auth_page.notice_text)
    except TimeoutException as e:
        allure.attach(body=start_page.driver.get_screenshot_as_png(),
                      name='screenshot_image',
                      attachment_type=allure.attachment_type.PNG)
        raise AssertionError(e.msg)
