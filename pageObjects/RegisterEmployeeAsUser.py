import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait


class RegisterEmployeeAsUser:
    admin_xpath = "//span[normalize-space()='Admin']"
    add_user = "//button[normalize-space()='Add']"
    drp_user_role_xpath = "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]"
    user_role_admin_xpath = "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]//div[contains(text(),'Admin')]"
    user_role_ess_xpath = "//div[contains(text(),'ESS')]"
    select_status_xpath = "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]"
    enable_status_xpath = "//div[contains(text(),'Enabled')]"
    employee_name_xpath = "//input[@placeholder='Type for hints...']"
    username_xpath = "//div[@class='oxd-form-row']//div[@class='oxd-grid-2 orangehrm-full-width-grid']//div[@class='oxd-grid-item oxd-grid-item--gutters']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']"
    password_xpath = "//div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@type='password']"
    confirm_password_xpath = "//div[@class='oxd-grid-item oxd-grid-item--gutters']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@type='password']"
    save_user_btn = "//button[normalize-space()='Save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnAdmin(self):
        self.driver.find_element(By.XPATH, self.admin_xpath).click()

    def clickOnAddUser(self):
        self.driver.find_element(By.XPATH, self.add_user).click()

    def setUserRole(self, user_role):
        self.driver.find_element(By.XPATH, self.drp_user_role_xpath).click()
        act = ActionChains(self.driver)
        target_locator = self.driver.find_element(By.XPATH, "//div[contains(text(),'-- Select --')]")
        target_item = user_role
        found = False

        while not found:
            act.key_down(Keys.ARROW_DOWN).perform()
            if target_locator.text == target_item:
                found = True
                act.key_up(Keys.ENTER).perform()


    def selectStatus(self, stat):
        self.driver.find_element(By.XPATH, self.select_status_xpath).click()
        act = ActionChains(self.driver)
        target_locator = self.driver.find_element(By.XPATH, "//div[@class='oxd-select-text-input'][normalize-space()='-- Select --']")
        target_item = stat
        found = False

        while not found:
            act.key_down(Keys.ARROW_DOWN).perform()
            if target_locator.text == target_item:
                found = True
                act.key_up(Keys.ENTER).perform()

    def enterEmployeename(self):
        self.driver.find_element(By.XPATH, self.employee_name_xpath).send_keys('Fra')
        time.sleep(5)
        act = ActionChains(self.driver)
        act.key_down(Keys.ARROW_DOWN).perform()
        act.key_down(Keys.ENTER).perform()


    def setUsername(self, username):
        self.driver.find_element(By.XPATH, self.username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def confirmPassword(self, password):
        self.driver.find_element(By.XPATH, self.confirm_password_xpath).send_keys(password)

    def saveUser(self):
        self.driver.find_element(By.XPATH, self.save_user_btn).click()



