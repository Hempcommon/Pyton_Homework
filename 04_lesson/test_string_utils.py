import pytest
from string_utils import StringUtils


class TestStringUtils:
    """Тесты для класса StringUtils"""

    def setup_method(self):
        """Инициализация объекта перед каждым тестом"""
        self.utils = StringUtils()

    # ТЕСТЫ ДЛЯ МЕТОДА capitalize

    @pytest.mark.parametrize("input_str, expected", [
        ("skypro", "Skypro"),        # обычное слово
        ("hello world", "Hello world"),  # фраза
        ("123abc", "123abc"),        # начинается с цифры
        ("", ""),                    # пустая строка
        (" ", " "),                  # пробел
        ("a", "A"),                  # одна буква
        ("python", "Python"),        # слово с маленькой буквы
        ("04 апреля", "04 апреля"),  # цифры и буквы
    ])
    def test_capitalize_positive(self, input_str, expected):
        """Позитивные тесты: capitalize корректно преобразует строки"""
        assert self.utils.capitalize(input_str) == expected

    @pytest.mark.parametrize("input_str", [
        None,    # передали None вместо строки
        123,     # передали число
        [],      # передали список
        {},      # передали словарь
    ])
    def test_capitalize_negative(self, input_str):
        """Негативные тесты: capitalize с некорректными типами данных"""
        with pytest.raises(AttributeError):
            self.utils.capitalize(input_str)

    # ТЕСТЫ ДЛЯ МЕТОДА trim

    @pytest.mark.parametrize("input_str, expected", [
        ("   skypro", "skypro"),         # пробелы в начале
        ("  hello  world  ", "hello  world  "),  # пробелы в начале и конце
        ("   ", ""),                     # только пробелы
        ("", ""),                        # пустая строка
        ("no_spaces", "no_spaces"),      # без пробелов
        ("   123   ", "123   "),         # цифры с пробелами
        ("   Python", "Python"),         # слово с пробелами
    ])
    def test_trim_positive(self, input_str, expected):
        """Позитивные тесты: trim убирает пробелы в начале строки"""
        assert self.utils.trim(input_str) == expected

    @pytest.mark.parametrize("input_str", [
        None,    # передали None
        123,     # передали число
        [],      # передали список
    ])
    def test_trim_negative(self, input_str):
        """Негативные тесты: trim с некорректными типами данных"""
        with pytest.raises(AttributeError):
            self.utils.trim(input_str)

    # ТЕСТЫ ДЛЯ МЕТОДА containsflake8 04_lesson

    @pytest.mark.parametrize("input_str, symbol, expected", [
        ("SkyPro", "S", True),      # символ есть
        ("SkyPro", "U", False),     # символа нет
        ("Hello", "e", True),       # символ есть
        ("12345", "3", True),       # цифра есть
        ("", "", False),            # пустая строка и пустой символ
        ("abc", "", False),         # строка и пустой символ
        (" ", " ", True),           # пробел есть
        ("Python", "Py", True),     # подстрока есть
        ("Hello", "z", False),      # символа нет
    ])
    def test_contains_positive(self, input_str, symbol, expected):
        """Позитивные тесты: contains корректно проверяет наличие символа"""
        assert self.utils.contains(input_str, symbol) == expected

    @pytest.mark.parametrize("input_str, symbol", [
        (None, "a"),      # первая строка - None
        ("abc", None),    # второй параметр - None
        (123, "a"),       # первая строка - число
        ("abc", 123),     # второй параметр - число
    ])
    def test_contains_negative(self, input_str, symbol):
        """Негативные тесты: contains с некорректными типами данных"""
        with pytest.raises((AttributeError, TypeError)):
            self.utils.contains(input_str, symbol)

    # ТЕСТЫ ДЛЯ МЕТОДА delete_symbol

    @pytest.mark.parametrize("input_str, symbol, expected", [
        ("SkyPro", "k", "SyPro"),           # удаляем букву
        ("Hello World", "o", "Hell Wrld"),  # удаляем букву
        ("aaa", "a", ""),                   # удаляем все буквы
        ("", "a", ""),                      # пустая строка
        ("abc", "", "abc"),                 # удаляем пустой символ
        ("a b c", " ", "abc"),              # удаляем пробелы
        ("SkyPro", "Pro", "Sky"),           # удаляем подстроку
        ("Test Test", "Test", " "),         # удаляем слово
        ("12345", "3", "1245"),             # удаляем цифру
        ("aabbcc", "ab", "abcc"),           # удаляем часть
    ])
    def test_delete_symbol_positive(self, input_str, symbol, expected):
        """Позитивные тесты: delete_symbol корректно удаляет символы"""
        assert self.utils.delete_symbol(input_str, symbol) == expected

    @pytest.mark.parametrize("input_str, symbol", [
        (None, "a"),      # первая строка - None
        ("abc", None),    # второй параметр - None
        (123, "a"),       # первая строка - число
        ("abc", 123),     # второй параметр - число
    ])
    def test_delete_symbol_negative(self, input_str, symbol):
        """Негативные тесты: delete_symbol с некорректными типами данных"""
        with pytest.raises((AttributeError, TypeError)):
            self.utils.delete_symbol(input_str, symbol)
