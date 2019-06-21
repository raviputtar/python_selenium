import time
import os

from selenium import webdriver
class SeleniumCommon():
    def __init__(self,driver):
        self.driver=driver


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
        myelement = self.driver.find_element(locator_type, locator)
        if myelement is not None:
            myelement.send_keys(data)
        else:
            print("element is not found: sorry!!")

    def takeScreenshot(self, resultmessage):
        filename = resultmessage + "_" + str(round(time.time())) + ".png"
        screenshotDirectory = "Screenshots"
        relativefilename = screenshotDirectory + "\\" + filename
        currentDir = os.path.dirname(__file__)
        destinationfilename = currentDir + "\\" + relativefilename
        destinationDir = os.path.join(currentDir, screenshotDirectory)

        try:
            if not os.path.exists(destinationDir):
                os.makedirs(destinationDir)
            self.driver.save_screenshot(destinationfilename)
        except:
            print("screenshot could not be taken")