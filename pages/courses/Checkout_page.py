from base.selenium_common import SeleniumCommon
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains

class Checkout(SeleniumCommon):



    dropdown_button_locator="//button[@class='dropbtn minimal']"
    dropdown_paypal_method_locator="//div[@id='option-container']//span[@class='option-text'][contains(text(),'Paypal')]"
    dropdown_creditcard_method_locator="//div[@class='spc__custom_dropdown dropdown arrow-down']"
    #cardnumber_locator="// div[ @ id = 'root'] / form // input[ @ name = 'cardnumber']"
    cardnumber_locator="//*[@id='root']/form/span[2]/span/input"

    agreement_checkbox_id='agreed_to_terms_checkbox'

    expdate_locator="// div[ @ id = 'root'] / form // input[ @ name = 'exp-date']"

    cvc="// div[ @ id = 'root'] / form // input[ @ name = 'cvc']"
    postal_code_locator="// div[ @ id = 'root'] / form // input[ @ name = 'postal']"
    country_dropdown_locator_id="country_code_credit_card-cc"


    confirm_purchase_button_id="confirm-purchase"

    _credit_card_frame = '__privateStripeFrame8'
    _Expdate_frame = '__privateStripeFrame9'
    _cvc_frame = '__privateStripeFrame10'
    _zip_frame = '__privateStripeFrame11'

    def click_paypal(self):
        self.click_element(By.XPATH,self.dropdown_paypal_method_locator)

    def click_creditcard(self):
        self.click_element(By.XPATH,self.dropdown_creditcard_method_locator)


    def waitfor(self):
        wait=WebDriverWait(self.driver,10,poll_frequency=2,ignored_exceptions=[ElementNotVisibleException,NoSuchElementException,ElementNotSelectableException,ElementClickInterceptedException])
        wait.until(EC.element_to_be_clickable((By.XPATH,self.dropdown_button_locator)))
        element=self.driver.find_element(By.XPATH,self.dropdown_button_locator)
        action=ActionChains(self.driver)
        action.move_to_element(element).click().perform()
        action.move_to_element(element).perform()

    def scroll_to_button_and_click(self):
        element = self.driver.find_element(By.XPATH, self.dropdown_button_locator)
        self.scroll_to_element(element)
        element.click()






    def select_payment_method(self,method):

        myelement=self.getelement(By.XPATH,self.dropdown_locator)

    def select_payment_method(self,method):
        self.click_dropdown_button()
        if method=="cc":
            self.click_creditcard()
        else:
            self.click_paypal()


    def click_dropdown_button(self):
        self.click_element(By.XPATH,self.dropdown_button_locator)


    def enter_cardnumber(self,cardno):
        self.switch_frame(self._credit_card_frame)
        self.element_sendkeys(cardno,By.XPATH,self.cardnumber_locator)
        self.switch_frame_default()

    def enter_expiration_date(self,expdate):
        self.switch_frame(self._Expdate_frame)
        self.element_sendkeys(expdate,By.XPATH,self.expdate_locator)
        self.switch_frame_default()

    def enter_cvc(self,cvc):
        self.switch_frame(self._cvc_frame)
        self.element_sendkeys(cvc,By.XPATH,self.cvc)
        self.switch_frame_default()

    def enter_postal(self,postal):
        self.switch_frame(self._zip_frame)
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