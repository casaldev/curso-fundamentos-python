class Employee:
    """Dados do funcionário"""
    def __init__(self, name, salary, dependents):
        self.name = name
        self.salary = salary
        self.dependents = dependents
        self.dependent_value = 189.59
    

class IRRF(Employee):
    def __init__(self, name, salary, dependents, aliquot_inss, aliquot_irrf, parcel):
        super().__init__(name, salary, dependents)
        self.aliquot_inss = aliquot_inss
        self.aliquot_irrf = aliquot_irrf
        self.parcel = parcel

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
        return (self.discount_dependents() * self.aliquot_irrf) - self.parcel 

    def liquid_salary(self):
        """Calcula o salário líquido com o desconto de INSS e IRRF"""
        return self.salary - self.discount_inss() - self.discount_aliquot_irrf()



irrf_2020 = IRRF('Julio', 2900.00, 1, 0.11, 0.075, 142.80)
print(irrf_2020 .liquid_salary()) 
print(irrf_2020 .discount_aliquot_irrf())

    
        

