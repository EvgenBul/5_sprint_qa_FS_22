# Sprint_5 - Тестирование Stellar Burgers

Этот проект содержит автоматизированные тесты для веб-приложения Stellar Burgers.

## Структура проекта

- `helpers/` - Вспомогательные функции (генераторы данных)
- `locators/` - Локаторы для элементов страниц
- `test_data/` - Тестовые данные
- `tests/` - Автоматизированные тесты
  - `conftest.py` - Фикстуры pytest
  - `test_login_and_registration.py` - Тесты авторизации и регистрации
  - `test_constructor_and_navigation.py` - Тесты навигации и конструктора

## Установка

1. Установите Python 3.9+
2. Установите зависимости:pip install -r requirements.txt
3. Установите браузеры (Chrome и Firefox) и драйверы для них

## Запуск тестов

Для запуска всех тестов: pytest tests/
Для запуска конкретного файла:pytest tests/test_login_and_registration.py
Для запуска с определенным браузером (через фикстуру): pytest --driver Chrome tests/

## Требования

- Selenium WebDriver
- ChromeDriver/GeckoDriver
- Браузеры Chrome и Firefox

