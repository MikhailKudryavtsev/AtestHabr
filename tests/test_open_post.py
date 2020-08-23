import allure
import pytest


@allure.feature("UI")
@allure.story("Проверка UI на стартовой странице")
@allure.title('Тест открытия поста')
def test_open_post(start_page, post_page):
    start_page.open_habr()
    start_page.open_post()
    try:
        with allure.step('Проверяем, что открылся нужный пост'):
            post_page.get_post_title()
            assert start_page.name_post == post_page.name_post
    except AssertionError as e:
        allure.attach(body=start_page.driver.get_screenshot_as_png(),
                      name='screenshot_image',
                      attachment_type=allure.attachment_type.PNG)
        pytest.fail(str(e))
