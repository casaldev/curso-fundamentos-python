from collections import namedtuple
Employees = namedtuple('Employees', 'name, salary, dependents')

import csv
for emp in map(Employees._make, csv.reader(open("aulas\employees.csv", "rt",  encoding='utf-8-sig'))):
    # print(emp[0], emp[1])
    print(emp.name, emp.salary)