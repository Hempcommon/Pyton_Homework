from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

    # Открываем главную страницу
    driver.get("https://httpbin.org/")
    original_url = driver.current_url

    # Находим и кликаем на ссылку "HTML Form"
    driver.find_element(By.LINK_TEXT, "HTML Form").click()

    # Проверяем, что URL изменился и содержит /forms/post
    assert "/forms/post" in driver.current_url, (
         f"Ожидался /forms/post в URL, получено: {driver.current_url}")

    # Возвращаемся назад на главную страницу
    driver.back()

    # Проверяем, что вернулись на исходный URL
    assert driver.current_url == original_url, (
         f"Ожидался возврат на {original_url}, получено: {driver.current_url}")

    driver.quit()
