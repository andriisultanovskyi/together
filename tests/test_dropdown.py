import pytest
from selenium.webdriver.support.ui import WebDriverWait
from pages.homepage import HomePage



@pytest.mark.parametrize(
    "name, pre_locator, hover_method, assert_locator, click_method, expected_url",
    [
        # check dropdown Courses
        ("courses_dropdown", None, None, "COURSES_DROPDOWN", None, None),

        # hover Offline and checking the submenu
        ("hover_offline", "OFFLINE", "hover_offline", "OFFLINE_MENU", None, None),

        # hover Online and checking the submenu
        ("hover_online", "ONLINE", "hover_online", "ONLINE_MENU", None, None),

        # click All courses
        ("click_all_courses_button", None, None, None, "click_all_courses_button",
         "https://en.together.edu.pl/polishcourses"),
    ],
    ids=["courses", "hover_offline", "hover_online", "click_all_courses"]
)
def test_courses_param(driver, name, pre_locator, hover_method, assert_locator, click_method, expected_url):
    homepage = HomePage(driver)
    homepage.open()
    homepage.hover_courses()

    # preliminary waiting for the required element
    if pre_locator:
        homepage.wait_for_element_visible(getattr(homepage, pre_locator))

    # hover method
    if hover_method:
        getattr(homepage, hover_method)()

    # checking the visibility of elements
    if assert_locator:
        element = homepage.wait_for_element_visible(getattr(homepage, assert_locator))
        assert element.is_displayed()

    # click and checking URL
    if click_method:
        getattr(homepage, click_method)()
        WebDriverWait(driver, 5).until(lambda d: d.current_url == expected_url)
        assert driver.current_url == expected_url


@pytest.mark.parametrize("menu_path, action, expected_url", [
    (["OFFLINE", "ALL_COURSES_OFF"], "click_all_courses_off", "https://en.together.edu.pl/offlinecourses"),
    (["OFFLINE", "SEMESTER_COURSE"], "click_semester_course", "https://en.together.edu.pl/semester"),
    (["OFFLINE", "INTENSIVE_COURSE"], "click_intensive_course", "https://en.together.edu.pl/intensive"),
    (["OFFLINE", "YEARLONG_COURSE"], "click_yearlong_course", "https://en.together.edu.pl/yearlong"),
    (["OFFLINE", "INDIVIDUAL_CLASSES_OFF"], "click_individual_classes_off", "https://en.together.edu.pl/individual"),
    (["OFFLINE", "POLISH_LANGUAGE_IN_MEDICINE"], "click_polish_language_in_medicine", "https://en.together.edu.pl/polishformedicine"),
    (["OFFLINE", "COMPANY_COURSES_OFF"], "click_company_courses_off", "https://en.together.edu.pl/companycourses"),
    (["OFFLINE", "FOR_CHILDREN_AND_TEENAGERS"], "click_for_children_and_teenagers", "https://en.together.edu.pl/forchildren"),
])
def test_courses_offline(driver, menu_path, action, expected_url):
    homepage = HomePage(driver)
    homepage.open()
    homepage.hover_courses()

    # opening submenu Offline
    homepage.wait_for_element_visible(homepage.OFFLINE)
    homepage.hover_offline()

    # waiting for the last element
    last_locator = getattr(homepage, menu_path[-1])
    homepage.wait_for_element_visible(last_locator)

    # click on the element
    getattr(homepage, action)()

    # checking the URL transition
    WebDriverWait(driver, 5).until(lambda d: expected_url in d.current_url)
    assert expected_url in driver.current_url


@pytest.mark.parametrize("menu_path, action, expected_url", [
    (["ONLINE", "ALL_COURSES_ON"], "click_all_courses_on", "https://en.together.edu.pl/online"),
    (["ONLINE", "SEMESTER_COURSE_ON"], "click_semester_course_on", "https://en.together.edu.pl/semester"),
    (["ONLINE", "B1_POLISH_EXAM_COURSE"], "click_b1_polish_exam_course", "https://en.together.edu.pl/b1"),
    (["ONLINE", "B2_CERTIFICATE_COURSE"], "click_b2_certificate_course", "https://en.together.edu.pl/b2"),
    (["ONLINE", "C1_POLISH_EXAM_COURSE"], "click_c1_polish_exam_course", "https://en.together.edu.pl/c1"),
    (["ONLINE", "TELC_COURSE"], "click_telc_course", "https://en.together.edu.pl/telccourse"),
    (["ONLINE", "COMPANY_COURSES_ON"], "click_company_courses_on", "https://en.together.edu.pl/companycourses"),
    (["ONLINE", "INDIVIDUAL_CLASSES_ON"], "click_individual_classes_on", "https://en.together.edu.pl/individual"),
])
def test_courses_online(driver, menu_path, action, expected_url):
    homepage = HomePage(driver)
    homepage.open()
    homepage.hover_courses()

    # opening submenu Offline
    homepage.wait_for_element_visible(homepage.ONLINE)
    homepage.hover_online()

    # waiting for the last element
    last_locator = getattr(homepage, menu_path[-1])
    homepage.wait_for_element_visible(last_locator)

    # click on the element
    getattr(homepage, action)()

    # checking the URL transition
    WebDriverWait(driver, 5).until(lambda d: expected_url in d.current_url)
    assert expected_url in driver.current_url

