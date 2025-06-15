import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import config

@allure.feature("Game Card")
@allure.story("Открытие первой, второй и последней карточки с главной страницы")
def test_open_various_game_cards(driver: webdriver.Chrome, test_config: config.Config) -> None:
    url = test_config.srv.URL
    driver.get(url)
    parent_selector = test_config.cards.PARENT_SELECTOR
    child_selector = test_config.cards.CHILD_SELECTOR
    wait = WebDriverWait(driver, 10)

    with allure.step("Получаем список карточек на главной странице"):
        cards = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, parent_selector))
        )
        assert len(cards) >= 2, "На странице должно быть как минимум две карточки"

    with allure.step("Переходим в первую карточку и проверяем отображение заголовка"):
        cards[0].click()
        header = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, child_selector))
        )
        assert header.is_displayed()
        driver.back()

    with allure.step("Переходим во вторую карточку и проверяем отображение заголовка"):
        cards = driver.find_elements(By.CSS_SELECTOR, parent_selector)
        cards[1].click()
        header = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, child_selector))
        )
        assert header.is_displayed()
        driver.back()

    with allure.step("Переходим в последнюю карточку и проверяем отображение заголовка"):
        cards = driver.find_elements(By.CSS_SELECTOR, parent_selector)
        cards[-1].click()
        header = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, child_selector))
        )
        assert header.is_displayed()