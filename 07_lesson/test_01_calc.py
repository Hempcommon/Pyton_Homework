from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class SlowCalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)
        self.url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )
        self.delay_input = (By.ID, "delay")
        self.result_screen = (By.CSS_SELECTOR, ".screen")

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, value):
        element = self.wait.until(
            EC.presence_of_element_located(self.delay_input)
        )
        element.clear()
        element.send_keys(str(value))

    def click_button(self, text):
        locator = (
            By.XPATH,
            f"//span[(contains(@class, 'btn') or "
            f"contains(@class, 'operator')) "
            f"and normalize-space(text())='{text}']"
        )
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def get_result(self):
        time.sleep(50)
        element = self.driver.find_element(*self.result_screen)
        full_text = element.text

        if "=" in full_text:
            result_value = full_text.split("=")[-1].strip()
            return f"Result: {result_value}"

        return f"Result: {full_text}"


def test_calculator():
    driver = webdriver.Chrome()
    calc_result = ""

    try:
        calc_page = SlowCalculatorPage(driver)
        calc_page.open()

        calc_page.set_delay(45)
        calc_page.click_button("7")
        calc_page.click_button("+")
        calc_page.click_button("8")
        calc_page.click_button("=")

        calc_result = calc_page.get_result()

    finally:
        driver.quit()

    assert calc_result == "Result: 15", \
        f"Ожидался результат 'Result: 15', но получено: '{calc_result}'"
