from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/links/10")

    # Находим все ссылки на странице (тег <a>)
    links = driver.find_elements(By.TAG_NAME, "a")

    # Проверяем, что количество ссылок равно 9 (как указано в задании)
    # Примечание: httpbin.org/links/10 обычно генерирует 10 ссылок.
    # Если тест падает на реальном сайте, попробуйте изменить значение на 10.
    assert len(links) == 9, (
         f"Ожидалось 9 ссылок, найдено: {len(links)}")

    # Проверяем, что все ссылки отображаются на странице
    for link in links:
        assert link.is_displayed(), "Ссылка не отображается"

    # Проверяем, что текст первой ссылки содержит "1"
    assert "1" in links[0].text, (
         f"Текст должен содержать '1', получено: '{links[0].text}'")

    driver.quit()
