import unittest

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.discount_percent = 0.0

    def add_item(self, name, price, qty=1):
        if price < 0 or qty <= 0:
            raise ValueError("precio/cantidad inválidos, debe de ser un valor arriba de cero")
        for item in self.items:
            if item[0] == name:
                item[2] += qty
                return
        self.items.append([name, float(price), qty])

    def remove_item(self, name, qty=1):
        if qty <= 0:
            raise ValueError("cantidad inválida, debe de ser un valor arriba de cero")
        for item in self.items:
            if item[0] == name:
                if qty > item[2]:
                    raise ValueError("excede la cantidad")
                item[2] -= qty
                if item[2] == 0:
                    self.items.remove(item)
                return
        raise ValueError("no existe este item")
    
    def discount(self, percent):
        self.discount_percent = float(percent)

    def total(self):
        s = 0.0
        for name, price, qty in self.items: 
            s += price * qty
        return s * (1 - self.discount_percent / 100.0)
    
cart = ShoppingCart()

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def testEmptyCart(self):
        self.assertEqual(self.cart.total(), 0.0)

    def testAddItem(self):
        self.cart.add_item("Maruchan", 8.0)
        self.cart.add_item("Maruchan", 8.0, qty=2) 
        self.assertEqual(self.cart.items[0], ["Maruchan", 8.0, 3])
        self.assertEqual(self.cart.total(), 24.0)

    def testAddItemInvalid(self):
        self.assertRaises(ValueError, self.cart.add_item, "prueba", -1.0)
        self.assertRaises(ValueError, self.cart.add_item, "prueba", 1.0, qty=0)
        self.assertRaises(ValueError, self.cart.add_item, "prueba", 1.0, qty=-2)

    def testRemoveItems(self):
        self.cart.add_item("Boing de Mango", 5.0, qty=2)
        self.cart.remove_item("Boing de Mango", qty=1)
        self.assertEqual(self.cart.items[0], ["Boing de Mango", 5.0, 1])
        self.cart.remove_item("Boing de Mango", qty=1)
        self.assertEqual(self.cart.items, [])
        self.assertEqual(self.cart.total(), 0.0)

    def testRemoveItemsInvalid(self):
        self.assertRaises(ValueError, self.cart.remove_item, "no existo")
        self.cart.add_item("Sponch", 3.0, qty=1)
        self.assertRaises(ValueError, self.cart.remove_item, "Sponch", 2)
        self.assertRaises(ValueError, self.cart.remove_item, "Sponch", 0)
        self.assertRaises(ValueError, self.cart.remove_item, "Sponch", -1)

    def test_discount_applies(self):
        self.cart.add_item("Churrumais", 50.0, qty=4)  
        self.cart.discount(10)                
        self.assertEqual(self.cart.total(), 180.0)

if __name__ == '__main__':
    unittest.main()
