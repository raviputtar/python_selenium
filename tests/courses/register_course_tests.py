import unittest
from pages.home.login_page import loginPage
from pages.home.home_page import Homepage
from pages.courses.Courses_page import Courses
from pages.courses.javascript_enroll_page import javascript_enroll
import unittest
import pytest
from base.webdriverProvider import webdriverProvider
from time import sleep

class RegisterCourseTests(unittest.TestCase):

    def setUp(self):
        wp = webdriverProvider()
        self.driver = wp.getwebdriver()
        self.hp = Homepage(self.driver)
        self.lp= loginPage(self.driver)
        self.courses=Courses(self.driver)
        self.javas_enroll=javascript_enroll(self.driver)
        baseurl = "https://letskodeit.teachable.com/"
        self.driver.get(baseurl)

    def test_click_one_Course(self):
        self.lp.valid_login("ravinder267@gmail.com","ninja77")
        self.courses.click_javascript_course()
        sleep(5)
        self.javas_enroll.click_enroll_button_top()
        sleep(5)

        print("we have done it ")

    # def tearDown(self):
    #     self.driver.quit()


