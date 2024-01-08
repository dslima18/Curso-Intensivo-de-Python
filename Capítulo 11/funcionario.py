class Employee():
    def __init__(self, first_name, last_name, salario):
        self.first_name = first_name
        self.last_name = last_name
        self.salario = salario
    def give_raise(self,acrescimo=5000):
        self.salario += acrescimo