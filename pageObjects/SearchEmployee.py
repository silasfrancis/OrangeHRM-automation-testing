from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By

class SearchEmployee:
    pim_xpath = "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='PIM']"
    employee_list_xpath = "//a[normalize-space()='Employee List']"
    employee_name_xpath = "//div[@class='oxd-grid-4 orangehrm-full-width-grid']//div[1]//div[1]//div[2]//div[1]//div[1]//input[1]"
    employee_id_xpath = "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']"
    search_btn_xpath = "//button[normalize-space()='Search']"
    records_table_xpath = "//div[@role='table']"
    table_header_xpath= "//div[@class='oxd-table-row oxd-table-row--with-border']"
    table_body_xpath= "//div[@class='oxd-table-row oxd-table-row--with-border oxd-table-row--clickable']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnPIM(self):
        self.driver.find_element(By.XPATH, self.pim_xpath).click()

    def clickOnEmployeeList(self):
        self.driver.find_element(By.XPATH, self.employee_list_xpath).click()

    def inputEmployeeName(self, emp_name):
        self.driver.find_element(By.XPATH, self.employee_name_xpath).send_keys(emp_name)

    def inputEmployeeId(self, emp_id):
        self.driver.find_element(By.XPATH, self.employee_id_xpath).send_keys(emp_id)

    def clickSearchbtn(self):
        self.driver.find_element(By.XPATH, self.search_btn_xpath).click()

    def searchEmployeeByUsername(self, FandM_name, lname):
            table = self.driver.find_element(By.XPATH, self.table_body_xpath)
            fname_and_mname = table.find_element(By.XPATH, "//div[@class='oxd-table-row oxd-table-row--with-border oxd-table-row--clickable']//div[3]").text
            if fname_and_mname == FandM_name:
                assert True
            lastname = table.find_element(By.XPATH, "//div[@class='oxd-table-row oxd-table-row--with-border oxd-table-row--clickable']//div[4]").text
            if lastname == lname:
                assert True
            else:
                assert False


    def searchEmployeeByID(self, emp_id):
        table = self.driver.find_element(By.XPATH, self.table_body_xpath)
        id = table.find_element(By.XPATH, "//div[@class='oxd-table-row oxd-table-row--with-border oxd-table-row--clickable']//div[2]").text
        if id == emp_id:
            assert True
        else:
            assert True

