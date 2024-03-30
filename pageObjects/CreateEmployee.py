from selenium.webdriver.common.by import By

class CreateEmployee:
    pim_xpath = "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='PIM']"
    add_employee_xpath = "//a[normalize-space()='Add Employee']"
    employee_firstname = "//input[@placeholder='First Name']"
    employee_middlename = "//input[@placeholder='Middle Name']"
    employee_lastname = "//input[@placeholder='Last Name']"
    save_employee_xpath = "//button[normalize-space()='Save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnPIM(self):
        self.driver.find_element(By.XPATH, self.pim_xpath).click()

    def clickAddEmployee(self):
        self.driver.find_element(By.XPATH, self.add_employee_xpath).click()

    def setFirstname(self, fname):
        self.driver.find_element(By.XPATH, self.employee_firstname).send_keys(fname)

    def setMiddlename(self, mname):
        self.driver.find_element(By.XPATH, self.employee_middlename).send_keys(mname)

    def setLastname(self, lname):
        self.driver.find_element(By.XPATH, self.employee_lastname).send_keys(lname)

    def saveEmployee(self):
        self.driver.find_element(By.XPATH, self.save_employee_xpath).click()





