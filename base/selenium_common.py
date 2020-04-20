import time
import os
import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class SeleniumCommon():

    driver = webdriver.Chrome(executable_path=r"C:\Users\ravin\PycharmProjects\python_selenium\webdrivers\chromedriver_win32\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()

    def is_element_present(self,locator_type,locator):
        myelement=self.driver.find_element(locator_type,locator)
        if myelement is not None:
            return True
        else:
            return False

    def getelement(self,locator_type,locator):
        myelement=self.driver.find_element(locator_type,locator)
        return myelement


    def gettext(self,locator_type,locator):
        myelement=self.driver.find_element(locator_type,locator)
        mytext=myelement.text
        return mytext


    def click_element(self,locator_type,locator):
        myelement = self.driver.find_element(locator_type, locator)
        print(myelement)
        if myelement is not None:
            myelement.click()
        else:
            print("element_not_found")

    def element_sendkeys(self,data,locator_type,locator):
        myelement = self.driver.find_element(locator_type,locator)
        if myelement is not None:
            myelement.send_keys(data)
        else:
            print("element is not found")



    def takeScreenshot(self, resultmessage):
        filename = resultmessage + "_" + str(datetime.date.today()) + "_"+".png"
        screenshotDirectory = "Screenshots"
        relativefilename = screenshotDirectory + "\\" + filename
        currentDir = os.path.dirname(__file__)
        destinationfilename = currentDir + "\\" + relativefilename
        print(destinationfilename)
        destinationDir = os.path.join(currentDir, screenshotDirectory)

        try:
            if not os.path.exists(destinationDir):
                os.makedirs(destinationDir)
            self.driver.save_screenshot(destinationfilename)
        except:
            print("screenshot could not be taken")

    def scroll_to_bottom(self):
        self.driver.find_element_by_tag_name('body').send_keys(Keys.END)

    def scroll_to_element(self,element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def switch_frame(self,frame_ref):
        self.driver.switch_to.frame(frame_ref)

    def switch_frame_default(self):
        self.driver.switch_to.default_content()

    def switch_to_main(self):
        self.driver.switch_to.default_content()