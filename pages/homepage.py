from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class HomePage(BasePage):
    URL = 'https://en.together.edu.pl/'

    EXAMS_BUTTON = (By.XPATH, "//a[@href='/exams' and normalize-space(text())='Exams']")
    LEGALISATION_BUTTON = (
        By.XPATH,
        "//a[contains(@class, 't199__menu-item') and "
        "contains(@class, 't-title') and "
        "contains(@class, 't-menu__link-item') and "
        "text()='Legalisation']"
    )
    ABOUT_US_BUTTON = (By.XPATH, "//a[@href='/aboutus' and normalize-space(text())='About us']")
    CONTACT_BUTTON = (By.XPATH, "//a[@href='/contact' and normalize-space(text())='Contact']")
    UKRAINIAN_VERSION_BUTTON = (By.XPATH, "//a[normalize-space(text())='Українська версія']")

    def open(self):
        super().open(self.URL)

    def click_exams_button(self):
        self.wait_for_element_to_be_clickable(self.EXAMS_BUTTON).click()


    def click_legalisation_button(self):
        self.wait_for_element_to_be_clickable(self.LEGALISATION_BUTTON).click()


    def click_about_us_button(self):
        self.wait_for_element_to_be_clickable(self.ABOUT_US_BUTTON).click()


    def click_contact_button(self):
        self.wait_for_element_to_be_clickable(self.CONTACT_BUTTON).click()


    def click_ukrainian_version_button(self):
        self.wait_for_element_to_be_clickable(self.UKRAINIAN_VERSION_BUTTON).click()


