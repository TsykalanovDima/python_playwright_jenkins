import os
from dotenv import load_dotenv
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

load_dotenv()


def test_nonexistent_item_not_visible(page):
    login_page = LoginPage(page)
    login_page.navigate(os.getenv("BASE_URL"))
    login_page.login(os.getenv("USERNAME"), os.getenv("PASSWORD"))
    fake_item = page.locator("//div[text()='Nonexistent Item']")
    assert not fake_item.is_visible(), "item not exist"
