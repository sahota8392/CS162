import unittest
from LemonadeStand import LemonadeStand, MenuItem, InvalidSalesItemError, SalesForDay


class TestLemonadeStand(unittest.TestCase):

    def test_1(self):
        """Test the get method for get_name"""
        item1 = MenuItem('Lemonade', 0.5, 1.5)
        self.assertEqual(item1.get_name(), 'Lemonade')

    def test_2(self):
        """Test the LemonadeStand initial value method"""
        name_stand = LemonadeStand('Lemons R Us')
        self.assertEqual(name_stand.get_name(), 'Lemons R Us')

    def test_3(self):
        """Test the selling price"""
        item1 = MenuItem('Lemonade', 0.5, 1.5)
        self.assertAlmostEqual(item1.get_selling_price(), 1.5)

    def test_4(self):
        """Test the wholesale cost"""
        item1 = MenuItem('Lemonade', 0.5, 1.5)
        self.assertAlmostEqual(item1.get_wholesale_cost(), 0.5)

    def test_5(self):
        """Test the raise InvalidSalesItemError"""
        stand = LemonadeStand('Lemons R Us')
        item1 = MenuItem('lemonade', 0.5, 1.5)
        stand.add_menu_item(item1)

        day_0_sales = {
            'lemonade': 5,
            'cookie': 2
        }
        with self.assertRaises(InvalidSalesItemError):
            stand.enter_sales_for_today(day_0_sales)


if __name__ == '__main__':
    unittest.main()
