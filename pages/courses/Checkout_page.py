from base.selenium_common import SeleniumCommon
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

class Checkout(SeleniumCommon):

    dropdown_locator="//select[@name='dropdown_select']"
    cardnumber_locator="// div[ @ id = 'root'] / form // input[ @ name = 'cardnumber']"

    expdate_locator="// div[ @ id = 'root'] / form // input[ @ name = 'exp-date']"

    cvc="// div[ @ id = 'root'] / form // input[ @ name = 'cvc']"
    postal_code_locator="// div[ @ id = 'root'] / form // input[ @ name = 'postal']"
    country_dropdown_locator_id="country_code_credit_card-cc"

    _credit_card_frame='__privateStripeFrame8'
    _Expdate_frame='__privateStripeFrame9'
    cvc_frame='__privateStripeFrame10'
    zip_frame='__privateStripeFrame11'



    def select_payment_method(self,method):

        myelement=self.getelement(By.XPATH,self.dropdown_locator)

        sel=Select(myelement)
        if method=="cc":
            sel.select_by_value("credit_card")
        else:
            sel.select_by_visible_text("PayPal")


    def enter_cardnumber(self,cardno):
        self.switch_frame(self._credit_card_frame)
        self.element_sendkeys("23456",By.XPATH,self.cardnumber_locator)
        self.switch_to_main()


    def enter_expiration_date(self,expdate):
        self.switch_frame(self._Expdate_frame)
        self.element_sendkeys(expdate,By.XPATH,self.expdate_locator)
        self.switch_to_main()

    def enter_cvc(self,cvc):
        self.switch_frame(self.cvc_frame)
        self.element_sendkeys(cvc,By.XPATH,self.cvc)
        self.switch_to_main()

    def enter_postal(self,postal):
        self.switch_frame(self.zip_frame)
        self.element_sendkeys(postal,By.XPATH,self.postal_code_locator)
        self.switch_to_main()

    def enter_creditcard_details(self,method,cardnum,expdate,cvc,postal):
        print("method is:",method)
        self.enter_cardnumber(cardnum)
        self.enter_expiration_date(expdate)
        self.enter_cvc(cvc)
        self.enter_postal(postal)











