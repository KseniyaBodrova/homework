from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

option = Options()
option.add_argument('--window-size=700,1080')
option.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=option)
# driver.maximize_window()
# driver.set_window_size(500, 1080)
driver.get('https://google.com/')
search_input = driver.find_element(By.NAME,'q')
search_input.send_keys('кошка или собака')
search_input.submit()
print(driver.title)
def test_title():
    assert driver.find_element(By.XPATH, "//*[contains(text(), 'Об этой странице')]")
    print('Assert -  ок')
test_title()
# driver.close()