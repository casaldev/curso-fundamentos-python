from collections import namedtuple

class Employee:
    """Dados do funcionário"""
    def __init__(self, name, salary, dependents):
        self.name = name
        self.salary = salary
        self.dependents = dependents
        self.dependent_value = 189.59
        self.aliquot_inss = 0.11
        self.aliquot_irrf = 0.0
        self.parcel = 0.0

    def get_dependents_value(self):
        """Verifica a quantidade de dependentes para calculo do salário familia"""
        if self.dependents == 1:
            return self.dependent_value
        elif self.dependents >= 2:
            return self.dependents * self.dependent_value
        else:
            return 0.0

    def discount_inss(self):
        """Calcula e retorna o valor do desconto de INSS"""
        return self.salary * self.aliquot_inss
    
    def salary_base_irrf(self):
        """Calcula salário e retorna desconto de INSS"""
        return self.salary - self.discount_inss()

    def discount_dependents(self):
        """Calcula o salário família pela quantidade de dependentes"""
        return self.salary_base_irrf() - self.get_dependents_value()

    def discount_aliquot_irrf(self):
        """Calcula o IRRF com a porcentagem e parcela a deduzir"""
        if self.salary <= 1903.38:
            self.aliquot_irrf = 0.0
            self.parcel = 0.0
        elif self.salary <= 2826.66:
            self.aliquot_irrf = 0.075
            self.parcel = 142.80
        elif self.salary <= 3751.05:
            self.aliquot_irrf = 0.15
            self.parcel = 354.80
        elif self.salary <= 4664.68:
            self.aliquot_irrf = 0.22
            self.parcel = 636.13
        else:
            self.aliquot_irrf = 0.275
            self.parcel = 869.36
        return (self.discount_dependents() * self.aliquot_irrf) - self.parcel 

    def liquid_salary(self):
        """Calcula o salário líquido com o desconto de INSS e IRRF"""
        return self.salary - self.discount_inss() - self.discount_aliquot_irrf()




Employees = namedtuple('Employees', 'name, salary, dependents')

import csv
for emp in map(Employees._make, csv.reader(open("aulas\employees.csv", "rt",  encoding='utf-8-sig'))):
    # print(emp[0], emp[1])
    irrf_2020 = Employee(emp.name, float(emp.salary), int(emp.dependents))
    print(irrf_2020 .liquid_salary()) 
    print(irrf_2020 .discount_aliquot_irrf())

    
        

