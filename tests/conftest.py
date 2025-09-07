import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import tempfile
import shutil
import logging
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException

# Logging settings
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def create_driver_instance():
    options = Options()
    user_data_dir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={user_data_dir}")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--no-first-run")
    options.add_argument("--disable-search-engine-choice-screen")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    driver_obj = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    return driver_obj, user_data_dir


@pytest.fixture
def driver():
    driver_obj, user_data_dir = create_driver_instance()
    yield driver_obj
    driver_obj.quit()
    # Clearing the temporary folder after completing the test
    try:
        shutil.rmtree(user_data_dir)
        logger.info(f"Deleted user data directory: {user_data_dir}")
    except OSError as e:
        logger.error(f"Error deleting user data directory {user_data_dir}: {e}")


@pytest.fixture
def close_cookie_popup(driver, timeout=10):
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((
                By.XPATH,
                "//div[@class='cky-consent-container' and @aria-label='Cenimy prywatność użytkowników']"))
        )
        accept_button = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 ".//button[contains(@class, 'cky-btn-accept') and contains(text(), 'Akceptuj wszystko')]"))
        )
        accept_button.click()
        print("Cookie popup closed")
    except TimeoutException:
        print("Cookie popup not found — probably already closed.")
    except Exception as e:
        print(f"Unexpected error while closing popup: {e}")
