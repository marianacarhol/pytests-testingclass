import unittest

# comentario 3 de prueba

def FizzBuzz(n):
    if n == 0:
        return 0
    # 3. both
    if (n % 3) == 0 and (n % 5) == 0:
        return "FizzBuzz"
    # 1. multiples of 3
    if (n % 3) == 0:
        return "Fizz"
    # 2. multiple of 5
    if (n % 5) == 0:
        return "Buzz"
    return n
    

# Mis pruebas usando TDD
# 1. Crear las preubas
class TestFizzBuzz(unittest.TestCase):
    # Create a function that returns "Fizz" for multiples of 3,
    # "Buzz" for multiples of 5, and "FizzBuzz" for multiples of both.
    # Return the number itself otherwise. Write tests covering edge 
    # cases: single numbers, multiples of 3, multiples of 5, multiples 
    # of 15, and numbers that are none of these.

    # a) Test TODOS los numeros que se nos ocurren
    # b) Test un subset de los numeros naturales
    #   b.1) Un 3
    #   b.2) 15
    #   b.3) pos muchos mas
    def testMultiple3(self):
        self.assertEqual(FizzBuzz(3), 'Fizz')
        self.assertEqual(FizzBuzz(9), 'Fizz')
        self.assertNotEqual(FizzBuzz(3000), 'Fizz')
        self.assertEqual(FizzBuzz(-3), 'Fizz')
        self.assertEqual(FizzBuzz(-69), 'Fizz')

    def testMultiple5(self):
        self.assertEqual(FizzBuzz(5), 'Buzz')
        self.assertEqual(FizzBuzz(25), 'Buzz')
        self.assertEqual(FizzBuzz(-50), 'Buzz')
        self.assertEqual(FizzBuzz(5555), 'Buzz')
        self.assertNotEqual(FizzBuzz(3), 'Buzz')

    def testBoth(self):
        self.assertEqual(FizzBuzz(15), 'FizzBuzz')
        self.assertEqual(FizzBuzz(-30), 'FizzBuzz')
        self.assertNotEqual(FizzBuzz(3), 'FizzBuzz')
        self.assertNotEqual(FizzBuzz(5), 'FizzBuzz')
        
    def testOthers(self):
        self.assertEqual(FizzBuzz(0), 0)
        self.assertEqual(FizzBuzz(67), 67)
        self.assertEqual(FizzBuzz(1), 1)
        self.assertEqual(FizzBuzz(69.69), 69.69)

    def testOtherTypes(self):
        with self.assertRaises(Exception):
            FizzBuzz("hola")

if __name__ == '__main__':
    unittest.main()

# python3 -m unittest test_fizzbuzz.py