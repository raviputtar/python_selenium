import unittest
from pages.home.login_page import loginPage
from pages.home.home_page import Homepage
from pages.courses.Courses_page import Courses
from pages.courses.javascript_enroll_page import javascript_enroll
from pages.courses.Checkout_page import Checkout
import unittest
import pytest
from time import sleep
from ddt import ddt, unpack, data
from utility.getCSVdata import getCSVdata


@pytest.mark.usefixtures("onetimesetup","setup")
@ddt
class RegisterCourseTests(unittest.TestCase):

        lp=loginPage()
        hp=Homepage()
        courses = Courses()
        javas_enroll = javascript_enroll()
        checkout = Checkout()

    @data(*getCSVdata(r'C:\Users\ravin\PycharmProjects\python_selenium\testdata\testdata.csv'))
    @unpack
    def test_click_one_Course(self, coursename,payment_method, ccNum, ccexp, ccCvc, zip,onetimesetup):
        self.lp.valid_login("ravinder267@gmail.com","ninja77")
        if coursename == "javascript":
            self.courses.click_javascript_course()
        elif coursename == "python_scratch":
            self.courses.click_python_Scratch_course()
        elif coursename == "selenium_python":
            self.courses.click_selenium_python_course()
        else:
            print("no course")
        sleep(3)
        self.javas_enroll.click_enroll_button_top()
        sleep(3)
        #self.checkout.scroll_to_bottom()
        self.checkout.enter_creditcard_details(payment_method,ccNum,ccexp,ccCvc,zip)

        print("we have done it ")

    # def tearDown(self):
    #     self.driver.quit()


