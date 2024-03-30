import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchEmployee import SearchEmployee
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_005_SearchEmployeeByName:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_searchemployeebyname(self, setup):
        self.logger.info("**************** Starting Search Employee Test****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info('************ Login Successful ************')

        self.logger.info("**************** Searching Employee By Name ****************")

        self.search_emp = SearchEmployee(self.driver)
        self.search_emp.clickOnPIM()
        self.search_emp.clickOnEmployeeList()
        self.search_emp.inputEmployeeName("Francis Samuel Silas")
        self.search_emp.clickSearchbtn()
        self.search_emp.searchEmployeeByUsername("Francis Samuel", "Silas")
        self.logger.info("*************** Search Successful ****************")

