import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from typing import Generator
import config


# @pytest.fixture
@pytest.fixture(scope="session", autouse=True)
def driver() -> Generator[webdriver.Chrome, None, None]:
    """Фикстура для инициализации и закрытия WebDriver Chrome."""
    options = Options()
    options.add_argument("--headless") #Запуск браузера без GUI
    options.add_argument("--no-sandbox")  #Отключение песочницы CI и Docker
    options.add_argument("--disable-dev-shm-usage") #Отключение общей памяти для CI
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope="session", autouse=True)
def test_config() -> config.Config:
    return config.get()

# Хук для добавления скриншота в Allure при падении любого теста
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call) -> None:
    """Хук для снятия скриншота при падении любого теста."""
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )