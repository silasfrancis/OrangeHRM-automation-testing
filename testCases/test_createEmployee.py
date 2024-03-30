import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.CreateEmployee import CreateEmployee
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_002_CreateEmployee:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_createemployee(self, setup):
        self.logger.info("**************** Starting Creating Employee Test ****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info('************ Login Successful ************')

        self.logger.info("**************** Creating Employee ****************")

        self.create_emp = CreateEmployee(self.driver)
        self.create_emp.clickOnPIM()
        self.create_emp.clickAddEmployee()
        self.create_emp.setFirstname("Francis")
        self.create_emp.setMiddlename("Samuel")
        self.create_emp.setLastname("Silas")
        self.create_emp.saveEmployee()
        self.logger.info("***************** Employee Created ***************")
        self.logger.info("***************** Test_002_CreateEmployee Successful ***************")







