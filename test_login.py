import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

@pytest.fixture(scope="function")
def driver():
    service = EdgeService(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_to_qiye_mail(driver):
    driver.get("https://mailh.qiye.163.com/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "account_name")))
    driver.find_element(By.ID, "account_name").send_keys("M202320805@xs.ustb.edu.cn")
    driver.find_element(By.ID, "password").send_keys("USTB07173421!")
    driver.find_element(By.ID, "submit-btn").click()
    sleep(10)
    assert "邮件" in driver.page_source or "mail" in driver.current_url.lower()
