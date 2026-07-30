from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()
    total_text = ""

    try:
        wait = WebDriverWait(driver, 10)
        driver.get("https://www.saucedemo.com/")

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        wait.until(
            EC.presence_of_element_located(
                (By.ID, "add-to-cart-sauce-labs-backpack")
            )
        ).click()
        driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()
        driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie"
        ).click()

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        wait.until(EC.presence_of_element_located((By.ID, "checkout"))).click()

        driver.find_element(By.ID, "first-name").send_keys("Ivan")
        driver.find_element(By.ID, "last-name").send_keys("Petrov")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()

        wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        total_element = driver.find_element(
            By.CLASS_NAME, "summary_total_label"
        )
        total_text = total_element.text

    finally:
        driver.quit()

    assert "$58.29" in total_text, \
        f"Ожидалась сумма $58.29, но получено: {total_text}"
