from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.url = "https://www.saucedemo.com/"
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_btn = (By.ID, "login-button")

    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.wait.until(
            EC.presence_of_element_located(self.username_input)
        ).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_btn).click()


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.backpack_btn = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.tshirt_btn = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.onesie_btn = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def add_backpack(self):
        self.wait.until(
            EC.element_to_be_clickable(self.backpack_btn)
        ).click()

    def add_tshirt(self):
        self.wait.until(
            EC.element_to_be_clickable(self.tshirt_btn)
        ).click()

    def add_onesie(self):
        self.wait.until(
            EC.element_to_be_clickable(self.onesie_btn)
        ).click()

    def get_cart_count(self):
        try:
            element = self.driver.find_element(*self.cart_badge)
            return int(element.text)
        except Exception:
            return 0

    def go_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.cart_link)
        ).click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.checkout_btn = (By.ID, "checkout")
        self.cart_items = (By.CLASS_NAME, "cart_item")

    def get_cart_items_count(self):
        return len(self.driver.find_elements(*self.cart_items))

    def click_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.checkout_btn)
        ).click()


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_btn = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_info(self, first_name, last_name, postal_code):
        self.wait.until(
            EC.presence_of_element_located(self.first_name_input)
        ).send_keys(first_name)
        self.driver.find_element(
            *self.last_name_input
        ).send_keys(last_name)
        self.driver.find_element(
            *self.postal_code_input
        ).send_keys(postal_code)

    def click_continue(self):
        self.wait.until(
            EC.element_to_be_clickable(self.continue_btn)
        ).click()

    def get_total_price(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.total_label)
        )
        return element.text


def test_shop():
    driver = webdriver.Firefox()
    total_text = ""

    try:
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        products_page = ProductsPage(driver)
        products_page.add_backpack()
        products_page.add_tshirt()
        products_page.add_onesie()

        assert products_page.get_cart_count() == 3, (
            f"В корзине должно быть 3 товара, "
            f"а не {products_page.get_cart_count()}"
        )

        products_page.go_to_cart()

        cart_page = CartPage(driver)
        assert cart_page.get_cart_items_count() == 3, (
            f"В корзине должно быть 3 товара, "
            f"а не {cart_page.get_cart_items_count()}"
        )

        cart_page.click_checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.fill_info("Ivan", "Petrov", "12345")
        checkout_page.click_continue()

        total_text = checkout_page.get_total_price()

    finally:
        driver.quit()

    assert total_text == "Total: $58.29", (
        f"Ожидалась сумма 'Total: $58.29', "
        f"но получено: '{total_text}'"
    )
