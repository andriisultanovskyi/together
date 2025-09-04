from selenium.webdriver.common.by import By
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

    PL_BUTTON = (
        By.XPATH,
        "//div[@class='t199__lang']/a[@class='t199__lang-item' and normalize-space(text())='Pl']"
    )

    RU_BUTTON = (
        By.XPATH,
        "//div[@class='t199__lang']/a[@class='t199__lang-item' and normalize-space(text())='Ru']"
    )

    COURSES_BUTTON = (By.XPATH, "//a[contains(@class, 't978__tm-link') and text()='Courses']")

    COURSES_DROPDOWN = (By.XPATH, "//ul[@class='t978__menu' and @style='width: 180px;']")

    ALL_COURSES = (
        By.XPATH,
        "//span[contains(@class, 't978__link-inner') and normalize-space()='All courses']"
    )

    ALL_COURSES_OFF = (
        By.XPATH,
        "//a[@href='/offlinecourses']/span[text()='All courses']"
    )

    ALL_COURSES_ON = (
        By.XPATH,
        "//a[@href='/online']/span[text()='All courses']"
    )

    OFFLINE = (By.XPATH, "//span[text()='Offline']")

    ONLINE = (By.XPATH, "//span[text()='Online']")

    OFFLINE_MENU = (
        By.XPATH,
        "//span[normalize-space()='Intensive course']/ancestor::div[contains(@class,'t978__innermenu-content')]"
    )

    ONLINE_MENU = (
        By.XPATH,
        "//span[normalize-space()='B1 Polish exam course']/ancestor::div[contains(@class,'t978__innermenu-content')]"
    )

    SEMESTER_COURSE = (
        By.XPATH,
        "//span[normalize-space()='Intensive course']/ancestor::div[contains(@class,'t978__innermenu-content')]//span[normalize-space()='Semester course']"
    )

    INTENSIVE_COURSE = (By.XPATH, "//span[normalize-space(text())='Intensive course']")

    YEARLONG_COURSE = (By.XPATH, "//span[normalize-space(text())='Yearlong course']")

    INDIVIDUAL_CLASSES_OFF = (By.XPATH, "(//span[normalize-space(text())='Individual classes'])[1]")

    INDIVIDUAL_CLASSES_ON = (By.XPATH, "(//span[normalize-space(text())='Individual classes'])[2]")

    POLISH_LANGUAGE_IN_MEDICINE = (By.XPATH, "//span[normalize-space(text())='Polish language in Medicine']")

    COMPANY_COURSES_OFF = (By.XPATH, "(//span[normalize-space(text())='Company courses'])[1]")

    COMPANY_COURSES_ON = (By.XPATH, "(//span[normalize-space(text())='Company courses'])[2]")

    FOR_CHILDREN_AND_TEENAGERS = (By.XPATH, "//span[normalize-space(text())='For children and teenagers']")

    SEMESTER_COURSE_ON = (
        By.XPATH,
        "//a[@data-menu-item-number='3' and @href='/semester']//span[text()='Semester course']"
    )
    B1_POLISH_EXAM_COURSE = (By.XPATH, "//span[normalize-space(text())='B1 Polish exam course']")

    B2_CERTIFICATE_COURSE = (By.XPATH, "//span[normalize-space(text())='B2 certificate course']")

    C1_POLISH_EXAM_COURSE = (By.XPATH, "//span[normalize-space(text())='C1 Polish exam course']")

    TELC_COURSE = (By.XPATH, "//span[normalize-space(text())='TELC course']")

    TEST_YOUR_POLISH = (By.XPATH, "//span[contains(normalize-space(.), 'Test your Polish')]")

    REGISTER_FOR_YOUR_CERTIFICATE = (By.XPATH, "//span[contains(normalize-space(.), 'certificate exam')]")

    REVISIT_CONSENT_BUTTON = (By.XPATH, "//img[@alt='Revisit consent button']")

    CONTACT_INFORMATION_BUTTON = (By.CLASS_NAME, "t708__btn")



    def open(self):
        super().open(self.URL)
        self.close_cookie_popup()

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

    def click_pl_button(self):
        self.wait_for_element_to_be_clickable(self.PL_BUTTON).click()

    def click_ru_button(self):
        self.wait_for_element_to_be_clickable(self.RU_BUTTON).click()

    def hover_courses(self):
        element = self.wait_for_element_visible(self.COURSES_BUTTON)
        self.hover(element)
        return element

    def click_all_courses_button(self):
        self.wait_for_element_to_be_clickable(self.ALL_COURSES).click()

    def click_all_courses_off(self):
        self.wait_for_element_to_be_clickable(self.ALL_COURSES_OFF).click()

    def click_all_courses_on(self):
        self.wait_for_element_to_be_clickable(self.ALL_COURSES_ON).click()

    def hover_offline(self):
        element = self.wait_for_element_visible(self.OFFLINE)
        self.hover(element)
        return element

    def hover_online(self):
        element = self.wait_for_element_visible(self.ONLINE)
        self.hover(element)
        return element

    def click_semester_course(self):
        self.wait_for_element_to_be_clickable(self.SEMESTER_COURSE).click()

    def click_intensive_course(self):
        self.wait_for_element_to_be_clickable(self.INTENSIVE_COURSE).click()

    def click_yearlong_course(self):
        self.wait_for_element_to_be_clickable(self.YEARLONG_COURSE).click()

    def click_individual_classes_off(self):
        self.wait_for_element_to_be_clickable(self.INDIVIDUAL_CLASSES_OFF).click()

    def click_polish_language_in_medicine(self):
        self.wait_for_element_to_be_clickable(self.POLISH_LANGUAGE_IN_MEDICINE).click()

    def click_company_courses_off(self):
        self.wait_for_element_to_be_clickable(self.COMPANY_COURSES_OFF).click()

    def click_for_children_and_teenagers(self):
        self.wait_for_element_to_be_clickable(self.FOR_CHILDREN_AND_TEENAGERS).click()

    def click_semester_course_on(self):
        self.wait_for_element_to_be_clickable(self.SEMESTER_COURSE_ON).click()

    def click_b1_polish_exam_course(self):
        self.wait_for_element_to_be_clickable(self.B1_POLISH_EXAM_COURSE).click()

    def click_b2_certificate_course(self):
        self.wait_for_element_to_be_clickable(self.B2_CERTIFICATE_COURSE).click()

    def click_c1_polish_exam_course(self):
        self.wait_for_element_to_be_clickable(self.C1_POLISH_EXAM_COURSE).click()

    def click_telc_course(self):
        self.wait_for_element_to_be_clickable(self.TELC_COURSE).click()

    def click_company_courses_on(self):
        self.wait_for_element_to_be_clickable(self.COMPANY_COURSES_ON).click()

    def click_individual_classes_on(self):
        self.wait_for_element_to_be_clickable(self.INDIVIDUAL_CLASSES_ON).click()

    def click_test_your_polish_button(self):
        self.wait_for_element_to_be_clickable(self.TEST_YOUR_POLISH).click()

    def click_register_for_your_certificate(self):
        self.wait_for_element_to_be_clickable(self.REGISTER_FOR_YOUR_CERTIFICATE).click()

    def click_revisit_consent_button(self):
        self.wait_for_element_to_be_clickable(self.REVISIT_CONSENT_BUTTON).click()

    def click_contact_information_button(self):
        self.wait_for_element_to_be_clickable(self.CONTACT_INFORMATION_BUTTON).click()
