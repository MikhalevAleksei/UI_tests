import pytest
from faker import Faker
from selenium import webdriver

from data import Urls
from pages.ingredient_page import IngredientPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.order_history_page import OrderHistoryPage
from pages.profile_page import ProfilePage
from pages.reset_password_page import ResetPasswordPage
from pages.register_page import RegisterPage


@pytest.fixture(scope='function')
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size-1920,1080')
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(Urls.main_url)
    yield driver
    driver.quit()


@pytest.fixture()
def new_fake_data():
    fake = Faker(locale="ru_RU")
    fake_email = fake.ascii_free_email()
    fake_password = fake.job()
    fake_name = fake.first_name()

    fake_data = {
        "email": fake_email,
        "password": fake_password,
        "name": fake_name
    }

    return fake_data


@pytest.fixture()
def make_order(
        driver, main_page, login_page, register_page):
    main_page.make_order()
    main_page.click_to_close_popup_success_order_btn()


@pytest.fixture()
def make_order_and_transfer_to_history_orders(driver, make_order, main_page,
                                              profile_page):
    main_page.transfer_to_personal_area_after_order()
    profile_page.click_history_of_orders()


@pytest.fixture()
def main_page(driver):
    page = MainPage(driver)
    return page


@pytest.fixture()
def login_page(driver):
    page = LoginPage(driver)
    return page


@pytest.fixture()
def forgot_password_page(driver):
    page = ForgotPasswordPage(driver)
    return page


@pytest.fixture()
def reset_password_page(driver):
    page = ResetPasswordPage(driver)
    return page


@pytest.fixture()
def register_page(driver):
    page = RegisterPage(driver)
    return page


@pytest.fixture()
def ingredient_page(driver):
    page = IngredientPage(driver)
    return page


@pytest.fixture()
def order_history_page(driver):
    page = OrderHistoryPage(driver)
    return page


@pytest.fixture()
def profile_page(driver):
    page = ProfilePage(driver)
    return page
