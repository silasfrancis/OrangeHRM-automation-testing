# Testing OrangeHRM Demo Application
This project involves the testing of the PIM Module on the OrangeHRM Demo Platform using the Pytest FrameWork

## Features
- Page Object Model
- HTML Reports
- Data Driven Testing
- Multiple Browsers Support
- Parallel Testing

##Test Scenarios
- Login into the OrangeHRM demo site: https://opensource-demo.orangehrmlive.com/
- Create Employee
- Register Employee as an Admin
- Login as the new employee
- Update Employee Details
- Search Employee by Name
- Search Employee by Id
- Login via test Data in xlsx file
- Create employee using test Data in xlsx file

## Languages, libraries and tools used
- Python
- Pytest
- pytest-html
- pytest-xdist
- Openpyxl
- Allure-pytest
- Pycharm

## Installation
To install the required libraries for distributed testing, run the following command in your terminal:
```bash
pip install -U pytest
pip install pytest-html
pip install pytest-xdist
pip install openpyxl
pip install allure-pytest
```

## Test Execution
### 1. Tests could be executed by running the following commands:
#### Chrome Browser:
```bash
pytest -s -v --html=Reports/report_login.html testCases/test_login.py --browser chrome
pytest -s -v --html=Reports/report_createEmployee.html testCases/test_createEmployee.py --browser chrome
pytest -s -v --html=Reports/report_registerEmp_asUser.html testCases/test_registerEmployeeasUser.py --browser chrome
pytest -s -v --html=Reports/report_updateEmpDetails.html testCases/test_UpdateEmployeeDetails.py --browser chrome
pytest -s -v --html=Reports/report_searchEmp_byName.html testCases/test_searchEmployeeByName.py --browser chrome
pytest -s -v --html=Reports/report_SearchEmp_byId.html testCases/test_searchEmployeeById.py --browser chrome
pytest -s -v --html=Reports/report_test_loginDDT.html testCases/test_loginDDT.py --browser chrome
pytest -s -v --html=Reports/report_createEmp_DDT.html testCases/test_createEmployeeDDT.py --browser chrome
```
#### Edge: 
```bash
pytest -s -v --html=Reports/report_login.html testCases/test_login.py --browser edge
pytest -s -v --html=Reports/report_createEmployee.html testCases/test_createEmployee.py --browser edge
pytest -s -v --html=Reports/report_registerEmp_asUser.html testCases/test_registerEmployeeasUser.py --browser edge
pytest -s -v --html=Reports/report_updateEmpDetails.html testCases/test_UpdateEmployeeDetails.py --browser edge
pytest -s -v --html=Reports/report_searchEmp_byName.html testCases/test_searchEmployeeByName.py --browser edge
pytest -s -v --html=Reports/report_SearchEmp_byId.html testCases/test_searchEmployeeById.py --browser edge
pytest -s -v --html=Reports/report_test_loginDDT.html testCases/test_loginDDT.py --browser edge
pytest -s -v --html=Reports/report_createEmp_DDT.html testCases/test_createEmployeeDDT.py --browser edge
```
#### Firefox: 
```
pytest -s -v --html=Reports/report_login.html testCases/test_login.py --browser firefox
pytest -s -v --html=Reports/report_createEmployee.html testCases/test_createEmployee.py --browser firefox
pytest -s -v --html=Reports/report_registerEmp_asUser.html testCases/test_registerEmployeeasUser.py --browser firefox
pytest -s -v --html=Reports/report_updateEmpDetails.html testCases/test_UpdateEmployeeDetails.py --browser firefox
pytest -s -v --html=Reports/report_searchEmp_byName.html testCases/test_searchEmployeeByName.py --browser firefox
pytest -s -v --html=Reports/report_SearchEmp_byId.html testCases/test_searchEmployeeById.py --browser firefox
pytest -s -v --html=Reports/report_test_loginDDT.html testCases/test_loginDDT.py --browser firefox
pytest -s -v --html=Reports/report_createEmp_DDT.html testCases/test_createEmployeeDDT.py --browser firefox
```
### 2. Running the Batch File located in this directory:
   Test can also be executed by running the batch file located in this directory.
   Double click on in or switch directory to this directory on command prompt and run the batch file from there
   - N/B: The batch file will run on default browser for now, but can be edited .
   



