import allure
import pytest

list_services = [('1', 'Лучшие публикации за сутки / Хабр'), ('2', 'Интересные вопросы — Хабр Q&A'),
                 ('3', 'Работа в IT-индустрии — Хабр Карьера'), ('4', 'Хабр Фриланс')]


@allure.feature("UI")
@allure.story("Проверка UI на стартовой странице")
@allure.title('Тест перехода на сервис Хабра')
@pytest.mark.parametrize('item', list_services, ids=['habr', 'q&a', 'career', 'freelance'])
def test_transition_to_service(item, start_page):
    try:
        start_page.open_habr()
        start_page.open_service_habr(item[0])
        with allure.step(f'Проверяем, что title страницы содержит "{item[1]}"'):
            start_page.get_title()
            assert item[1] == start_page.my_title
    except AssertionError as e:
        allure.attach(body=start_page.driver.get_screenshot_as_png(),
                      name='screenshot_image',
                      attachment_type=allure.attachment_type.PNG)
        pytest.fail(str(e))
