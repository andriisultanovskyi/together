from selenium.webdriver.common.by import By
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


# The test checks the click of the "Ukrainian version" button on the header and opens a web page in Ukrainian
def test_click_ukrainian_version_button(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_ukrainian_version_button()
    element = homepage.wait_for_element_visible((
            By.XPATH,
            "//strong[contains(text(), 'Школа польської мови Together')]"
        ))
    assert element.is_displayed()


# The test checks the click of the "PL" button on the header and opens a web page in Polish
def test_click_pl_button(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_pl_button()
    element = homepage.wait_for_element_visible((
            By.XPATH,
            "//span[contains(text(), 'Polski otworzy Ci nowe możliwości')]"
        ))
    assert element.is_displayed()


# The test checks the click of the "RU" button on the header and opens a web page in Russian
def test_click_ru_button(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_ru_button()
    element = homepage.wait_for_element_visible((
            By.XPATH,
            "//div[normalize-space()='Польский — твой ключ к новым возможностям! Учись у профессионалов.']"
        ))
    assert element.is_displayed()


# The test checks the click of the "Test your Polish" button on the header and opens a web page in Russian
def test_click_test_your_polish_button(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_test_your_polish_button()
    assert "https://en.together.edu.pl/test_poziomujacy" in driver.current_url


def test_click_register_for_your_certificate(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_register_for_your_certificate()
    assert "https://en.together.edu.pl/stateexam" in driver.current_url


def test_click_revisit_consent_button(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_revisit_consent_button()
    element = homepage.wait_for_element_visible((
        By.XPATH,
        "//span[normalize-space()='Dostosuj preferencje dotyczące zgody']"
    ))
    assert element.is_displayed()


def test_click_contact_information_button(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_contact_information_button()
    element = homepage.wait_for_element_visible((By.CLASS_NAME, "t708__wrapper"))
    assert element.is_displayed()
