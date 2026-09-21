import allure
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SlowCalculatorPage:
    """Page Object страницы медленного калькулятора."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует страницу калькулятора.

        Args:
            driver: Экземпляр браузера Selenium.

        Returns:
            None.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 70)
        self.url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )
        self.delay_input = (By.ID, "delay")
        self.result_screen = (By.CSS_SELECTOR, ".screen")

    def open(self) -> None:
        """Открывает страницу медленного калькулятора.

        Returns:
            None.
        """
        self.driver.get(self.url)

    def set_delay(self, value: int) -> None:
        """Устанавливает задержку вычисления.

        Args:
            value: Задержка вычисления в секундах.

        Returns:
            None.
        """
        element = self.wait.until(
            EC.presence_of_element_located(self.delay_input)
        )
        element.clear()
        element.send_keys(str(value))

    def click_button(self, text: str) -> None:
        """Нажимает кнопку калькулятора.

        Args:
            text: Текст кнопки, которую необходимо нажать.

        Returns:
            None.
        """
        locator = (
            By.XPATH,
            f"//span[(contains(@class, 'btn') or "
            f"contains(@class, 'operator')) "
            f"and normalize-space(text())='{text}']"
        )
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def get_result(self) -> str:
        """Получает результат вычисления.

        Returns:
            str: Результат вычисления в формате "Result: число".
        """
        element: WebElement = self.wait.until(
            EC.presence_of_element_located(self.result_screen)
        )

        initial_text = element.text

        self.wait.until(
            lambda driver: element.text != initial_text
        )

        full_text = element.text

        if "=" in full_text:
            result_value = full_text.split("=")[-1].strip()
            return f"Result: {result_value}"

        return f"Result: {full_text}"


@allure.title("Проверка работы медленного калькулятора")
@allure.description(
    "Проверка сложения чисел 7 и 8 "
    "с установленной задержкой вычисления"
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator() -> None:
    """Проверяет сложение двух чисел в калькуляторе.

    Returns:
        None.
    """
    driver = webdriver.Chrome()
    calc_result = ""

    try:
        calc_page = SlowCalculatorPage(driver)

        with allure.step("Открыть страницу калькулятора"):
            calc_page.open()

        with allure.step("Установить задержку 45 секунд"):
            calc_page.set_delay(45)

        with allure.step("Нажать кнопку 7"):
            calc_page.click_button("7")

        with allure.step("Нажать кнопку +"):
            calc_page.click_button("+")

        with allure.step("Нажать кнопку 8"):
            calc_page.click_button("8")

        with allure.step("Нажать кнопку ="):
            calc_page.click_button("=")

        with allure.step("Получить результат вычисления"):
            calc_result = calc_page.get_result()

    finally:
        driver.quit()

    with allure.step("Проверить, что результат равен Result: 15"):
        assert calc_result == "Result: 15", (
            f"Ожидался результат 'Result: 15', "
            f"но получено: '{calc_result}'"
        )


if __name__ == "__main__":
    test_calculator()
