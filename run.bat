pytest -s -v --html=Reports/report_login.html testCases/test_login.py
pytest -s -v --html=Reports/report_createEmployee.html testCases/test_createEmployee.py
pytest -s -v --html=Reports/report_registerEmp_asUser.html testCases/test_registerEmployeeasUser.py
pytest -s -v --html=Reports/report_updateEmpDetails.html testCases/test_UpdateEmployeeDetails.py
pytest -s -v --html=Reports/report_searchEmp_byName.html testCases/test_searchEmployeeByName.py
pytest -s -v --html=Reports/report_SearchEmp_byId.html testCases/test_searchEmployeeById.py
pytest -s -v --html=Reports/report_test_loginDDT.html testCases/test_loginDDT.py
pytest -s -v --html=Reports/report_createEmp_DDT.html testCases/test_createEmployeeDDT.py