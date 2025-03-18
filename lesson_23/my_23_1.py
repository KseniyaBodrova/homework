import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.set_window_size(700, 1020)
    return chrome_driver


def test_id_name(driver):
    input_data = 'name'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.NAME, 'text_string')
    text_string.send_keys(input_data)
    len_text_string = text_string.get_attribute('value')
    for _ in range(len(len_text_string)):
        text_string.send_keys(Keys.BACKSPACE)
    text_string.clear()