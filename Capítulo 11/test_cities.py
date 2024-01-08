import unittest
from city_functions import cidade_pais

class CidadePaisTestCase(unittest.TestCase):
#    def test_city_country(self):
#        formatted_name = cidade_pais('santiago','chile',5000000)
#        self.assertEqual(formatted_name, 'Santiago, Chile - População 5000000')
    def test_city_country_population(self):
        formatted_name = cidade_pais('santiago','chile','população=5000000')
        self.assertEqual(formatted_name, 'Santiago, Chile - População=5000000')
unittest.main()