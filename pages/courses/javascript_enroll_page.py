from base.selenium_common import SeleniumCommon
from selenium.webdriver.common.by import By

class javascript_enroll(SeleniumCommon):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver


    enroll_button_top_locator="//button[@id='enroll-button-top']"

    def click_enroll_button_top(self):
        self.click_element(By.XPATH,self.enroll_button_top_locator)

