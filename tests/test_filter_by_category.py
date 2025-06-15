import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@allure.feature("Filter")
@allure.story("Фильтр по категории (Category)")
def test_filter_by_category(driver):
    url = "https://makarovartem.github.io/frontend-avito-tech-test-assignment"
    driver.get(url)
    wait = WebDriverWait(driver, 10)

    with allure.step("Находим фильтр категории и проверяем дефолтное значение"):
        filter_category = driver.find_elements(By.CSS_SELECTOR, "div.ant-select")[1]
        dropdown = filter_category.find_element(By.CSS_SELECTOR, ".ant-select-selection-item")
        assert dropdown.text.lower() == "not chosen", f"Фильтр не в дефолтном состоянии: {dropdown.text}"

    with allure.step("Выбираем категорию 'shooter'"):
        dropdown.click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".ant-select-dropdown")))
        category_option = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(@class,'ant-select-item-option-content') and text()='shooter']")
            )
        )
        category_option.click()
        time.sleep(1)
        cards = driver.find_elements(By.CSS_SELECTOR, "ul.ant-list-items > li")
        assert len(cards) > 0, "Нет карточек для категории 'shooter'"

    with allure.step("Сбрасываем фильтр обратно на 'not chosen' и проверяем баг"):
        dropdown = filter_category.find_element(By.CSS_SELECTOR, ".ant-select-selection-item")
        dropdown.click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".ant-select-dropdown")))
        not_chosen_option = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(@class,'ant-select-item-option-content') and text()='not chosen']")
            )
        )
        not_chosen_option.click()
        time.sleep(1)
        try:
            cards_all = driver.find_elements(By.CSS_SELECTOR, "ul.ant-list-items > li")
            assert len(cards_all) > 0, "Нет карточек после сброса фильтра на 'not chosen'"
        except Exception as e:
            allure.attach(driver.page_source, name="page_source", attachment_type=allure.attachment_type.HTML)
            raise AssertionError(f"Ошибка при возврате фильтра Category в 'not chosen': {e}")