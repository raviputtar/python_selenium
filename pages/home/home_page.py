from selenium.webdriver.common.by import By
from base.selenium_common import SeleniumCommon

class Homepage(SeleniumCommon):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    #locators

    search_courses="//input[@id='search-courses']"
    webdriver_java_course="//div[@data-course-id='56738']"

    def verify_search_box(self):
        if (self.is_element_present(By.XPATH,self.search_courses)):
            return True
        else:
            return False

    def enter_text_search_box(self,data):
        self.click_element(By.XPATH,self.search_courses)
        self.element_sendkeys(data,By.XPATH,self.search_courses)

    def click_selenium_java_Course(self):
        self.click_element(By.XPATH,self.webdriver_java_course)







