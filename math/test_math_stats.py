import unittest
from math_stats import *

class TestStats(unittest.TestCase):
    # ------------- ADD --------------

    def test_add(self):
        #1: setup
        a, b = 2, 12

        #2: expected outputs
        res = 14

        #3: assert
        self.assertEqual(
            add(a, b),
            res,
            "Error" 
        )

    def test_add2(self):
        self.assertEqual(add(1, -3), -2)

    # ------------- SUBTRACT --------------
        
    def test_subtract(self):
        #1: setup
        a, b = 12, 2

        #2: expected outputs
        res = 10

        #3: assert
        self.assertEqual(
            subtract(a, b),
            res,
            "Error" 
        )

    def test_subtract2(self):
        self.assertEqual(subtract(1, -3), 4)

    # ------------- MULTIPLY --------------
        
    def test_multiply(self):
        #1: setup
        a, b = 12, 2

        #2: expected outputs
        res = 24

        #3: assert
        self.assertEqual(
            multiply(a, b),
            res,
            "Error" 
        )

    def test_multiply2(self):
        self.assertEqual(multiply(1, -3), -3)

    # ------------- DIVIDE --------------

    def test_divide(self):
        #1: setup
        a, b = 10, 2

        #2: expected outputs
        res = 5
        
        #3: assert
        self.assertEqual(
            divide(a, b),
            res,
            "Error"
        )

    def test_divide2(self):
        self.assertEqual(divide(-9, 3), -3)

    def test_divide3(self):
        with self.assertRaises(ValueError):
            divide(1, 0)

    # ------------- POWER --------------

    def test_power(self):
        self.assertEqual(power(1, 2), 1)
        self.assertEqual(power(2, 2), 4)
        self.assertEqual(power(2, 0), 1)
        self.assertEqual(power(2, -1), 0.5)
        self.assertEqual(power(5, -3), 1/125)
        self.assertAlmostEqual(power(3, -1), 0.33, delta=0.01)

    # ------------- SQUARE ROOT --------------

    def test_square_root(self):
        #1: setup
        n = 9

        #2: expected outputs
        res = 3

        #3: assert
        self.assertEqual(
            square_root(n),
            res,
            "Error"
        )

    def test_square_root2(self):
        self.assertAlmostEqual(square_root(2), 1.414213562, places=6)

    def test_square_root3(self):
        with self.assertRaises(ValueError):
            square_root(-1)
      
    # ------------- ABSOLUTE VALUE --------------

    def test_absolute_value(self):
        #1: setup
        n = -7
        #2: expected outputs
        res = 7
        #3: assert
        self.assertEqual(
            absolute_value(n),
            res,
            "Error"
        )

    def test_absolute_value2(self):
        self.assertEqual(absolute_value(5), 5)

    # ------------- MEAN --------------

    def test_mean(self):
        #1: setup
        data = [1, 2, 3, 4]

        #2: expected outputs
        res = 2.5

        #3: assert
        self.assertEqual(
            mean(data),
            res,
            "Error"
        )

    def test_mean2(self):
        self.assertEqual(mean([5]), 5.0)

    def test_mean3(self):
        with self.assertRaises(ValueError):
            mean([])

    # ------------- MEDIAN --------------

    def test_median(self):
        #1: setup
        data = [1, 3, 2, 4]

        #2: expected outputs
        res = 2.5

        #3: assert
        self.assertEqual(
            median(data),
            res,
            "Error"
        )

    def test_median2(self):
        self.assertEqual(median([3, 1, 2]), 2)

    def test_median3(self):
        with self.assertRaises(ValueError):
            median([])

    # ------------- MODE --------------

    def test_mode(self):
        #1: setup
        data = [1, 1, 2, 3]

        #2: expected outputs
        res = 1

        #3: assert
        self.assertEqual(
            mode(data),
            res,
            "Error"
        )

    def test_mode2(self):
        self.assertEqual(mode([1, 1, 2, 2, 3]), [1, 2])

    def test_mode3(self):
        with self.assertRaises(ValueError):
            mode([])

    # ------------- VARIANCE --------------

    def test_variance(self):
        #1: setup
        data = [1, 2, 3, 4]

        #2: expected outputs
        res = 1.25

        #3: assert
        self.assertAlmostEqual(
            variance(data),
            res,
            places=6
        )

    def test_variance2(self):
        self.assertEqual(variance([5, 5, 5]), 0.0)

    def test_variance3(self):
        with self.assertRaises(ValueError):
            variance([])

    # ------------- STANDARD DEVIATION --------------

    def test_standard_deviation(self):
        #1: setup
        data = [1, 2, 3, 4]

        #2: expected outputs (sqrt(1.25))
        res = 1.118033988749895

        #3: assert
        self.assertAlmostEqual(
            standard_deviation(data),
            res,
            places=6
        )

    def test_standard_deviation2(self):
        self.assertEqual(standard_deviation([5, 5, 5]), 0.0)

    def test_standard_deviation3(self):
        with self.assertRaises(ValueError):
            standard_deviation([])

    # ------------- IS EVEN --------------

    def test_is_even(self):
        #1: setup
        n = 12

        #2: expected outputs
        res = True

        #3: assert
        self.assertEqual(
            is_even(n),
            res,
            "Error"
        )

    def test_is_even2(self):
        self.assertFalse(is_even(-3))

    # ------------- IS PRIME --------------

    def test_is_prime(self):
        #1: setup
        n = 13

        #2: expected outputs
        res = True

        #3: assert
        self.assertEqual(
            is_prime(n),
            res,
            "Error"
        )

    def test_is_prime2(self):
        self.assertFalse(is_prime(1))

    # ------------- FACTORIAL --------------

    def test_factorial(self):
        #1: setup
        n = 5

        #2: expected outputs
        res = 120

        #3: assert
        self.assertEqual(
            factorial(n),
            res,
            "Error"
        )

    def test_factorial2(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial3(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    # ------------- GCD --------------

    def test_gcd(self):
        #1: setup
        a, b = 54, 24

        #2: expected outputs
        res = 6

        #3: assert
        self.assertEqual(
            gcd(a, b),
            res,
            "Error"
        )

    def test_gcd2(self):
        self.assertEqual(gcd(-8, 12), 4)

# so it runs when running the file
if __name__ == '__main__':
    unittest.main()