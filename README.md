# Testing OrangeHRM Demo Application
This project involves the testing of the PIM Module on the OrangeHRM Demo Platform using the Pytest FrameWork

## Features
- Page Object Model
- HTML Reports
- Data Driven Testing
- Logging
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
## Test Execution
Test Execution commands can be found in the run.bat file located in this respository 

#### Browser Supported:
- Chrome (--browser chrome)
- Edge (--browser edge)
- Firefox (--browser firefox)
  
```bash
e.g.
pytest -s -v --html=Reports/report_login.html testCases/test_login.py --browser chrome
```
> This will run test on Chrome Browser

_N/B: If no browser is specified test will be executed on chrome_

   



