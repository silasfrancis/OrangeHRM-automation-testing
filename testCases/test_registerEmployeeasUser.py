import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.RegisterEmployeeAsUser import RegisterEmployeeAsUser
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_003_RegisterEmployeeAsUser:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_resgisterempasuser(self, setup):
        self.logger.info("**************** Starting Registering Employee as UserTest ****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info('************ Login Successful ************')

        self.logger.info("**************** Registering Employee as User ****************")

        self.reg_emp = RegisterEmployeeAsUser(self.driver)
        self.reg_emp.clickOnAdmin()
        self.reg_emp.clickOnAddUser()
        self.reg_emp.setUserRole("Admin")
        self.reg_emp.selectStatus("Enabled")
        self.reg_emp.enterEmployeename()
        self.reg_emp.setUsername("Admin7812")
        self.reg_emp.setPassword("admin7812")
        self.reg_emp.confirmPassword("admin7812")
        self.reg_emp.saveUser()



