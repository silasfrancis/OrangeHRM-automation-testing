from selenium.common import ElementNotInteractableException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class PersonalDetails:
    my_info_xpath = "//span[normalize-space()='My Info']"
    first_name_xpath = "//input[@name='firstName']"
    middle_name_xpath = "//input[@name='middleName']"
    last_name_xpath = "//input[@name='lastName']"
    employee_id_xpath = "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/input[1]"
    drivers_license_xpath = "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[2]/div[1]/div[1]/div[2]/input[1]"
    license_expiry_date_xpath = "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]" #yyyy-dd-mm
    nationality_xpath = "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/i[1]"
    marital_status_xpath = "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/i[1]"
    dob_xpath = "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]"
    rd_gender_male_xpath = "//label[normalize-space()='Male']"
    rd_gender_female_xpath = "//label[normalize-space()='Female']"
    btn_save_details_xpath = "//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button[@type='submit'][normalize-space()='Save']"
    blood_type_xpath = "//div[@class='orangehrm-custom-fields']//div[@class='orangehrm-card-container']//form[@class='oxd-form']//div[@class='oxd-form-row']//div[@class='oxd-grid-3 orangehrm-full-width-grid']//div[@class='oxd-grid-item oxd-grid-item--gutters']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']"
    test_field_comment_xpath = "//div[@class='orangehrm-custom-fields']//div[@class='orangehrm-card-container']//form[@class='oxd-form']//div[@class='oxd-form-row']//div[@class='oxd-grid-3 orangehrm-full-width-grid']//div[@class='oxd-grid-item oxd-grid-item--gutters']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']"
    btn_custom_field_save_xpath = "//div[@class='orangehrm-custom-fields']//button[@type='submit'][normalize-space()='Save']"
    btn_add_attachments_xpath = "//button[normalize-space()='Add']"
    btn_browse_file_xpath = "//div[@class='oxd-file-button']"
    btn_upload_file_xpath = "//i[@class='oxd-icon bi-upload oxd-file-input-icon']"
    attachment_comment_xpath = "//textarea[@placeholder='Type comment here']"
    save_attachment_xpath = "//div[@class='orangehrm-attachment']//button[@type='submit'][normalize-space()='Save']"



    def __init__(self, driver):
        self.driver = driver

    def clickMyInfoMenu(self):
        self.driver.find_element(By.XPATH, self.my_info_xpath).click()

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.first_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.first_name_xpath).send_keys(fname)

    def setMiddleName(self, mname):
        self.driver.find_element(By.XPATH, self.middle_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.middle_name_xpath).send_keys(mname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.last_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.last_name_xpath).send_keys(lname)

    def setEmployeeId(self, emp_id):
        self.driver.find_element(By.XPATH, self.employee_id_xpath).clear()
        self.driver.find_element(By.XPATH, self.employee_id_xpath).send_keys(emp_id)

    def setDriversLicense(self, license):
        self.driver.find_element(By.XPATH, self.drivers_license_xpath).clear()
        self.driver.find_element(By.XPATH, self.drivers_license_xpath).send_keys(license)

    def setLicenseExp(self, yyyyddmm):
        self.driver.find_element(By.XPATH, self.license_expiry_date_xpath).clear()
        self.driver.find_element(By.XPATH, self.license_expiry_date_xpath).send_keys(yyyyddmm)

    def clickNationalitydrp(self, nationality):
        act = ActionChains(self.driver)
        self.driver.find_element(By.XPATH, self.nationality_xpath).click()
        target_locator = self.driver.find_element(By.XPATH, "//div[contains(text(),'-- Select --')]")
        target_item = nationality
        found = False

        while not found:
            act.key_down(Keys.ARROW_DOWN).perform()
            if target_locator.text == target_item:
                found = True
                act.key_down(Keys.ENTER).perform()


    def clickMaritalStatusdrp(self, status):
        self.driver.find_element(By.XPATH, self.marital_status_xpath).click()
        act = ActionChains(self.driver)
        target_locator = self.driver.find_element(By.XPATH, "//div[contains(text(),'-- Select --')]")
        target_item = status
        found = False

        while not found:
            act.key_down(Keys.ARROW_DOWN).perform()
            if target_locator.text == target_item:
                found = True
                act.key_down(Keys.ENTER).perform()



    def setDob(self, dob):
        self.driver.find_element(By.XPATH, self.dob_xpath).clear()
        self.driver.find_element(By.XPATH, self.dob_xpath).send_keys(dob)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.XPATH, self.rd_gender_male_xpath).click()
        elif gender == 'Female':
            self.driver.find_element(By.XPATH, self.rd_gender_female_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rd_gender_male_xpath)

    def clickOnBloodTypedrp(self, bloodtype):
        self.driver.find_element(By.XPATH, self.blood_type_xpath).click()
        act = ActionChains(self.driver)
        target_locator = self.driver.find_element(By.XPATH, "//div[contains(text(),'-- Select --')]")
        target_item = bloodtype
        found = False

        while not found:
            act.key_down(Keys.ARROW_DOWN).perform()
            if target_locator.text == target_item:
                found = True
                act.key_down(Keys.ENTER).perform()



    def testFieldComment(self, comment):
        self.driver.find_element(By.XPATH, self.test_field_comment_xpath).send_keys(comment)

    def addAttachmentFile(self, filepath):
        try:
            self.driver.find_element(By.XPATH, self.btn_add_attachments_xpath).click()
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.presence_of_element_located((By.XPATH, "//body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-attachment']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-3 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]")))
            element.send_keys(filepath)
        except ElementNotInteractableException:
            print("This element is not interactable through selenium(automation) as it is not visible in UI")
            pass

        # self.driver.find_element(By.XPATH, self.btn_browse_file_xpath).send_keys(filepath)

    def attachmentComment(self, comment):
        self.driver.find_element(By.XPATH, self.attachment_comment_xpath).send_keys(comment)

    def clickSaveDetails(self):
        self.driver.find_element(By.XPATH, self.btn_save_details_xpath).click()

    def clickSaveCustomFields(self):
        self.driver.find_element(By.XPATH, self.btn_custom_field_save_xpath).click()

    def clickSaveAttachment(self):
        self.driver.find_element(By.XPATH, self.save_attachment_xpath).click()








