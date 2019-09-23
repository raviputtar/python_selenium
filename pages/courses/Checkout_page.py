from base.selenium_common import SeleniumCommon
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

class Checkout(SeleniumCommon):



    dropdown_button_locator="//button[@class='dropbtn minimal']"
    dropdown_paypal_method_locator="//div[@id='option-container']//span[@class='option-text'][contains(text(),'Paypal')]"
    dropdown_creditcard_method_locator="//div[@id='option-container']//span[@class='option-text'][contains(text(),'Credit Card')]"
    #cardnumber_locator="// div[ @ id = 'root'] / form // input[ @ name = 'cardnumber']"
    cardnumber_locator="//*[@id='root']/form/span[2]/span/input"

    agreement_checkbox_id='agreed_to_terms_checkbox'

    expdate_locator="// div[ @ id = 'root'] / form // input[ @ name = 'exp-date']"

    cvc="// div[ @ id = 'root'] / form // input[ @ name = 'cvc']"
    postal_code_locator="// div[ @ id = 'root'] / form // input[ @ name = 'postal']"
    country_dropdown_locator_id="country_code_credit_card-cc"

    cardno_frame_name="__privateStripeFrame8"
    expdate_frame_name="__privateStripeFrame9"
    cvc_frame_name="__privateStripeFrame10"
    postal_frame_name="__privateStripeFrame11"

    confirm_purchase_button_id="confirm-purchase"

    def click_paypal(self):
        self.click_element(By.XPATH,self.dropdown_paypal_method_locator)

    def click_creditcard(self):
        self.click_element(By.XPATH,self.dropdown_creditcard_method_locator)

    def select_payment_method(self,method):
        self.click_dropdown_button()
        if method=="cc":
            self.click_creditcard()
        else:
            self.click_paypal()


    def click_dropdown_button(self):
        self.click_element(By.XPATH,self.dropdown_button_locator)

    def enter_cardnumber(self,cardno):
        self.switch_frame(self.cardno_frame_name)
        self.element_sendkeys(cardno,By.XPATH,self.cardnumber_locator)
        self.switch_frame_default()

    def enter_expiration_date(self,expdate):
        self.switch_frame(self.expdate_frame_name)
        self.element_sendkeys(expdate,By.XPATH,self.expdate_locator)
        self.switch_frame_default()

    def enter_cvc(self,cvc):
        self.switch_frame(self.cvc_frame_name)
        self.element_sendkeys(cvc,By.XPATH,self.cvc)
        self.switch_frame_default()

    def enter_postal(self,postal):
        self.switch_frame(self.postal_frame_name)
        self.element_sendkeys(postal,By.XPATH,self.postal_code_locator)
        self.switch_frame_default()

    def click_agree_to_terms(self):
        self.click_element(By.ID,self.agreement_checkbox_id)

    def check_confrim_button_Disabled(self):
        mybutton=self.getelement(By.ID,self.confirm_purchase_button_id)
        if (mybutton.is_enabled()):
            return False
        else:
            return True


    def enter_creditcard_details(self,method,cardnum,expdate,cvc,postal):
        self.select_payment_method(method)
        self.enter_cardnumber(cardnum)
        self.enter_expiration_date(expdate)
        self.enter_cvc(cvc)
        self.enter_postal(postal)


















