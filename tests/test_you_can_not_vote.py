import allure
import pytest
from selenium.webdriver.common.by import By


@allure.feature("UI")
@allure.story("Проверка UI на странице поста")
@allure.title('Тест проверки, что не зарегистрированные пользователи не могут проголосовать')
def test_you_can_not_vote(start_page, post_page):
    start_page.open_habr()
    start_page.open_post()
    try:
        with allure.step('Проверяем, что не зарегистрированные пользователи не могут проголосовать'):
            item = post_page.find_element(post_page.driver,
                                          (By.XPATH, '//li[1]/div/button[1]'))
            text = 'Голосовать могут только зарегистрированные пользователи'
            assert text == item.get_attribute('title')
    except AssertionError as e:
        allure.attach(body=start_page.driver.get_screenshot_as_png(),
                      name='screenshot_image',
                      attachment_type=allure.attachment_type.PNG)
        pytest.fail(str(e))
