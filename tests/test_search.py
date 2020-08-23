import allure
import pytest

word = 'pytest'


@allure.feature("UI")
@allure.story("Проверка UI на странице поиска")
@allure.title('Тест поиска постов по ключевому слову')
def test_search(start_page, post_page):
    start_page.open_habr()
    start_page.input_text_in_search(word)
    try:
        with allure.step(f'Проверяем, что найденные посты содержат слово {word}'):
            elements = post_page.find_elements(post_page.driver, post_page.searched_item)
            for i in range(len(elements)):
                text = elements[i].get_attribute('textContent').lower()
                assert word in text
    except AssertionError as e:
        allure.attach(body=start_page.driver.get_screenshot_as_png(),
                      name='screenshot_image',
                      attachment_type=allure.attachment_type.PNG)
        pytest.fail(str(e))
