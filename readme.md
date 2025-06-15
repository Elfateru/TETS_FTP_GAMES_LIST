TEST FtP Games list

Описание

Автоматизированные тесты для проверки пользовательских сценариев платформы Free-to-Play Games (https://makarovartem.github.io/frontend-avito-tech-test-assignment):

- Открытие карточки игры
- Отображение разного количества карточек на странице поиска
- Переход по страницам результата поиска с помощью пагинации
- Фильтрация по платформе и категории
- Сортировка карточек
- Проверка обработки багов при сбросе фильтра

Тесты написаны на Python с использованием pytest, selenium, allure-pytest, webdriver-manager.
Все сценарии покрыты Allure-отчётами и снабжены скриншотами в случае падения.



Установка

1. Клонируйте репозиторий

   git clone !!!!!!!!!!!НЕ ЗАБУДЬ ПРИЛОЖИТЬ ССЫЛКУ!!!!!!
   cd TEST_FtP_Games_list


2. Создайте и активируйте виртуальное окружение (опционально)

   python -m venv .venv
   Windows:
   .venv\Scripts\activate
   Linux/Mac:
   source .venv/bin/activate

3. Установите зависимости

   pip install -r requirements.txt


4. Проверьте, что установлен Google Chrome (браузер)

   - Драйвер скачивается автоматически через webdriver-manager.


Запуск тестов

1. Запуск всех тестов

   pytest --alluredir=allure-results


2. Просмотр Allure-отчёта

     allure serve allure-results
   - Если Allure не найден, убедитесь, что он добавлен в PATH и установлен Java (JRE/JDK).

Структура проекта

- tests/ — автотесты, сгруппированные по типам сценариев.
- conftest.py — фикстуры для запуска Selenium, снятия скриншотов при ошибке и т.д.
- requirements.txt — необходимые библиотеки для запуска тестов.
- TESTCASES.md — сценарии для автоматизации.
- BUGS.md — баг-репорты, найденные при тестировании.
- README.md — вы читаете его.
- .gitignore — игнорирует служебные файлы и окружения.


Примеры команд

- Запуск всех тестов:
  pytest --alluredir=allure-results

- Запуск одного теста:
  pytest tests/test_cards.py --alluredir=allure-results


- Повторный запуск упавших тестов:
  pytest --last-failed --alluredir=allure-results

- Просмотр Allure-отчёта

  allure serve allure-results

Примечания
- Скриншоты и page source автоматически прикладываются к отчёту при падении тестов.
- Для полноценного просмотра Allure-отчётов необходима Java и установленный Allure CLI.
- Все тесты должны быть “зелёными” (кроме сценариев, где подтверждается известный баг).
- Если что-то не запускается — убедитесь, что установлены Python 3.8+, Chrome, Allure, Java.


