import os
from pages.login_page import LoginPage


def test_login_without_password(page):
    login_page = LoginPage(page)
    login_page.navigate(os.getenv("BASE_URL"))
    login_page.login(os.getenv("USERNAME"), "")
    assert "Epic sadface" in login_page.get_error_message()


def test_login_without_username(page):
    login_page = LoginPage(page)
    login_page.navigate(os.getenv("BASE_URL"))
    login_page.login("", os.getenv("PASSWORD"))
    assert "Epic sadface" in login_page.get_error_message()
