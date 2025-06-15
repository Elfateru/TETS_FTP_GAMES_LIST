import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@allure.feature("Pagination")
@allure.story("Переход по страницам результата поиска с помощью пагинации")
def test_pagination_navigation(driver):
    url = "https://makarovartem.github.io/frontend-avito-tech-test-assignment"
    driver.get(url)
    wait = WebDriverWait(driver, 10)

    with allure.step("Ждём появления карточек на первой странице"):
        cards_first = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.ant-list-items > li"))
        )
        cards_texts_first = [c.text for c in cards_first]

    with allure.step("Кликаем на последнюю страницу в пагинации"):
        page_buttons = driver.find_elements(By.CSS_SELECTOR, "li.ant-pagination-item")
        last_page_btn = page_buttons[-1]
        last_page_number = last_page_btn.text
        last_page_btn.click()
        time.sleep(1)

    with allure.step("Проверяем, что открыта последняя страница и карточки изменились"):
        active_page = driver.find_element(By.CSS_SELECTOR, "li.ant-pagination-item-active")
        assert active_page.text == last_page_number, "Активная страница — не последняя!"
        cards_last = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.ant-list-items > li"))
        )
        cards_texts_last = [c.text for c in cards_last]
        assert cards_texts_first != cards_texts_last, "Карточки на последней и первой странице совпадают!"

    with allure.step("Переходим обратно на первую страницу"):
        first_page_btn = driver.find_element(By.CSS_SELECTOR, "li.ant-pagination-item:nth-child(1)")
        first_page_btn.click()
        time.sleep(1)

    with allure.step("Проверяем, что вернулись на первую страницу"):
        active_page = driver.find_element(By.CSS_SELECTOR, "li.ant-pagination-item-active")
        assert active_page.text == "1", "Активная страница — не первая!"
        cards_first_back = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.ant-list-items > li"))
        )
        cards_texts_first_back = [c.text for c in cards_first_back]
        assert cards_texts_first_back == cards_texts_first, "Карточки на первой странице не совпадают после возврата!"


@allure.feature("Pagination")
@allure.story("Переход между страницами с помощью кнопок Next и Previous")
def test_pagination_next_previous(driver):
    url = "https://makarovartem.github.io/frontend-avito-tech-test-assignment"
    driver.get(url)
    wait = WebDriverWait(driver, 10)

    with allure.step("Ждём появления карточек на первой странице"):
        cards_first = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.ant-list-items > li"))
        )
        cards_texts_first = [c.text for c in cards_first]

    with allure.step("Нажимаем на кнопку Next Page"):
        next_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "li.ant-pagination-next"))
        )
        next_button.click()
        time.sleep(1)

    with allure.step("Проверяем, что активна страница 2 и карточки изменились"):
        active_page = driver.find_element(By.CSS_SELECTOR, "li.ant-pagination-item-active")
        assert active_page.text == "2", f"Ожидалась страница 2, а отображается {active_page.text}"
        cards_second = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.ant-list-items > li"))
        )
        cards_texts_second = [c.text for c in cards_second]
        assert cards_texts_first != cards_texts_second, "Карточки не изменились при переходе на вторую страницу!"

    with allure.step("Нажимаем на кнопку Previous Page"):
        prev_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "li.ant-pagination-prev"))
        )
        prev_button.click()
        time.sleep(1)

    with allure.step("Проверяем, что снова активна страница 1 и карточки совпадают с первой страницей"):
        active_page = driver.find_element(By.CSS_SELECTOR, "li.ant-pagination-item-active")
        assert active_page.text == "1", f"Ожидалась страница 1, а отображается {active_page.text}"
        cards_first_back = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.ant-list-items > li"))
        )
        cards_texts_first_back = [c.text for c in cards_first_back]
        assert cards_texts_first == cards_texts_first_back, "Карточки на первой странице не совпадают после возврата!"
