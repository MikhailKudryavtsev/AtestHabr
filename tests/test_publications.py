import allure
import pytest


@allure.feature("UI")
@allure.story("Проверка UI на стартовой странице")
@allure.title('Тест ображения публикаций за "Год"')
def test_publications_per_year(start_page):
    try:
        start_page.open_habr()
        start_page.determine_last_year()
        start_page.open_posts_from_year()
        with allure.step(f'Проверяем, что год в постах равен {start_page.year} или {start_page.last_year}'):
            elements = start_page.find_elements(start_page.driver, start_page.post_time)
            for i in range(len(elements)):
                text = elements[i].get_attribute('textContent')
                assert str(start_page.year) or start_page.last_year in text
    except AssertionError as e:
        allure.attach(body=start_page.driver.get_screenshot_as_png(),
                      name='screenshot_image',
                      attachment_type=allure.attachment_type.PNG)
        pytest.fail(str(e))
