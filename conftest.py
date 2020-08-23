import pytest
import logging
from selenium.webdriver import Chrome, ChromeOptions
from pages.authorization_page import AuthorizationPage
from pages.company_page import CompanyPage
from pages.post_page import PostPage
from pages.start_page import StartPage
from pages.user_profile_page import UserProfilePage

logger = logging.getLogger(__name__)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s : %(message)s', level=logging.INFO,
                    filename='Habr.log')


@pytest.fixture
def driver(request):
    options = ChromeOptions()
    options.add_argument('start-maximized')
    wd = Chrome(options=options)
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture
def company_page(driver):
    page = CompanyPage(driver)
    return page


@pytest.fixture
def user_profile_page(driver):
    page = UserProfilePage(driver)
    return page


@pytest.fixture
def start_page(driver):
    page = StartPage(driver)
    return page


@pytest.fixture
def auth_page(driver):
    page = AuthorizationPage(driver)
    return page


@pytest.fixture
def post_page(driver):
    page = PostPage(driver)
    return page
