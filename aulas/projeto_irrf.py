

class Employee:
    """Dados do funcionário"""
    def __init__(self, name, salary, dependents):
        self.name = name
        self.salary = salary
        self.dependents = dependents
        self.dependent_value = 189.59
    
    def check_dependents(self):
        if self.dependents == 1:
            return self.dependent_value
        elif self.dependents >= 2:
            return self.dependents * self.dependent_value
        else:
            return "Você não tem direito ao salário família"
       
d1 = Employee("Julio", 2000.00, 0)
print(d1.check_dependents())

class INSS(Employee):
    """Define a aliquota do INSS"""
    def __init__(self, name, salary, dependents, aliquot):
        super().__init__(name, salary, dependents)
        self.aliquot = aliquot

    def subtract(self):
        return self.salary * self.aliquot

    def basis(self):
        return self.salary - self.subtract()

i1 = INSS('Julio', 2900.00, 1, 0.11)
print(i1.subtract())
print(i1.basis())

class IRRF(Employee):
    def __init__(self, name, salary, dependents, aliquot, parcel):
        super().__init__(name, salary, dependents)
        self.__aliquot = aliquot
        self.parcel = parcel

  
        
        




# income = 2826.65
# dependent = 1
# INSS = 0.11
# if income <= 1903.98:
#     aliquot = 0.0       # Bloco #1
# elif income <= 2826.65:
#     c_inss = income * INSS
#     b_irrf = income - c_inss
#     v_dependent = 189.59
#     s_b_irrf = b_irrf - v_dependent
#     aliquot = 0.075 
#     d_aliquot = abs((s_b_irrf * aliquot) - v_dependent)    # Bloco #2
#     s_liquido = income - c_inss - d_aliquot
#     print('Meu salario líquido será de', s_liquido, 'e meu desconto do IRPF será de', d_aliquot )
# elif income <= 3751.05:
#     income_base = 2826.65
#     aliquot = 0.15       # Bloco #3
# elif income <= 4664.68:
#     aliquot = 0.225
#     income_base = 3751.05
# else:  
#     income_base = 4664.68   
#     aliquot = 0.275     # # Bloco #4
