from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options


def test_form():
    options = Options()
    driver = webdriver.Edge(options=options)

    try:
        wait = WebDriverWait(driver, 10)
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

        driver.find_element(By.NAME, "first-name").send_keys("Иван")
        driver.find_element(By.NAME, "last-name").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
        driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        driver.find_element(By.NAME, "city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME, "job-position").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")

        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        wait.until(EC.url_contains("data-types-submitted.html"))

        zip_code_element = wait.until(
            EC.visibility_of_element_located((By.ID, "zip-code"))
        )
        assert "alert-danger" in zip_code_element.get_attribute("class"), \
            "Поле Zip code должно быть подсвечено красным"

        other_fields = [
            "first-name", "last-name", "address", "city", "country",
            "e-mail", "phone", "job-position", "company"
        ]
        for field_id in other_fields:
            element = wait.until(
                EC.visibility_of_element_located((By.ID, field_id))
            )
            assert "alert-success" in element.get_attribute("class"), \
                f"Поле {field_id} должно быть подсвечено зеленым"

    finally:
        driver.quit()
