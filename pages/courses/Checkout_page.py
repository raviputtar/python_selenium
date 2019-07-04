from base.selenium_common import SeleniumCommon
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

class Checkout(SeleniumCommon):

    def __init__(self,driver):
        super().__init__(driver)
        driver=self.driver


    dropdown_locator="//select[@name='dropdown_select']"
    cardnumber_locator="// div[ @ id = 'root'] / form // input[ @ name = 'cardnumber']"

    expdate_locator="// div[ @ id = 'root'] / form // input[ @ name = 'exp-date']"

    cvc="// div[ @ id = 'root'] / form // input[ @ name = 'cvc']"
    postal_code_locator="// div[ @ id = 'root'] / form // input[ @ name = 'postal']"
    country_dropdown_locator_id="country_code_credit_card-cc"

    def select_payment_method(self,method):
        myelement=self.getelement(By.XPATH,self.dropdown_locator)

        sel=Select(myelement)
        if method=="cc":
            sel.select_by_value("credit_card")
        else:
            sel.select_by_visible_text("PayPal")


    def enter_cardnumber(self,cardno):
        myelement=self.getelement(By.XPATH,self.cardnumber_locator)
        if myelement.
        self.element_sendkeys("23456",By.XPATH,self.cardnumber_locator)


    def enter_expiration_date(self,expdate):
        self.element_sendkeys(expdate,By.XPATH,self.expdate_locator)

    def enter_cvc(self,cvc):
        self.element_sendkeys(cvc,By.XPATH,self.cvc)

    def enter_postal(self,postal):
        self.element_sendkeys(postal,By.XPATH,self.postal_code_locator)

    def enter_creditcard_details(self,method,cardnum,expdate,cvc,postal):
        self.select_payment_method(method)
        self.enter_cardnumber(cardnum)
        self.enter_expiration_date(expdate)
        self.enter_cvc(cvc)
        self.enter_postal(postal)











