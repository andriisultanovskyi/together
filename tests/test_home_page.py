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


# The test checks the click of the "Legalisation" button on the header and goes to the 'Legalisation in Poland' page
def test_click_legalisation_button(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_legalisation_button()
    assert "https://en.together.edu.pl/legalization" in driver.current_url


# The test checks the click of the "About Us" button on the header and goes to the 'About Us' page
def test_click_about_us_button(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_about_us_button()
    assert "https://en.together.edu.pl/aboutus" in driver.current_url


# The test checks the click of the "Contact" button on the header and goes to the 'Contacts' page
def test_click_contact_button(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_contact_button()
    assert "https://en.together.edu.pl/contact" in driver.current_url


# The test checks the click of the "Ukrainian version" button on the header and goes to the Ukrainian version of the site
def test_click_ukrainian_version_button(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_ukrainian_version_button()
    assert driver.find_element(
    By.XPATH,
    "//strong[normalize-space(text())='Школа польської мови Together']"
    )
