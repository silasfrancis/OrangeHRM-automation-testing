import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("*************** Starting HomePage Title Test ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        page_title = self.driver.title
        if page_title == "OrangeHRM":
            assert True
            self.logger.info("***************Home Page Title Test Passed ***************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.info("*************** Home Page Title Test Failed ***************")
            assert False
        self.logger.info("*************** Finished Home Page Title Test ***************")

    def test_login(self, setup):
        self.logger.info("*************** Starting Login Test ***************")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        page_title = self.driver.title
        if page_title == "OrangeHRM":
            assert True
            self.logger.info("*************** Login Test Passed ***************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.info("*************** Login Test Failed***************")
            assert False
        self.logger.info("*************** Finished Login Test ***************")
        self.logger.info("*************** Finished Test_001_Login ***************")
