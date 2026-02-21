import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Set up Chrome options (Optional: add "--headless" to run without a window)
    options = webdriver.ChromeOptions()
    
    # Setup: Initialize the Chrome Driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    driver.maximize_window()
    driver.implicitly_wait(10) # Wait up to 10s for elements to appear
    
    yield driver
    
    # Teardown: Close the browser after the test
    driver.quit()