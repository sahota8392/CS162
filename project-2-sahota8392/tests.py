import unittest
from LemonadeStand import MenuItem, SalesForDay, LemonadeStand, InvalidSalesItemError


class TestLemonadeStand(unittest.TestCase):
    def setUp(self):
        pass

    def test_0(self):
        """testing LemonadeStand get_name"""
        stand = LemonadeStand('Lemons R Us')
        self.assertGreater(len(stand.get_name()), 0, msg="LemonadeStand.get_name() failed: -2")

    def test_1(self):
        """make a stand, add a couple of menu items, record a day's sales, check profit for one menu item"""
        stand = LemonadeStand('Lemons R Us')
        item1 = MenuItem('lemonade', .5, 1.5)
        item2 = MenuItem('cookie', .2, 1)
        stand.add_menu_item(item1)
        stand.add_menu_item(item2)
        day0 = {
            'lemonade': 5,
            'cookie': 2
        }
        stand.enter_sales_for_today(day0)
        lemonade_profit = stand.total_profit_for_menu_item('lemonade')
        self.assertAlmostEqual(lemonade_profit, 5.0,
                               msg=f'\nExpected value: 5.0 \nValue from your code: {lemonade_profit}')

    def test_2(self):
        """test whether InvalidSalesItemError is raised if an item reported sold doesn't match any item in the menu"""
        item1 = MenuItem('lemonade', .5, 1.5)
        item2 = MenuItem('cookie', .2, 1)
        stand = LemonadeStand('Lemons R Us')
        stand.add_menu_item(item1)
        stand.add_menu_item(item2)
        day0 = {
            'lemonade': 3,
            'cookie': 5
        }
        day1 = {
            'lemonade': 5,
            'cupcake': 2
        }
        stand.enter_sales_for_today(day0)
        with self.assertRaises(InvalidSalesItemError):
            stand.enter_sales_for_today(day1)

    def test_3(self):
        """Testing total_sales_for_menu_item()"""
        stand = LemonadeStand('Lemons R Us')
        item1 = MenuItem('lemonade', 0.5, 1.5)
        item2 = MenuItem('cookie', 0.3, 0.75)
        item3 = MenuItem('hot chocolate', 0.2, 1)
        stand.add_menu_item(item1)
        stand.add_menu_item(item2)
        stand.add_menu_item(item3)
        day0 = {
            'lemonade': 5,
            'cookie': 2
        }
        day1 = {
            'cookie': 6,
            'lemonade': 8
        }
        day2 = {
            'hot chocolate': 4,
            'lemonade': 7,
            'cookie': 4
        }
        stand.enter_sales_for_today(day0)
        stand.enter_sales_for_today(day1)
        stand.enter_sales_for_today(day2)
        lemonade_sales = stand.total_sales_for_menu_item('lemonade')
        cookie_sales = stand.total_sales_for_menu_item('cookie')
        hot_chocolate_sales = stand.total_sales_for_menu_item('hot chocolate')
        self.assertAlmostEqual(lemonade_sales, 20, msg=f'\nExpected value: 20 \nValue from your code: {lemonade_sales}')
        self.assertAlmostEqual(cookie_sales, 12, msg=f'\nExpected value: 12 \nValue from your code: {cookie_sales}')
        self.assertAlmostEqual(hot_chocolate_sales, 4,
                               msg=f'\nExpected value: 4 \nValue from your code: {hot_chocolate_sales}')

    def test_4(self):
        """Testing total_profit_for_menu_item()"""
        stand = LemonadeStand('Lemons R Us')
        item1 = MenuItem('lemonade', 0.5, 1.5)
        item2 = MenuItem('cookie', 0.3, 0.75)
        item3 = MenuItem('hot chocolate', 0.2, 1)
        stand.add_menu_item(item1)
        stand.add_menu_item(item2)
        stand.add_menu_item(item3)
        day0 = {
            'lemonade': 5,
            'cookie': 2
        }
        day1 = {
            'cookie': 6,
            'lemonade': 8
        }
        day2 = {
            'hot chocolate': 4,
            'lemonade': 7,
            'cookie': 4
        }
        stand.enter_sales_for_today(day0)
        stand.enter_sales_for_today(day1)
        stand.enter_sales_for_today(day2)
        lemonade_profit = stand.total_profit_for_menu_item('lemonade')
        cookie_profit = stand.total_profit_for_menu_item('cookie')
        hot_chocolate_profit = stand.total_profit_for_menu_item('hot chocolate')
        self.assertAlmostEqual(lemonade_profit, 20.0,
                               msg=f'\nExpected value: 20.0 \nValue from your code: {lemonade_profit}')
        self.assertAlmostEqual(cookie_profit, 5.4, msg=f'\nExpected value: 5.4 \nValue from your code: {cookie_profit}')
        self.assertAlmostEqual(hot_chocolate_profit, 3.2,
                               msg=f'\nExpected value: 3.2 \nValue from your code: {hot_chocolate_profit}')

    def test_5(self):
        """Testing total_profit_for_stand()"""
        stand = LemonadeStand('Lemons R Us')
        item1 = MenuItem('lemonade', 0.5, 1.5)
        item2 = MenuItem('cookie', 0.3, 0.75)
        item3 = MenuItem('hot chocolate', 0.2, 1)
        stand.add_menu_item(item1)
        stand.add_menu_item(item2)
        stand.add_menu_item(item3)
        day0 = {
            'lemonade': 5,
            'cookie': 2
        }
        day1 = {
            'cookie': 6,
            'lemonade': 8
        }
        day2 = {
            'hot chocolate': 4,
            'lemonade': 7,
            'cookie': 4
        }
        stand.enter_sales_for_today(day0)
        stand.enter_sales_for_today(day1)
        stand.enter_sales_for_today(day2)
        total_profit = stand.total_profit_for_stand()
        self.assertAlmostEqual(total_profit, 28.6, msg=f'\nExpected value: 28.6 \nValue from your code: {total_profit}')

    def test_6(self):
        """Test sales_of_menu_item_for_day()"""
        stand = LemonadeStand('Lemons R Us')
        item1 = MenuItem('lemonade', 0.5, 1.5)
        item2 = MenuItem('cookie', 0.3, 0.75)
        item3 = MenuItem('hot chocolate', 0.2, 1)
        stand.add_menu_item(item1)
        stand.add_menu_item(item2)
        stand.add_menu_item(item3)
        day0 = {
            'lemonade': 5,
            'cookie': 2
        }
        day1 = {
            'cookie': 6,
            'lemonade': 8
        }
        day2 = {
            'hot chocolate': 4,
            'lemonade': 7,
            'cookie': 4
        }
        stand.enter_sales_for_today(day0)
        stand.enter_sales_for_today(day1)
        stand.enter_sales_for_today(day2)
        result = stand.sales_of_menu_item_for_day(1, 'lemonade')
        self.assertEqual(result, 8, msg=f'\nExpected value: 8 \nValue from your code: {result}')
        result = stand.sales_of_menu_item_for_day(0, 'hot chocolate')
        self.assertEqual(result, 0, msg=f'\nExpected value: 0 \nValue from your code: {result}')

    def test_7(self):
        """Test get methods"""
        stand = LemonadeStand('Lemons R Us')
        self.assertEqual(stand.get_name(), 'Lemons R Us')

        item1 = MenuItem('lemonade', 0.5, 1.5)
        self.assertEqual(item1.get_name(), 'lemonade')
        self.assertAlmostEqual(item1.get_wholesale_cost(), 0.5)
        self.assertAlmostEqual(item1.get_selling_price(), 1.5)

        day0 = {
            'lemonade': 5,
            'cookie': 2
        }
        sales0 = SalesForDay(0, day0)
        self.assertEqual(sales0.get_day(), 0, msg=f'\nExpected value: 0 \nValue from your code: {sales0.get_day()}')
        self.assertEqual(sales0.get_sales_dict(), day0,
                         msg=f'\nExpected value: {day0} \nValue from your code: {sales0.get_sales_dict()}')

    def test_8(self):
        """Testing total_profit_for_menu_item() with more items and days"""
        stand = LemonadeStand('Lemons R Us')
        item1 = MenuItem('lemonade', 0.5, 1.5)
        item2 = MenuItem('cookie', 0.3, 0.75)
        item3 = MenuItem('hot chocolate', 0.2, 1)
        item4 = MenuItem('blueberry muffin', 0.5, 1.0)
        stand.add_menu_item(item1)
        stand.add_menu_item(item2)
        stand.add_menu_item(item3)
        stand.add_menu_item(item4)
        day0 = {
            'lemonade': 5,
            'cookie': 2,
            'blueberry muffin': 6
        }
        day1 = {
            'blueberry muffin': 1,
            'cookie': 6,
            'hot chocolate': 3,
            'lemonade': 8
        }
        day2 = {
            'hot chocolate': 4,
            'lemonade': 7,
            'cookie': 4
        }
        day3 = {
            'blueberry muffin': 6,
            'cookie': 4,
            'hot chocolate': 3,
            'lemonade': 1
        }
        stand.enter_sales_for_today(day0)
        stand.enter_sales_for_today(day1)
        stand.enter_sales_for_today(day2)
        stand.enter_sales_for_today(day3)

        item5 = MenuItem('fish pie', 1.0, 2.0)
        stand.add_menu_item(item5)
        day4 = {
            'lemonade': 4,
            'fish pie': 8,
            'hot chocolate': 1,
            'cookie': 7,
            'blueberry muffin': 3
        }
        stand.enter_sales_for_today(day4)

        lemonade_profit = stand.total_profit_for_menu_item('lemonade')
        cookie_profit = stand.total_profit_for_menu_item('cookie')
        hot_chocolate_profit = stand.total_profit_for_menu_item('hot chocolate')
        blueberry_muffin_profit = stand.total_profit_for_menu_item('blueberry muffin')
        fish_pie_profit = stand.total_profit_for_menu_item('fish pie')
        self.assertAlmostEqual(lemonade_profit, 25.0,
                               msg=f'\nExpected value: 25.0 \nValue from your code: {lemonade_profit}')
        self.assertAlmostEqual(cookie_profit, 10.35,
                               msg=f'\nExpected value: 10.35 \nValue from your code: {cookie_profit}')
        self.assertAlmostEqual(hot_chocolate_profit, 8.8,
                               msg=f'\nExpected value: 8.8 \nValue from your code: {hot_chocolate_profit}')
        self.assertAlmostEqual(blueberry_muffin_profit, 8.0,
                               msg=f'\nExpected value: 8.0 \nValue from your code: {blueberry_muffin_profit}')
        self.assertAlmostEqual(fish_pie_profit, 8.0,
                               msg=f'\nExpected value: 8.0 \nValue from your code: {fish_pie_profit}')
        total_profit = stand.total_profit_for_stand()
        self.assertAlmostEqual(total_profit, 60.15,
                               msg=f'\nExpected value: 60.15 \nValue from your code: {total_profit}')
