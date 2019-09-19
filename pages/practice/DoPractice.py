from selenium import webdriver
from base.selenium_common import SeleniumCommon
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep



class practice(SeleniumCommon):

    _dropdown_id = "carselect"
    signup_xpath="//a[contains(text(),'Sign')]"
    login_xpath="//a[@href='/sign_in']"

    def __init__(self):
        self.driver=webdriver.Chrome(r"C:\Users\rsingh\PycharmProjects\automationProject\webdrivers\chromedriver_win32\chromedriver.exe")


    def runtest(self):
        self.driver.implicitly_wait(10)
        self.driver.get("https://learn.letskodeit.com/p/practice")
        self.driver.maximize_window()

    def click_dropdown(self,click_this):
        sel=Select(self.getelement(By.ID,self._dropdown_id))
        sel.select_by_visible_text(click_this)
        sleep(1)
        sel.select_by_value("benz")
        sleep(1)
        sel.select_by_index(0)

    def click_Sign_up(self):
        self.click_element(By.XPATH,self.signup_xpath)

    def click_login(self):
        self.click_element(By.XPATH,self.login_xpath)








mytest=practice()
mytest.runtest()
#mytest.click_dropdown("Honda")
mytest.click_login()
