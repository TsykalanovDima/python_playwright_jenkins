import os
from pages.login_page import LoginPage
from dotenv import load_dotenv


load_dotenv()


def test_successful_login(page):
    login_page = LoginPage(page)
    login_page.navigate(os.getenv("BASE_URL"))
    login_page.login(os.getenv("USERNAME"), os.getenv("PASSWORD"))
    assert "inventory" in page.url
