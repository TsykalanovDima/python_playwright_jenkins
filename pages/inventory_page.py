from pages.base_page import BasePage


class InventoryPage(BasePage):
    INVENTORY_ITEM = ".inventory_item"
    ADD_TO_CART_BUTTON = "button.btn_inventory"
    CART_ICON = ".shopping_cart_link"
    CART_ITEM = ".cart_item"

    def get_items_count(self):
        return self.page.locator(self.INVENTORY_ITEM).count()

    def add_item_to_cart_by_index(self, index=0):
        self.page.locator(self.ADD_TO_CART_BUTTON).nth(index).click()

    def go_to_cart(self):
        self.page.locator(self.CART_ICON).click()

    def get_cart_items_count(self):
        return self.page.locator(self.CART_ITEM).count()

    def get_cart_badge_count(self):
        badge = self.page.locator(".shopping_cart_badge")
        return badge.inner_text() if badge.is_visible() else "0"

    def remove_item_from_cart_by_index(self, index=0):
        self.page.locator(".cart_button").nth(index).click()
