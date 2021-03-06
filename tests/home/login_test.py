from selenium import webdriver
from pages.home.login_page import loginPage
from pages.home.home_page import Homepage
import unittest
import pytest
from  selenium.webdriver.common.by import By
import time
import HtmlTestRunner
import xmlrunner

# @pytest.mark.usefixtures("OneTimeSetup","setUp")
# class logintest(unittest.TestCase):
#
#     def __init__(self,driver):
#         self.driver=driver
#
#     @pytest.fixture(autouse=True)
#     def classSetup(self,OneTimeSetup):
#         self.lp=loginPage(self.driver)
#         self.hp=Homepage(self.driver)
#
#     @pytest.mark.run(order=1)
#     def test_validlogin(self,setUp):
#         self.email = "ravinder267@gmail.com"
#         self.passwd = "ninja77"
#         self.lp.valid_login(self.email,self.passwd)
#         result=self.hp.verify_search_box()
#         self.assertTrue(result,"search_bcoz_not_found")
#         self.hp.enter_text_search_box("javascript")

    # def test_enter_javascript(self):
    #
class logintest(unittest.TestCase):


    @classmethod
    def setUp(self):
        self.lp=loginPage()
        self.hp=Homepage()

        baseurl = "https://letskodeit.teachable.com/"
        self.lp.driver.get(baseurl)
        self.lp.driver.maximize_window()
        self.lp.driver.implicitly_wait(10)



    def test_validlogin(self):
        self.email = "ravinder267@gmail.com"
        self.passwd = "ninja77"
        self.lp.valid_login(self.email,self.passwd)
        self.lp.takeScreenshot("loginpage")
        result=self.hp.verify_search_box()
        self.assertTrue(result,"search_bcoz_not_found")
        self.hp.enter_text_search_box("javascript")
        time.sleep(3)




    # def test_invalid_login(self):
    #     self.email = "ravinder267@gmail.co"
    #     self.passwd = "ninja77"
    #     self.lp.valid_login(self.email, self.passwd)
    #     if self.lp.get_invalid_login_message() == "Invalid email or password.":
    #         print(self.lp.get_invalid_login_message())
    #         myresult=True
    #     else:
    #         myresult=False
    #     self.assertTrue(myresult,"message must be different")
    #     self.lp.takeScreenshot("invalid_loginpage")

    @classmethod
    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output=out),
    failfast=False, buffer=False, catchbreak=False, exit=False)
