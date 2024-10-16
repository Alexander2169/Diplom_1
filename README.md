## Дипломный проект. Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Процент покрытия 100% (отчет: `htmlcov/index.html`)

### Структура проекта

- `praktikum` - пакет, содержащий классы 'Bun', 'Burgers', 'Database', 'Ingridient';
- `tests` - пакет, содержащий тесты, разделенные по классам:
            `test_bun.py` - тестирование класса Bun;
            `test_burger.py` - тестирование класса Burger;
            `test_database.py` - тестирование класса Database;
            `test_ingridient.py` - тестирование класса Ingridient;
- `gitignore` - файл, содержащий локальные файлы;
- `ingridient_types.py` - файл, содержащий перечесление типров ингридиентов;
- `praktikum.py` - корневой файл - точка входа в приложение;
- `README.md` - файл, содержащий текстовую часть о проделанной работе;
- `requirements.txt` - файл, содержащий список внешних зависимостей.

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**

>  `$ pytest --cov=praktikum --cov-report=html`
