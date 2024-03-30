import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils
import time

class Test_007_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info('**********Test_007_DDT_Login*********')
        self.logger.info('*****************Verifying Login DDT test*****************************')
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = ExcelUtils.getRowCount(self.path, 'Login Data')
        list_status = []

        for r in range(2,self.rows+1):
            self.username = ExcelUtils.readData(self.path, 'Login Data', r, 1)
            self.password = ExcelUtils.readData(self.path, 'Login Data', r, 2)
            self.exp = ExcelUtils.readData(self.path, 'Login Data', r, 3)

        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)

        act_title = self.driver.title
        exp_title = "OrangeHRM"
        if act_title == exp_title :
            if self.exp == 'Pass':
                self.logger.info('******Passed*******')
                self.lp.clickLogout()
                list_status.append("Pass")
            elif self.exp == 'Fail':
                self.logger.info('******Failed*******')
                self.lp.clickLogout()
                list_status.append("Fail")

        elif act_title != exp_title:
            if self.exp == 'Pass':
                self.logger.info('******Failed*******')
                self.lp.clickLogout()
                list_status.append("Pass")
            elif self.exp == 'Fail':
                self.logger.info('******Passed*******')
                self.lp.clickLogout()
                list_status.append("Pass")

        if "Fail" not in list_status:
            self.logger.info("****Login DDT test passed*****")
            self.driver.close()
            assert True
        else:
            self.logger.info("****Login DDT test failed*****")
            self.driver.close()
            assert False

        self.logger.info("****** End of Login DDT Test ********")
        self.logger.info("****** Completed Test_007_DDT_Login ********")



