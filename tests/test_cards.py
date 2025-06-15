import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Game Card")
@allure.story("Открытие первой, второй и последней карточки с главной страницы")
def test_open_various_game_cards(driver):
    url = "https://makarovartem.github.io/frontend-avito-tech-test-assignment"
    driver.get(url)
    wait = WebDriverWait(driver, 10)

    with allure.step("Получаем список карточек на главной странице"):
        cards = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.ant-list-items > li"))
        )
        assert len(cards) >= 2, "На странице должно быть как минимум две карточки"

    with allure.step("Переходим в первую карточку и проверяем отображение заголовка"):
        cards[0].click()
        header = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h2.ant-typography"))
        )
        assert header.is_displayed()
        driver.back()

    with allure.step("Переходим во вторую карточку и проверяем отображение заголовка"):
        cards = driver.find_elements(By.CSS_SELECTOR, "ul.ant-list-items > li")
        cards[1].click()
        header = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h2.ant-typography"))
        )
        assert header.is_displayed()
        driver.back()

    with allure.step("Переходим в последнюю карточку и проверяем отображение заголовка"):
        cards = driver.find_elements(By.CSS_SELECTOR, "ul.ant-list-items > li")
        cards[-1].click()
        header = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h2.ant-typography"))
        )
        assert header.is_displayed()