import allure
import pytest
import random

number_company = random.randint(1, 10)


@allure.feature("UI")
@allure.story("Проверка UI на стартовой странице")
@allure.title('Тест перехода на профиль компании')
def test_transition_to_company_profile(start_page, company_page):
    try:
        start_page.open_habr()
        start_page.choose_a_company(number_company)
        with allure.step('Проверяем, что открлась нужная копания'):
            company_page.get_name_company_from_profile()
            assert start_page.name_company == company_page.name_company
    except AssertionError as e:
        allure.attach(body=start_page.driver.get_screenshot_as_png(),
                      name='screenshot_image',
                      attachment_type=allure.attachment_type.PNG)
        pytest.fail(str(e))
