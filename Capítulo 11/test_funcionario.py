import unittest
from funcionario import Employee

class TesteFuncionario(unittest.TestCase):
    def setUp(self):
        self.funcionario = Employee('Donato','Souza',3000)
    def test_give_default_raise(self):
        self.funcionario.give_raise()
        self.assertEqual(self.funcionario.salario, 8000)
    def test_give_custom_raise(self):
        self.funcionario.give_raise(3000)
        self.assertEqual(self.funcionario.salario, 6000)
unittest.main()