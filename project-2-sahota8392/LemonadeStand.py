# Author: Harpreet Sahota
# GitHub: Sahota8392
# Date: 7/03/2023
# Description: Create code to record menu items and daily sales of a lemonade stand


class InvalidSalesItemError(Exception):
    pass


class MenuItem:
    """Class 1 MenuItems"""

    def __init__(self, name, wholesale_cost, selling_price):
        """Creates menu with 3 parameters (name, cost and sales price)"""
        self._name = name
        self._wholesale_cost = wholesale_cost
        self._selling_price = selling_price

    def get_name(self):
        """Returns menu item name"""
        return self._name

    def get_wholesale_cost(self):
        """Returns menu item cost"""
        return self._wholesale_cost

    def get_selling_price(self):
        """Return selling price of menu item"""
        return self._selling_price


class SalesForDay:
    """Class 2 Sales for the Day"""

    def __init__(self, day, sales_dict):
        """Create Sales of Day with 2 parameters (number of day and dictionary of item names"""
        self._day = day
        self._sales_dict = sales_dict

    def get_day(self):
        """Returns the number of days stand has been open so far"""
        return self._day

    def get_sales_dict(self):
        """Returns Dict (names of item sold: number of items sold)"""
        return self._sales_dict


class LemonadeStand:
    """Class 3 Lemonade Stand"""

    def __init__(self, stand):
        """Create lemonade stand with 1 parameter, initial day 0, initial menu empty dictionary, initial sales empty
        list"""
        # self.stand = stand    need to privatize since using get
        self._stand = stand
        self._current_day = 0
        self._menu = {}
        self._sales = []

    def get_name(self):
        """Returns Lemonade Stand Name"""
        return self._stand

    def add_menu_item(self, menu_item):
        """Adds to the menu dictionary"""
        self._menu[menu_item.get_name()] = menu_item

    def enter_sales_for_today(self, item_sales):
        """If item is not in Menu, raise error else add object to list of SalesForDay and increment day by 1"""
        for item in item_sales:
            if item in self._menu:
                pass
            else:
                raise InvalidSalesItemError

        self._sales.append(SalesForDay(self._current_day, item_sales))
        self._current_day += 1

        # for item, count in sales_dict.items():
        #     if item not in self._menu:
        #         raise InvalidSalesItemError
        #     else:
        #         sales_for_day = SalesForDay(self._current_day, sales_dict)
        #         self._sales_day.append(sales_for_day)
        #         self._current_day += 1

    def sales_of_menu_item_for_day(self, day, menu_item_name):
        """returns the number of sales for a menu item in a given day"""
        for sales_for_day in self._sales:
            if sales_for_day.get_day() == day:
                if menu_item_name in sales_for_day.get_sales_dict():
                    return sales_for_day.get_sales_dict()[menu_item_name]
                return 0
        # if day_number <= 0:
        #     return 0
        # sales_in_the_day = self._sales_day[day_number]
        # sales_dict = sales_in_the_day.get_sales_dict
        #
        # if menu_item_name in sales_dict:
        #     return sales_dict[menu_item_name]
        # return 0

    def total_sales_for_menu_item(self, item_name):
        """Return total number of item sold over history of stand"""
        total_sales = 0
        for day in range(self._current_day):
            total_sales += self.sales_of_menu_item_for_day(day, item_name)
        return total_sales

        # for sales_in_day in self._sales_day:
        #     sales_dict = sales_in_day.get_sales_dict()
        #     if item_name in sales_dict:
        #         total_sales += sales_dict[item_name]

    def total_profit_for_menu_item(self, item_name):
        """Returns total profit of menu item over history of stand"""
        total_sale_item = self.total_sales_for_menu_item(item_name)
        total_profit = self._menu[item_name].get_selling_price() - self._menu[item_name].get_wholesale_cost()
        return total_profit * total_sale_item

    def total_profit_for_stand(self):
        """total profit of all items in stand over history of stand"""
        total = 0
        for item_name in self._menu:
            total += self.total_profit_for_menu_item(self._menu[item_name].get_name())
            # total += self.total_profit_for_menu_item(item_name)
        return total


def main():
    stand = LemonadeStand('Lemons R Us')
    item1 = MenuItem('lemonade', 0.5, 1.5)
    stand.add_menu_item(item1)
    item2 = MenuItem('nori', 0.6, 0.8)
    stand.add_menu_item(item2)
    item3 = MenuItem('cookie', 0.2, 1)
    stand.add_menu_item(item3)
    day_0_sales = {
        'lemonade': 5,
        'cookie': 2
    }
    stand.enter_sales_for_today(day_0_sales)
    print(f"lemonade profit = {stand.total_profit_for_menu_item('lemonade')}")


if __name__ == '__main__':
    main()
