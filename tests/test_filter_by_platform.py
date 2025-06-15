import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import config
import time


@allure.feature("Filter")
@allure.story("Фильтр по платформе (Platform)")
def test_filter_by_platform(driver: webdriver.Chrome, test_config: config.Config) -> None:
    url = test_config.srv.URL
    selection_list = test_config.filter_by_platform.SELECTION_LIST
    selection_item = test_config.filter_by_platform.SELECTION_ITEM
    selection_dropdown = test_config.filter_by_platform.SELECTION_DROPDOWN
    driver.get(url)
    wait = WebDriverWait(driver, 10)

    with allure.step("Находим фильтр платформы и проверяем дефолтное значение"):
        # Первый .ant-select — это фильтр по платформе
        filter_platform = driver.find_elements(By.CSS_SELECTOR, "div.ant-select")[0]
        dropdown = filter_platform.find_element(By.CSS_SELECTOR, selection_item)
        assert dropdown.text.lower() == "not chosen", f"Фильтр не в дефолтном состоянии: {dropdown.text}"

    with allure.step("Выбираем 'PC'"):
        dropdown.click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selection_dropdown)))
        # Находим опцию "PC" среди видимых элементов дропдауна
        pc_option = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(@class,'ant-select-dropdown')]//div[contains(@class,'ant-select-item-option-content') and text()='PC']")
            )
        )
        pc_option.click()
        time.sleep(1)
        cards_pc = driver.find_elements(By.CSS_SELECTOR, selection_list)
        assert len(cards_pc) > 0, "Нет карточек для платформы 'PC'"

    with allure.step("Сбрасываем фильтр обратно на 'not chosen' и проверяем баг"):
        dropdown = filter_platform.find_element(By.CSS_SELECTOR, selection_item)
        dropdown.click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selection_dropdown)))
        not_chosen_option = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(@class,'ant-select-dropdown')]//div[contains(@class,'ant-select-item-option-content') and text()='not chosen']")
            )
        )
        not_chosen_option.click()
        time.sleep(1)
        try:
            cards_all = driver.find_elements(By.CSS_SELECTOR, selection_list)
            assert len(cards_all) > 0, "Нет карточек после сброса фильтра на 'not chosen'"
        except Exception as e:
            # Allure attachment: page source при падении
            allure.attach(driver.page_source, name="page_source", attachment_type=allure.attachment_type.HTML)
            raise AssertionError(f"Ошибка при возврате фильтра Platform в 'not chosen': {e}")