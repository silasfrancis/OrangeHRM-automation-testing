import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.CreateEmployee import CreateEmployee
from pageObjects.PersonalDetails import PersonalDetails
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils
import time

class Test_008_DDT_CreateEmployee:
    baseURL = ReadConfig.getApplicationURL()
    login_path = ".//TestData/LoginData.xlsx"
    create_emp_path = ".//TestData/CustomerInfo.xlsx"
    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info('********** Test_008_DDT_CreateEmployee *********')
        self.logger.info('*****************Verifying Login DDT test*****************************')
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.username = ExcelUtils.readData(self.login_path, 'Login Data', 2, 1)
        self.password = ExcelUtils.readData(self.login_path, 'Login Data', 2, 2)

        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info('************ Login Successful ************')

        self.logger.info("**************** Creating Employee ****************")
        self.create_emp = CreateEmployee(self.driver)
        self.create_emp.clickOnPIM()
        self.create_emp.clickAddEmployee()

        self.fname = ExcelUtils.readData(self.create_emp_path, 'Sheet1', 2, 1)
        self.mname = ExcelUtils.readData(self.create_emp_path, 'Sheet1', 2, 2)
        self.lname = ExcelUtils.readData(self.create_emp_path, 'Sheet1', 2, 3)
        self.create_emp.setFirstname(self.fname)
        self.create_emp.setMiddlename(self.mname)
        self.create_emp.setLastname(self.lname)
        self.create_emp.saveEmployee()
        self.logger.info("***************** Employee Created ***************")
        self.logger.info("***************** Test_008_DDT_CreateEmployee Successful ***************")
        self.driver.close()




