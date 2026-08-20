import os
import requests
from dotenv import load_dotenv


# Загружаем переменные из .env файла
load_dotenv()


class YougileProjectApi:
    def __init__(self):
        # Базовый URL API Yougile
        self.base_url = "https://ru.yougile.com/api-v2"

        # Токен берем из переменной окружения (из .env)
        self.token = os.environ.get("YOUGILE_TOKEN")
        if not self.token:
            raise ValueError("Переменная YOUGILE_TOKEN не задана в .env!")

        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

    def create_project(self, title: str):
        """POST /api-v2/projects"""
        url = f"{self.base_url}/projects"
        return requests.post(url, json={"title": title}, headers=self.headers)

    def get_project(self, project_id: str):
        """GET /api-v2/projects/{id}"""
        url = f"{self.base_url}/projects/{project_id}"
        return requests.get(url, headers=self.headers)

    def update_project(self, project_id: str, title: str):
        """PUT /api-v2/projects/{id}"""
        url = f"{self.base_url}/projects/{project_id}"
        return requests.put(url, json={"title": title}, headers=self.headers)

    def delete_project(self, project_id: str):
        """Вспомогательный метод для очистки данных после тестов"""
        url = f"{self.base_url}/projects/{project_id}"
        return requests.delete(url, headers=self.headers)
