from selenium import webdriver

class webdriverProvider():
    def getwebdriver(self):
        #self.driver = webdriver.Firefox(executable_path="C:\\Users\\rsingh\\PycharmProjects\\automationProject\\webdrivers\\geckodriver-v0.24.0-self.driver= webdriver.Chrome(executable_path=r"C:\Users\ravin\PycharmProjects\python_selenium\webdrivers\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
      #  myele=self.driver.find_element_by_id()
      #  myele.is




        return self.driver