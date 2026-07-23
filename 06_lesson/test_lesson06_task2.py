from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    user1_cookies = [
        {
            "name": "SESSION",
            "value": "OTFmYWVhYjYtNmI2NC00MTJkLWI4NjItZTE5NDA5MTA3NjE5",
            "domain": ".gitflic.ru",
        }
    ]

    user2_cookies = [
        {
            "name": "SESSION",
            "value": "NjU2Y2IyZDItN2ZhYi00YzNiLWE2NjItNTFmOTkwYjA3M2U3",
            "domain": ".gitflic.ru",
        }
    ]

    user1_profile_url = "https://gitflic.ru/user/devtools"
    user2_profile_url = "https://gitflic.ru/user/poops"

    try:
        # 1. Откройте страницу https://gitflic.ru/
        driver.get("https://gitflic.ru/")

        # 2. Установите cookie пользователя 1
        for cookie in user1_cookies:
            driver.add_cookie(cookie)

        # 3. Обновите страницу
        driver.refresh()

        # 4. Перейдите на страницу пользователя 1
        driver.get(user1_profile_url)

        # Явное ожидание загрузки элемента профиля (для надежности)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # 5. Сохраните текущий URL
        url_user1 = driver.current_url

        # 6. Разлогиньтесь (очистите куки)
        driver.delete_all_cookies()

        # 7. Установите cookie пользователя 2
        # Снова переходим на домен
        driver.get("https://gitflic.ru/")
        for cookie in user2_cookies:
            driver.add_cookie(cookie)

        # 8. Обновите страницу
        driver.refresh()

        # 9. Перейдите на страницу пользователя 2
        driver.get(user2_profile_url)

        # Явное ожидание загрузки элемента профиля
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # 10. Сохраните текущий URL
        url_user2 = driver.current_url

        # 11. Проверьте, URL для пользователя 1 и пользователя 2 различаются
        assert url_user1 != url_user2, (
         f"URL должны различаться. "
         f"Пользователь 1: {url_user1}, "
         f"Пользователь 2: {url_user2}"
        )
    finally:
        driver.quit()
