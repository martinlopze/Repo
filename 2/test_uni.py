import unittest
import operaciones

class pruebas(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(operaciones.suma(6,3),9)
    def test_resta(self):
        self.assertEqual(operaciones.resta(6,3),3)
    def test_mul(self):
        self.assertEqual(operaciones.multiplicar(6,3),18)
    def test_div(self):
        self.assertEqual(operaciones.div(6,3),2)

if __name__=='__main__':
    unittest.main()