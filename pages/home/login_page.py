from selenium.webdriver.common.by import By
from base.selenium_common import SeleniumCommon


class loginPage(SeleniumCommon):

    #locators
    login_link="Login"
    email_id="user_email"
    passwd_id="user_password"
    button_name="commit"
    invalid_login_error_locator="//div[@class='alert alert-danger']"

    def get_loginlink(self):
        return self.driver.find_element(By.LINK_TEXT,self.login_link)

    def get_email_id(self):
        return self.driver.find_element(By.ID,self.email_id)

    def get_password(self):
        return self.driver.find_element(By.ID,self.passwd_id)

    def get_button(self):
        return self.getelement(By.NAME,self.button_name)

    def get_invalid_login_message(self):
        return self.gettext(By.XPATH,self.invalid_login_error_locator)

    def click_login(self):
        self.get_loginlink().click()

    def enter_email(self,email):
        self.get_email_id().send_keys(email)

    def enter_password(self,passwd_id):
        self.get_password().send_keys(passwd_id)

    def click_button(self):
        self.get_button().click()

    def valid_login(self,email,password):
        self.click_login()
        self.enter_email(email)
        self.enter_password(password)
        self.click_button()

    def verify_successfull_login(self):
        pass




