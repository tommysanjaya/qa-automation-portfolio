import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Add Delay for Demo Purposes
DEMO_DELAY = 1

# --- FIXTURE: Setup and Teardown ---
@pytest.fixture()
def driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    
    yield driver  
    
    time.sleep(DEMO_DELAY) # Pause before closing the browser so you can see the final state
    driver.quit()

# --- POSITIVE TEST SCENARIO (TC-01) ---
def test_valid_login(driver):
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 5) 
    time.sleep(DEMO_DELAY) # Pause to show the page loaded

    # 1. Input valid credentials
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    time.sleep(DEMO_DELAY) # Pause to show username entered
    
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(DEMO_DELAY) # Pause to show password entered

    # 2. Click Login
    driver.find_element(By.ID, "login-button").click()

    # 3. Verify successful redirect
    products_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
    assert products_title.text == "Products", "Expected to see 'Products' on the inventory page."
    assert "inventory.html" in driver.current_url, "URL did not redirect to the inventory page."


# --- NEGATIVE TEST SCENARIO (TC-08) ---
def test_empty_password(driver):
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 5)
    time.sleep(DEMO_DELAY)

    # 1. Input valid username but leave password blank
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    time.sleep(DEMO_DELAY) 

    # 2. Click Login
    driver.find_element(By.ID, "login-button").click()
    time.sleep(DEMO_DELAY) # Pause to let reviewer read the specific empty password error

    # 3. Verify the error message for empty password
    error_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))
    expected_error = "Epic sadface: Password is required"
    
    assert error_element.text == expected_error, f"Expected error '{expected_error}', but got '{error_element.text}'"


# --- NEGATIVE TEST SCENARIO (TC-10) ---
def test_locked_out_user(driver):
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 5)
    time.sleep(DEMO_DELAY)

    # 1. Input locked out user credentials
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    time.sleep(DEMO_DELAY)
    
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(DEMO_DELAY)

    # 2. Click Login
    driver.find_element(By.ID, "login-button").click()
    time.sleep(DEMO_DELAY) # Pause to show the error message popping up

    # 3. Verify the exact error message text appears
    error_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))
    expected_error = "Epic sadface: Sorry, this user has been locked out."
    
    assert error_element.text == expected_error, f"Expected error '{expected_error}', but got '{error_element.text}'"