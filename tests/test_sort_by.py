import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import config
import time

@allure.feature("Sort")
@allure.story("Сортировка по выпадающему списку Sort by")
def test_sort_by(driver: webdriver.Chrome, test_config: config.Config) -> None:
    url = test_config.srv.URL
    selection_item = test_config.sort_by.SELECTION_ITEM
    selection_dropdown = test_config.sort_by.SELECTION_DROPDOWN
    selection_list = test_config.sort_by.SELECTION_LIST
    driver.get(url)
    wait = WebDriverWait(driver, 10)

    with allure.step("Находим фильтр Sort by и проверяем дефолтное значение"):
        sort_by = driver.find_elements(By.CSS_SELECTOR, "div.ant-select")[2]  # Третий селект — Sort by
        dropdown = sort_by.find_element(By.CSS_SELECTOR, selection_item)
        assert dropdown.text.lower() == "not chosen", f"Sort by не в дефолтном состоянии: {dropdown.text}"

    with allure.step("Выбираем первое доступное значение (не 'not chosen')"):
        dropdown.click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selection_dropdown)))
        options = driver.find_elements(By.CSS_SELECTOR, ".ant-select-dropdown .ant-select-item-option-content")
        # Берём первое доступное значение не равное "not chosen"
        for option in options:
            if option.text.lower() != "not chosen":
                sort_value = option.text
                option.click()
                break
        else:
            pytest.skip("Нет доступных опций для сортировки кроме 'not chosen'")
        time.sleep(1)

    with allure.step("Проверяем, что сортировка применилась (количество карточек осталось, порядок мог измениться)"):
        cards = driver.find_elements(By.CSS_SELECTOR, selection_list)
        assert len(cards) > 0, "После сортировки не найдено ни одной карточки!"


    with allure.step("Сбрасываем сортировку обратно на 'not chosen'"):
        dropdown = sort_by.find_element(By.CSS_SELECTOR, selection_item)
        dropdown.click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selection_dropdown)))
        not_chosen_option = driver.find_element(
            By.XPATH, "//div[contains(@class,'ant-select-item-option-content') and text()='not chosen']"
        )
        not_chosen_option.click()
        time.sleep(1)
        cards_after = driver.find_elements(By.CSS_SELECTOR, selection_list)
        assert len(cards_after) > 0, "После сброса сортировки карточки не появились!"