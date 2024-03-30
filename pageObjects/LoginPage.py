from selenium.webdriver.common.by import By

class LoginPage:
    textbox_username_xpath = "//input[@placeholder='Username']"
    textbox_password_xpath = "//input[@placeholder='Password']"
    button_login_xpath = "//button[@type='submit']"
    drp_button_xpath = "//li[@class='--active oxd-userdropdown']"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self,username):
        # self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def setPassword(self,password):
        # self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.drp_button_xpath).click()
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()


