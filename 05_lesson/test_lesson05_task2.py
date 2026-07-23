from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")

    # Запоминаем исходный URL для последующей проверки
    original_url = driver.current_url

    # Находим поле ввода по атрибуту name и вводим имя
    driver.find_element(By.NAME, "custname").send_keys("TestUser")

    # Находим кнопку Submit по тексту и нажимаем на нее
    driver.find_element(By.XPATH, "//*[text()='Submit']").click()

    # Проверяем, что после нажатия URL изменился
    assert driver.current_url != original_url, (
         "URL не изменился после отправки формы")

    driver.quit()
