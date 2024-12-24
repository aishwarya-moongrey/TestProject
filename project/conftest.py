import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager  # Optional, handles driver installation

# Test Setup
@pytest.fixture(autouse=True)
def driver():
    # Setup Chrome driver
    options = Options()
    options.add_argument('--headless')

    options.addArguments("start-maximized");# open Browser in maximized mode
    options.addArguments("disable-infobars"); #// disabling infobars
    options.addArguments("--disable-extensions"); #// disabling extensions
    options.addArguments("--disable-gpu"); #// applicable to windows os only
    options.addArguments("--disable-dev-shm-usage"); #// overcome limited resource problems
    options.addArguments("--no-sandbox"); #// Bypass OS security model

    # options.headless = True  # Optional: run the browser in the background without UI
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://rahulshettyacademy.com/")
    driver.maximize_window()
    yield driver
    driver.quit()