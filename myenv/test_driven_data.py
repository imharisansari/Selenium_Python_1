from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import csv
import time
import pandas as pd


@pytest.mark.parametrize("username, password", pd.read_csv("E:\\CG Exit\\Learning\\Coding\\Selenium_Python\\myenv\\test_driven_data1.csv").values)
def test_login(username, password):
    # Set up WebDriver (e.g., Chrome)
    driver = webdriver.Chrome()
    
    time.sleep(1)               #It will run the code with 1s delay

    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(3)

    username_locator = driver.find_element(By.NAME, "username")
    username_locator.send_keys(username)
    time.sleep(2)

    #Type password Password123 into Password field
    password_locator = driver.find_element(By.ID, "password")
    #password_locator = driver.find_element(By.NAME, "password")
    password_locator.send_keys(password)
    time.sleep(2)

    #Push Submit button
    submit_button_locator = driver.find_element(By.ID, "submit")
    submit_button_locator.click()
    time.sleep(2)

    #Verify new page URL contains practicetestautomation.com/logged-in-successfully/
    actual_url = driver.current_url
    assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"
    time.sleep(2)

    driver.quit()
    
