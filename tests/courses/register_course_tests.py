import unittest
from pages.home.login_page import loginPage
from pages.home.home_page import Homepage
from pages.courses.Courses_page import Courses
from pages.courses.javascript_enroll_page import javascript_enroll
from pages.courses.Checkout_page import Checkout
import unittest
import pytest
from base.webdriverProvider import webdriverProvider
from time import sleep


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

    def test_click_one_Course(self):
        self.lp.valid_login("ravinder267@gmail.com","ninja77")
        self.courses.click_javascript_course()
        self.javas_enroll.click_enroll_button_top()
        self.checkout.scroll_to_bottom()
        print("button result is:", self.checkout.check_confrim_button_Disabled())
        self.checkout.enter_creditcard_details("cc",12234442,"22/2",233,"201301")
        self.checkout.click_agree_to_terms()
        print("button result is:",self.checkout.check_confrim_button_Disabled())
        self.lp.takeScreenshot()

    def tearDown(self):
        loginPage.driver.quit()


