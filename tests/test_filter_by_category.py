import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import config
import time


@allure.feature("Filter")
@allure.story("Фильтр по категории (Category)")
def test_filter_by_category(driver: webdriver.Chrome, test_config: config.Config) -> None:
    url = test_config.srv.URL
    driver.get(url)
    selection_item = test_config.filter_by_category.SELECTION_ITEM
    selection_dropdown = test_config.filter_by_category.SELECTION_DROPDOWN
    selection_list = test_config.filter_by_category.SELECTION_LIST
    wait = WebDriverWait(driver, 10)

    with allure.step("Находим фильтр категории и проверяем дефолтное значение"):
        filter_category = driver.find_elements(By.CSS_SELECTOR, "div.ant-select")[1]
        dropdown = filter_category.find_element(By.CSS_SELECTOR, selection_item)
        assert dropdown.text.lower() == "not chosen", f"Фильтр не в дефолтном состоянии: {dropdown.text}"

    with allure.step("Выбираем категорию 'shooter'"):
        dropdown.click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selection_dropdown)))
        category_option = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(@class,'ant-select-item-option-content') and text()='shooter']")
            )
        )
        category_option.click()
        time.sleep(1)
        cards = driver.find_elements(By.CSS_SELECTOR, selection_list)
        assert len(cards) > 0, "Нет карточек для категории 'shooter'"

    with allure.step("Сбрасываем фильтр обратно на 'not chosen' и проверяем баг"):
        dropdown = filter_category.find_element(By.CSS_SELECTOR, selection_item)
        dropdown.click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selection_dropdown)))
        not_chosen_option = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(@class,'ant-select-item-option-content') and text()='not chosen']")
            )
        )
        not_chosen_option.click()
        time.sleep(1)
        try:
            cards_all = driver.find_elements(By.CSS_SELECTOR, selection_list)
            assert len(cards_all) > 0, "Нет карточек после сброса фильтра на 'not chosen'"
        except Exception as e:
            allure.attach(driver.page_source, name="page_source", attachment_type=allure.attachment_type.HTML)
            raise AssertionError(f"Ошибка при возврате фильтра Category в 'not chosen': {e}")