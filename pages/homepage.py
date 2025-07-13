from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class HomePage(BasePage):
    URL = 'https://en.together.edu.pl/'

    EXAMS_BUTTON = (By.XPATH, "//a[@href='/exams' and normalize-space(text())='Exams']")

    def open(self):
        super().open(self.URL)

    def click_exams_button(self):
        self.wait_for_element_to_be_clickable(self.EXAMS_BUTTON).click()


