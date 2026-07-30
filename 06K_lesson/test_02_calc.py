from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():
    driver = webdriver.Chrome()

    try:
        wait = WebDriverWait(driver, 60)
        driver.get(
         "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

        delay_input = wait.until(
            EC.presence_of_element_located((By.ID, "delay"))
        )
        delay_input.clear()
        delay_input.send_keys("45")

        driver.find_element(
            By.XPATH, "//span[contains(@class, 'btn') and text()='7']"
        ).click()
        driver.find_element(
            By.XPATH, "//span[contains(@class, 'operator') and text()='+']"
        ).click()
        driver.find_element(
            By.XPATH, "//span[contains(@class, 'btn') and text()='8']"
        ).click()
        driver.find_element(
            By.XPATH, "//span[contains(@class, 'btn') and text()='=']"
        ).click()

        wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15"
            )
        )

        result = driver.find_element(By.CSS_SELECTOR, ".screen").text
        assert result == "15", f"Ожидался результат '15', получено: '{result}'"

    finally:
        driver.quit()
