import unittest
from pages.courses.register_courses import RegisterCoursePage
from pages.home.login_page import loginPage
from pages.home.home_page import Homepage
import unittest
import pytest
from base.webdriverProvider import webdriverProvider

class RegisterCourseTests(unittest.TestCase):

    def setUp(self):
        wp = webdriverProvider()
        self.driver = wp.getwebdriver()
        self.hp = Homepage(self.driver)
        self.lp= loginPage(self.driver)
        baseurl = "https://letskodeit.teachable.com/"
        self.driver.get(baseurl)

    def test_enroll(self):
        self.lp.valid_login("ravinder267@gmail.com","ninja77")
        self.hp.click_selenium_java_Course()
        print("we have done it ")

    # def tearDown(self):
    #     self.driver.quit()


