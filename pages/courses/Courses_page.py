from base.selenium_common import SeleniumCommon
from selenium.webdriver.common.by import By

class Courses(SeleniumCommon):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    javascript_course_locator="//div[contains(text(),'JavaScript for beginners')]"
    selenium_python_course_locator="//div[contains(text(),'Selenium WebDriver With Python 3.x')]"
    python_scratch_Course_locator="//div[contains(text(),'Learn Python 3 from scratch')]"

    def click_javascript_course(self):
        self.click_element(By.XPATH,self.javascript_course_locator)

    def click_selenium_python_course(self):
        self.click_element(By.XPATH,self.selenium_python_course_locator)

    def click_python_Scratch_course(self):
        self.click_element(By.XPATH,self.python_scratch_Course_locator)




