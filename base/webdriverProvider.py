from selenium import webdriver

class webdriverProvider():
    def getwebdriver(self):
        #self.driver = webdriver.Firefox(executable_path="C:\\Users\\rsingh\\PycharmProjects\\automationProject\\webdrivers\\geckodriver-v0.24.0-win64\\geckodriver.exe")
        self.driver= webdriver.Chrome(executable_path=r"C:\Users\ravin\PycharmProjects\python_selenium\webdrivers\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
<<<<<<< HEAD
      #  myele=self.driver.find_element_by_id()
      #  myele.is
=======



>>>>>>> f14b922b77c4ed0e36f438a796ad953dc436a3a7
        return self.driver