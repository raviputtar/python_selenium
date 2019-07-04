from selenium import webdriver

class webdriverProvider():
    def getwebdriver(self):
      #  self.driver = webdriver.Firefox(executable_path="C:\\Users\\rsingh\\PycharmProjects\\automationProject\\webdrivers\\geckodriver-v0.24.0-win64\\geckodriver.exe")
        self.driver= webdriver.Chrome(executable_path=r"C:\Users\rsingh\PycharmProjects\automationProject\webdrivers\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        return self.driver