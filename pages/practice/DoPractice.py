from selenium import webdriver

class practice(webdriver):
    def __init__(self):
        self.driver=webdriver.Chrome(r"C:\Users\rsingh\PycharmProjects\automationProject\webdrivers\chromedriver_win32\chromedriver.exe")


    def runtest(self):
        self.driver.get("https://learn.letskodeit.com/p/practice")



mytest=practice()
mytest.runtest()