import allure
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Page Object страницы авторизации."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует страницу авторизации.

        Args:
            driver: Экземпляр браузера Selenium.

        Returns:
            None.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.url = "https://www.saucedemo.com/"
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_btn = (By.ID, "login-button")

    def open(self) -> None:
        """Открывает страницу авторизации.

        Returns:
            None.
        """
        self.driver.get(self.url)

    def login(self, username: str, password: str) -> None:
        """Авторизует пользователя.

        Args:
            username: Имя пользователя.
            password: Пароль пользователя.

        Returns:
            None.
        """
        self.wait.until(
            EC.presence_of_element_located(self.username_input)
        ).send_keys(username)
        self.driver.find_element(
            *self.password_input
        ).send_keys(password)
        self.driver.find_element(*self.login_btn).click()


class ProductsPage:
    """Page Object страницы товаров."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует страницу товаров.

        Args:
            driver: Экземпляр браузера Selenium.

        Returns:
            None.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.backpack_btn = (
            By.ID,
            "add-to-cart-sauce-labs-backpack"
        )
        self.tshirt_btn = (
            By.ID,
            "add-to-cart-sauce-labs-bolt-t-shirt"
        )
        self.onesie_btn = (
            By.ID,
            "add-to-cart-sauce-labs-onesie"
        )
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def add_backpack(self) -> None:
        """Добавляет рюкзак в корзину.

        Returns:
            None.
        """
        self.wait.until(
            EC.element_to_be_clickable(self.backpack_btn)
        ).click()

    def add_tshirt(self) -> None:
        """Добавляет футболку в корзину.

        Returns:
            None.
        """
        self.wait.until(
            EC.element_to_be_clickable(self.tshirt_btn)
        ).click()

    def add_onesie(self) -> None:
        """Добавляет комбинезон в корзину.

        Returns:
            None.
        """
        self.wait.until(
            EC.element_to_be_clickable(self.onesie_btn)
        ).click()

    def get_cart_count(self) -> int:
        """Возвращает количество товаров в корзине.

        Returns:
            int: Количество товаров в корзине.
        """
        try:
            element = self.driver.find_element(*self.cart_badge)
            return int(element.text)
        except Exception:
            return 0

    def go_to_cart(self) -> None:
        """Переходит в корзину.

        Returns:
            None.
        """
        self.wait.until(
            EC.element_to_be_clickable(self.cart_link)
        ).click()


class CartPage:
    """Page Object страницы корзины."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует страницу корзины.

        Args:
            driver: Экземпляр браузера Selenium.

        Returns:
            None.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.checkout_btn = (By.ID, "checkout")
        self.cart_items = (By.CLASS_NAME, "cart_item")

    def get_cart_items_count(self) -> int:
        """Возвращает количество товаров в корзине.

        Returns:
            int: Количество товаров в корзине.
        """
        return len(self.driver.find_elements(*self.cart_items))

    def click_checkout(self) -> None:
        """Переходит к оформлению заказа.

        Returns:
            None.
        """
        self.wait.until(
            EC.element_to_be_clickable(self.checkout_btn)
        ).click()


class CheckoutPage:
    """Page Object страницы оформления заказа."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует страницу оформления заказа.

        Args:
            driver: Экземпляр браузера Selenium.

        Returns:
            None.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_btn = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_info(
        self,
        first_name: str,
        last_name: str,
        postal_code: str
    ) -> None:
        """Заполняет данные покупателя.

        Args:
            first_name: Имя покупателя.
            last_name: Фамилия покупателя.
            postal_code: Почтовый индекс.

        Returns:
            None.
        """
        self.wait.until(
            EC.presence_of_element_located(self.first_name_input)
        ).send_keys(first_name)
        self.driver.find_element(
            *self.last_name_input
        ).send_keys(last_name)
        self.driver.find_element(
            *self.postal_code_input
        ).send_keys(postal_code)

    def click_continue(self) -> None:
        """Переходит к итоговой информации о заказе.

        Returns:
            None.
        """
        self.wait.until(
            EC.element_to_be_clickable(self.continue_btn)
        ).click()

    def get_total_price(self) -> str:
        """Возвращает итоговую стоимость заказа.

        Returns:
            str: Итоговая стоимость заказа.
        """
        element = self.wait.until(
            EC.visibility_of_element_located(self.total_label)
        )
        return element.text


@allure.title("Проверка оформления заказа в интернет-магазине")
@allure.description(
    "Проверка добавления трех товаров в корзину "
    "и итоговой стоимости заказа"
)
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop() -> None:
    """Проверяет добавление товаров и оформление заказа.

    Returns:
        None.
    """
    driver = webdriver.Firefox()
    total_text = ""

    try:
        login_page = LoginPage(driver)

        with allure.step("Открыть страницу авторизации"):
            login_page.open()

        with allure.step("Авторизоваться под стандартным пользователем"):
            login_page.login("standard_user", "secret_sauce")

        products_page = ProductsPage(driver)

        with allure.step("Добавить рюкзак в корзину"):
            products_page.add_backpack()

        with allure.step("Добавить футболку в корзину"):
            products_page.add_tshirt()

        with allure.step("Добавить комбинезон в корзину"):
            products_page.add_onesie()

        with allure.step("Проверить количество товаров в корзине"):
            assert products_page.get_cart_count() == 3, (
                f"В корзине должно быть 3 товара, "
                f"а не {products_page.get_cart_count()}"
            )

        with allure.step("Перейти в корзину"):
            products_page.go_to_cart()

        cart_page = CartPage(driver)

        with allure.step("Проверить количество товаров в корзине"):
            assert cart_page.get_cart_items_count() == 3, (
                f"В корзине должно быть 3 товара, "
                f"а не {cart_page.get_cart_items_count()}"
            )

        with allure.step("Перейти к оформлению заказа"):
            cart_page.click_checkout()

        checkout_page = CheckoutPage(driver)

        with allure.step("Заполнить данные покупателя"):
            checkout_page.fill_info("Ivan", "Petrov", "12345")

        with allure.step("Продолжить оформление заказа"):
            checkout_page.click_continue()

        with allure.step("Получить итоговую стоимость"):
            total_text = checkout_page.get_total_price()

    finally:
        driver.quit()

    with allure.step("Проверить итоговую стоимость заказа"):
        assert total_text == "Total: $58.29", (
            f"Ожидалась сумма 'Total: $58.29', "
            f"но получено: '{total_text}'"
        )


if __name__ == "__main__":
    test_shop()
