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


@ddt
class RegisterCourseTests(unittest.TestCase):

    def setUp(self):
        self.hp = Homepage()
        self.lp= loginPage()
        self.courses=Courses()
        self.javas_enroll=javascript_enroll()
        self.checkout=Checkout()

        self.baseurl = "https://letskodeit.teachable.com/"
        self.lp.driver.get(self.baseurl)
        self.lp.driver.maximize_window()
        self.lp.driver.implicitly_wait(10)

    @data(*getCSVdata(r'C:\Users\rsingh\PycharmProjects\automationProject\testdata\testdata.csv'))
    @unpack
    def test_click_one_Course(self, coursename ,payment_method, ccNum, ccexp, ccCvc, zip):
        self.lp.valid_login("ravinder267@gmail.com","ninja77")
        if coursename == "javascript":
            self.courses.click_javascript_course()
        elif coursename == "python_scratch":
            self.courses.click_python_Scratch_course()
        elif coursename == "selenium_python":
            self.courses.click_selenium_python_course()
        else:
            print("no course")
        self.javas_enroll.click_enroll_button_top()
        self.checkout.scroll_to_bottom()
        #self.checkout.scroll_to_bottom()
        self.checkout.waitfor()
        self.checkout.enter_creditcard_details(payment_method,ccNum,ccexp,ccCvc,zip)
        sleep(3)
        self.lp.takeScreenshot("screenshot taken")


    def tearDown(self):
        pass