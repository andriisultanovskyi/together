from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


class BasePage:
    DEFAULT_TIMEOUT = 10

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def find_element(self, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_element_to_be_clickable(self, locator, timeout=DEFAULT_TIMEOUT):
        """Waits for the element to become clickable."""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_element_visible(self, locator, timeout=DEFAULT_TIMEOUT):
        """Waits for the element to be visible on the page."""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_url_contains(self, text, timeout=DEFAULT_TIMEOUT):
        """Waits until the URL contains the specified text."""
        return WebDriverWait(self.driver, timeout).until(
            EC.url_contains(text)
        )

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    COOKIE_POPUP_CONTAINER = (
        By.XPATH, "//div[@class='cky-consent-container' and @aria-label='Cenimy prywatność użytkowników']")
    COOKIE_ACCEPT_BUTTON = (
        By.XPATH, ".//button[contains(@class, 'cky-btn-accept') and contains(text(), 'Akceptuj wszystko')]")

    def close_cookie_popup(self, timeout=None):
        if timeout is None:
            timeout = self.timeout
        print("Trying to close cookie popup")
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(self.COOKIE_POPUP_CONTAINER)
            )
            print("Cookie popup was found.")
            accept_button = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(self.COOKIE_ACCEPT_BUTTON)
            )
            accept_button.click()
            print("The cookie popup button is pressed")
            self.wait_for_element_to_disappear(self.COOKIE_POPUP_CONTAINER, timeout=timeout)
        except TimeoutException:
            print("Cookie popup not found — probably already closed.")
        except Exception as e:
            print(f"Unexpected error while closing popup: {e}")

    def open(self, url):
        self.driver.get(url)
        self.close_cookie_popup()
