import os
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from dotenv import load_dotenv

load_dotenv()


def test_add_one_item_to_cart(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.navigate(os.getenv("BASE_URL"))
    login_page.login(os.getenv("USERNAME"), os.getenv("PASSWORD"))

    assert inventory_page.get_items_count() > 0
    inventory_page.add_item_to_cart_by_index(0)
    inventory_page.go_to_cart()
    assert inventory_page.get_cart_items_count() == 1


def test_add_all_items_to_cart(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.navigate(os.getenv("BASE_URL"))
    login_page.login(os.getenv("USERNAME"), os.getenv("PASSWORD"))

    items_count = inventory_page.get_items_count()
    for i in range(items_count):
        inventory_page.add_item_to_cart_by_index(i)

    inventory_page.go_to_cart()
    assert inventory_page.get_cart_items_count() == items_count


def test_add_and_remove_item_from_cart(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.navigate(os.getenv("BASE_URL"))
    login_page.login(os.getenv("USERNAME"), os.getenv("PASSWORD"))

    inventory_page.add_item_to_cart_by_index(0)
    assert inventory_page.get_cart_badge_count() == "1"

    inventory_page.go_to_cart()
    inventory_page.remove_item_from_cart_by_index(0)
    assert inventory_page.get_cart_items_count() == 0
