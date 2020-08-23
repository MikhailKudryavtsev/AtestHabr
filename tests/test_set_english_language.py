import allure
import pytest



@allure.feature("UI")
@allure.story("Проверка UI на стартовой странице")
@allure.title('Тест проверки переключения языка интерфейса на английский')
def test_set_english_language(start_page):
    start_page.open_habr()
    start_page.set_english_language()
    try:
        with allure.step('Проверяем, что язык интерфейса переключился на английский'):
            item = start_page.find_element(start_page.driver, start_page.language_settings_form_header)
            assert 'Language settings' == item.get_attribute('textContent')
    except AssertionError as e:
        allure.attach(body=start_page.driver.get_screenshot_as_png(),
                      name='screenshot_image',
                      attachment_type=allure.attachment_type.PNG)
        pytest.fail(str(e))
