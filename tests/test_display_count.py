import pytest
import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Display Count")
@allure.story("Проверка отображения разного количества карточек на странице")
@pytest.mark.parametrize("count", [10, 20, 50, 100])
def test_display_count(driver, count):
    url = "https://makarovartem.github.io/frontend-avito-tech-test-assignment"
    driver.get(url)
    wait = WebDriverWait(driver, 10)

    with allure.step("Считаем карточки на первой странице (дефолтное количество)"):
        cards_before = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.ant-list-items > li"))
        )
        default_count = len(cards_before)

    with allure.step("Открываем dropdown выбора количества карточек"):
        dropdown = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "li.ant-pagination-options span.ant-select-selection-item"))
        )
        dropdown.click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".ant-select-dropdown")))
        time.sleep(0.3)

    with allure.step(f"Выбираем вариант {count} / page"):
        option_text = f"{count} / page"
        options = driver.find_elements(By.XPATH, "//div[@role='option']")
        for opt in options:
            if option_text in opt.text:
                opt.click()
                break

    with allure.step("Дожидаемся изменения числа карточек на странице"):
        wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "ul.ant-list-items > li")) != default_count or count == 10)

    with allure.step("Проверяем итоговое количество карточек"):
        cards_after = driver.find_elements(By.CSS_SELECTOR, "ul.ant-list-items > li")
        assert len(cards_after) <= count, (
            f"Ожидалось не больше {count} карточек, найдено {len(cards_after)}"
        )