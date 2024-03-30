import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.PersonalDetails import PersonalDetails
from utilities.readProperties import ReadConfigUser
from utilities.customLogger import LogGen


class Test_004_UpdateEmployeeDetails:
    baseURL = ReadConfigUser.getApplicationURL()
    username = ReadConfigUser.getUsername()
    password = ReadConfigUser.getPassword()

    logger = LogGen.loggen()

    def test_updatepersonaldetails(self, setup):
        self.logger.info("**************** Starting Personal Details Test****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info('************ Login Successful ************')

        self.logger.info("****************Editing Personal Details ****************")

        self.pdetails = PersonalDetails(self.driver)
        self.pdetails.clickMyInfoMenu()
        self.pdetails.setDriversLicense("ABC-1234-5678")
        self.pdetails.setLicenseExp("2024-09-11")
        self.pdetails.clickNationalitydrp('Nigerian')
        self.pdetails.clickMaritalStatusdrp('Single')
        self.pdetails.setDob("2002-07-05")
        self.pdetails.setGender('Male')
        self.pdetails.clickSaveDetails()
        self.logger.info("*************** Edit Successful ****************")
        self.driver.close()

    def test_updatecustomfield(self, setup):
        self.logger.info("**************** Starting Custom Field Test****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info('************ Login Successful ************')

        self.logger.info("****************Editing Custom Field ****************")

        self.custom = PersonalDetails(self.driver)
        self.custom.clickMyInfoMenu()
        self.custom.clickOnBloodTypedrp('O+')
        self.custom.testFieldComment("This is test")
        self.custom.clickSaveCustomFields()
        self.driver.close()


    def test_addattachment(self, setup):
        self.logger.info("**************** Starting Attachment Test****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info('************ Login Successful ************')

        self.logger.info("**************** Adding Attachment ****************")

        self.addatch = PersonalDetails(self.driver)
        self.addatch.clickMyInfoMenu()
        self.addatch.addAttachmentFile(".\\OrangeHRM\\test.png")
        self.addatch.attachmentComment("This is a test...")
        self.addatch.clickSaveAttachment()
        self.driver.save_screenshot(".\\Screenshots\\" + "Test_004_Element_interactable_through_Selenium.png")
        self.driver.close()









