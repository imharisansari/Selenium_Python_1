from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
import pytest
import time


def test_flight():

    # Set up WebDriver (e.g., Chrome)
    driver = webdriver.Edge()

    #maximising the current window
    driver.maximize_window()
    
    time.sleep(1)               #It will run the code with 1s delay

    #going the URL
    driver.get("https://www.cleartrip.com/flights")
    time.sleep(1)

    #closing sign in popup
    cross_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/div[1]/div[2]")
    cross_button.click()
    time.sleep(1)

    #choosing the passanger dropdown
    passanger_choose = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/div[2]/div[1]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/div/div/div[1]/div/div")
    passanger_choose.click()
    time.sleep(5)

    #choosing no of adult passanger
    passanger_choose_adult = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/div[2]/div[1]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/div/div/div[2]/div/div[1]/div/div/div/div[2]/button[2]")
    passanger_choose_adult.click()
    time.sleep(5)   

    #choosing no of child passanger
    passanger_choose_child = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/div[2]/div[1]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[2]/button[2]")
    passanger_choose_child.click()
    time.sleep(5)

    #choosing depatrure location
    departure = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/div[2]/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/div/div[1]/input")
    departure.click()
    departure.send_keys("Luc")
    time.sleep(6)

    #choosing depatrure city
    departure_cities = driver.find_elements(By.XPATH, "/html/body/div[1]/div/main/div/div/div[2]/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[2]/ul[1]/li/div/div[2]")
    for city_d in departure_cities:
        if "LKO" in city_d.text:
            city_d.click()
            break
    time.sleep(3)

    #choosing arrival location
    arrival = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/div[2]/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/div/div[3]/input")
    arrival.click()
    arrival.send_keys("New")
    time.sleep(6)

    #choosing arrival city
    arrival_cities = driver.find_elements(By.XPATH, "/html/body/div[1]/div/main/div/div/div[2]/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/div/div[3]/div[2]/ul[1]/li/div/div[2]/p")
    for city_a in arrival_cities:
        if "DEL" in city_a.text:
            city_a.click()
            break
    time.sleep(3)

    #choosing depatrure date dropdown
    departure_date = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/div[2]/div[1]/div[1]/div/div[1]/div[2]/div/div[4]/div/div/div/div[1]/div[2]")
    departure_date.click()
    time.sleep(1)

    #choosing depatrure date
    departure_date_select = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/div[2]/div[1]/div[1]/div/div[1]/div[2]/div/div[4]/div/div/div/div[4]/div[3]/div/div[2]/div[1]/div[3]/div[5]/div[4]/div/div")
    departure_date_select.click()
    time.sleep(5)

    #choosing arrival date dropdown
    arrival_date = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[1]/div[2]/div[1]/div[1]/div/div[1]/div[2]/div/div[4]/div/div/div/div[3]")
    arrival_date.click()
    time.sleep(2)

    #choosing arrival date 
    arrival_date_select = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/div[2]/div[1]/div[1]/div/div[1]/div[2]/div/div[4]/div/div/div/div[4]/div[3]/div/div[2]/div[2]/div[3]/div[4]/div[5]/div/div")
    time.sleep(3)
    arrival_date_select.click()
    time.sleep(1)

    #clicking the search flight button
    #explicit wait
    search_flight = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/div[2]/div[1]/div[1]/div/div[1]/div[2]/div/div[7]/button/div/h4")
    search_flight.click()
    time.sleep(3)

    #waiting and clicking of non-stop checkbox
    wait = WebDriverWait(driver, 20)
    check_box = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/main/div/div/div[1]/div/aside/div[2]/div[2]/div[2]/div/label[1]/div[2]/div/p")))
    check_box.click()
    time.sleep(3)

    #clicking on book button
    book = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/div[2]/div[2]/div[4]/div[1]/div[2]/div[2]/button/span")
    book.click()
    time.sleep(3)

    #Swithing to new tab after clicking book button
    child_window = driver.window_handles[1]
    driver.switch_to.window(child_window)
    time.sleep(10)

    #closinhg the driver
    driver.quit()

    # python -m pytest myenv\test_ticket_book.py



















    # Email_icon = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/div/section/div[2]/img")
    # Email_icon.click()
    # time.sleep(2) 

    # #Type username student into Username field
    # Email_label = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/div/section/form/div[1]/label")
    # # print(Email_label)
    # time.sleep(2)
    # email_holder_locator = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/div/section/form/div[1]/div/input")
    # #username_locator = driver.find_element(By.NAME, "username")
    # # print(username_locator)
    # email_holder_locator.send_keys("test007@givmail.com")
    # time.sleep(2) 

    # continue_button_locator = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/div/section/form/div[2]/button")
    # continue_button_locator.click()
    # time.sleep(2)
    
    # password_data = driver.find_elements(By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/div/section/form/div[1]/p[1]/label")
    # password_button_locator1 = driver.find_elements(By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/div/section/form/div[1]/div/input[2]")
    # # password_button_locator1.send_keys("Test@123")
    # password_button_locator1.send_keys("Test!12345")
    # time.sleep(2)
    # driver.quit()
    
    

# python -m pytest myenv\test_ticket_book.py