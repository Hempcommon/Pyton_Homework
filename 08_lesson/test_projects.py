import pytest
import requests
from yougile_api import YougileProjectApi


@pytest.fixture(scope="module")
def api():
    """Инициализируем клиент API один раз для всех тестов"""
    return YougileProjectApi()


@pytest.fixture
def create_and_clean_project(api):
    """Фикстура: создает проект для теста и удаляет его после завершения"""
    title = "Autotest Project"
    resp = api.create_project(title)
    assert resp.status_code == 201, f"Ошибка создания: {resp.text}"
    project_id = resp.json()["id"]

    yield project_id  # Возвращаем ID в тест

    # очистка данных после теста
    api.delete_project(project_id)


# ================= ПОЗИТИВНЫЕ ТЕСТЫ =================

def test_create_positive(api):
    """Позитивный: создание проекта"""
    title = "Positive Create Test"
    resp = api.create_project(title)

    # 1. Проверяем статус создания
    assert resp.status_code == 201

    # 2. Получаем ID из ответа
    body = resp.json()
    assert "id" in body
    project_id = body["id"]

    # 3.Делаем GET-запрос,чтобы убедиться, что проект создался с нужным именем
    get_resp = api.get_project(project_id)
    assert get_resp.status_code == 200
    assert get_resp.json()["title"] == title

    # Чистим за собой
    api.delete_project(project_id)


def test_get_positive(api, create_and_clean_project):
    """Позитивный: получение существующего проекта"""
    project_id = create_and_clean_project
    resp = api.get_project(project_id)

    assert resp.status_code == 200
    assert resp.json()["id"] == project_id


def test_update_positive(api, create_and_clean_project):
    """Позитивный: обновление названия проекта"""
    project_id = create_and_clean_project
    new_title = "Updated Title"

    # 1. Отправляем PUT-запрос на обновление
    resp = api.update_project(project_id, new_title)
    assert resp.status_code == 200

    # 2. Проверяем через GET, что название действительно обновилось в базе
    get_resp = api.get_project(project_id)
    assert get_resp.status_code == 200
    assert get_resp.json()["title"] == new_title


# ================= НЕГАТИВНЫЕ ТЕСТЫ =================

def test_create_negative(api):
    """Негативный: создание с неверным типом данных для title"""
    # Отправляем число вместо строки.
    resp = requests.post(
        f"{api.base_url}/projects",
        json={"title": 12345},
        headers=api.headers
    )
    assert resp.status_code in [400, 422]


def test_get_negative(api):
    """Негативный: получение несуществующего проекта"""
    # Генерируем неверный UUID
    fake_id = "00000000-0000-0000-0000-000000000000"
    resp = api.get_project(fake_id)

    # Ожидаем 404 Not Found
    assert resp.status_code == 404


def test_update_negative(api):
    """Негативный: обновление несуществующего проекта"""
    fake_id = "00000000-0000-0000-0000-000000000000"
    resp = requests.put(
        f"{api.base_url}/projects/{fake_id}",
        json={"title": "New Title"},
        headers=api.headers
    )
    # Ожидаем 404, так как проекта с таким ID не существует
    assert resp.status_code == 404
