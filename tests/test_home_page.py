import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from pages.homepage import HomePage


# The test checks the click of the "Exams" button on the header and goes to the 'Exams' page
def test_click_button_exams(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_exams_button()
    assert "https://en.together.edu.pl/exams" in driver.current_url
