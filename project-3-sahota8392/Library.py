# Author:  Harpreet Sahota
# GitHub:  Sahota8392
# Date:  7/9/2023
# Description:  Library simulator with 3 classes inheriting from LibraryItem


class LibraryItem:
    """
    library item that patron can check out from library with 6 data members
    """

    def __init__(self, library_item_id, title):
        """initial value of LibraryItem data members"""
        self._library_item_id = library_item_id
        self._title = title
        self._checked_out_by = None
        self._requested_by = None
        self._date_checked_out = None
        self._location = "ON_SHELF"

    def get_location(self):
        """returns library item's location"""
        return self._location

    def get_library_item_id(self):
        """returns unique identifier for library item"""
        return self._library_item_id

    def get_title(self):
        """returns library item title"""
        return self._title

    def get_checked_out_by(self):
        """returns patron who has it checked out"""
        return self._checked_out_by

    def get_requested_by(self):
        """returns patron who has it requested it"""
        return self._requested_by

    def get_date_checked_out(self):
        """return date item is checked out"""
        return self._date_checked_out

    def set_requested_by(self, patron):
        """sets the patron requesting"""
        self._requested_by = patron

    def set_checked_out_by(self, patron):
        """sets the checked out patron"""
        self._checked_out_by = patron

    def set_date_checked_out(self, date):
        """sets the date item is checked out"""
        self._date_checked_out = date

    def set_location(self, location):
        """sets the item location"""
        self._location = location


class Book(LibraryItem):
    """
    Book class that inherits from the LibraryItem class
    """

    def __init__(self, library_item_id, title, author):
        """initial value of Book data members and inherits from LibraryItem"""
        super().__init__(library_item_id, title)
        self._author = author

    def get_author(self):
        """returns the author of the book"""
        return self._author

    def get_check_out_length(self):
        """returns number of days that type of library item may be checked out for"""
        return 21


class Album(LibraryItem):
    """
    Album class that inherits from the LibraryItem class
    """

    def __init__(self, library_item_id, title, artist):
        """initial value of Album data members and inherits from LibraryItem"""
        super().__init__(library_item_id, title)
        self._artist = artist

    def get_artist(self):
        """returns the artist of the album"""
        return self._artist

    def get_check_out_length(self):
        """returns number of days that type of library item may be checked out for"""
        return 14


class Movie(LibraryItem):
    """
    Movie class that inherits from LibraryItem Class
    """

    def __init__(self, library_item_id, title, director):
        """initial value of Movie data members and inherits from LibraryItem"""
        super().__init__(library_item_id, title)
        self._director = director

    def get_director(self):
        """returns the director of the movie"""
        return self._director

    def get_check_out_length(self):
        """returns number of days that type of library item may be checked out for"""
        return 7


class Patron:
    """
    represents patron of a library with 4 data members
    """

    def __init__(self, patron_id, name):
        """initial value of Patron data members and inherits from LibraryItem"""
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0

    def get_patron_id(self):
        """returns the patron id"""
        return self._patron_id

    def get_name(self):
        """returns the name of patron"""
        return self._name

    def get_fine_amount(self):
        """returns the amount of fine"""
        return self._fine_amount

    def get_checked_out_items(self):
        """returns the items checked out"""
        return self._checked_out_items

    def get_overdue_items(self, current_date):
        """returns the overdue items based on due date"""
        overdue_items = []
        for item in self._checked_out_items:
            due_date = item.get_date_checked_out() + item.get_check_out_length()
            if current_date > due_date:
                overdue_items.append(item)
        return overdue_items

    def amend_fine(self, fine):
        """positive increases fine and negative decreases fine"""
        self._fine_amount += fine

    def set_fine_amount(self, fine):
        """sets the fine amount"""
        self._fine_amount = fine

    def add_library_item(self, library_item):
        """adds library item to checked_out_items"""
        self._checked_out_items.append(library_item)

    def remove_library_item(self, library_item):
        """removes the library item from checked_out_items"""
        self._checked_out_items.remove(library_item)


class Library:
    """
    represents library that contains various library items and used by various patrons
    """

    def __init__(self):
        """initial values for Library are set to empty and 0"""
        self._holdings = []
        self._members = []
        self._current_date = 0

    def add_library_item(self, library_item):
        """adds item to the holdings"""
        self._holdings.append(library_item)

    def add_patron(self, patron):
        """adds patron to member list"""
        self._members.append(patron)

    def lookup_library_item_from_id(self, library_item_id):
        """looks up library item with holdings and returns library id else None"""
        for item in self._holdings:
            if item.get_library_item_id() == library_item_id:
                return item
        return None

    def lookup_patron_from_id(self, patron_id):
        """looks up the patron and returns patron id else None"""
        for patron in self._members:
            if patron.get_patron_id() == patron_id:
                return patron
        return None

    def check_out_library_item(self, patron_id, library_item_id):
        """returns status of library items that are checked out and patron"""
        patron = self.lookup_patron_from_id(patron_id)
        if patron is None:
            return 'patron not found'

        library_item = self.lookup_library_item_from_id(library_item_id)
        if library_item is None:
            return 'item not found'

        if library_item.get_location() == 'CHECKED_OUT':
            return 'item already checked out'

        if library_item.get_requested_by() != patron and library_item.get_requested_by() is not None:
            return 'item on hold by other patron'

        library_item.set_checked_out_by(patron)
        library_item.set_date_checked_out(self._current_date)
        library_item.set_location('CHECKED_OUT')

        if library_item.get_requested_by() == patron:
            library_item.set_requested_by(None)

        patron.add_library_item(library_item)
        return 'check out successful'

    def return_library_item(self, library_item_id):
        """Returns the library item updating the respective methods"""
        library_item = self.lookup_library_item_from_id(library_item_id)
        if library_item is None:
            return 'item not found'

        if library_item.get_location() != 'CHECKED_OUT':
            return 'item already in library'

        patron = library_item.get_checked_out_by()
        patron.remove_library_item(library_item)

        if library_item.get_requested_by() is not None:
            library_item.set_location('ON_HOLD_SHELF')
        else:
            library_item.set_location('ON_SHELF')

        library_item.set_checked_out_by(None)

        return 'return successful'

    def request_library_item(self, patron_id, library_item_id):
        """returns the requested item status"""
        patron = self.lookup_patron_from_id(patron_id)
        if patron is None:
            return 'patron not found'

        library_item = self.lookup_library_item_from_id(library_item_id)
        if library_item is None:
            return 'item not found'

        if library_item.get_requested_by() is not None:
            return 'item already on hold'

        library_item.set_requested_by(patron)

        if library_item.get_location() == 'ON_SHELF':
            library_item.set_location('ON_HOLD_SHELF')

        return 'request successful'

    def pay_fine(self, patron_id, fine):
        """reduce the fine amount"""
        patron = self.lookup_patron_from_id(patron_id)
        if patron is None:
            return 'patron not found'

        patron.amend_fine(-fine)

        return 'payment successful'

    def increment_current_date(self):
        """increments the date for overdue item adding 10 cent to the fine"""
        self._current_date += 1

        for patron in self._members:
            overdue_items = patron.get_overdue_items(self._current_date)
            if overdue_items is not None:
                for item in overdue_items:
                    fine = 0.10
                    patron.amend_fine(fine)
#
#
# b1 = Book("345", "Phantom Tollbooth", "Juster")
# c1 = Book('452', 'Doc Oz', 'Times')
# a1 = Album("456", "...And His Orchestra", "The Fastbacks")
# m1 = Movie("567", "Laputa", "Miyazaki")
#
# print('b1 - ID, Title, Author: ', b1.get_library_item_id(), b1.get_title(), b1.get_author())
# print('Book Checkout Days: ', b1.get_check_out_length())
# print()
#
# print('a1 - ID, Title, Artist: ', a1.get_library_item_id(), a1.get_title(), a1.get_artist())
# print('Album Checkout Days: ', a1.get_check_out_length())
# print()
#
# print('m1 - ID, Title, Director: ', m1.get_library_item_id(), m1.get_title(), m1.get_director())
# print('Movie Checkout Days: ', m1.get_check_out_length())
# print()
#
# p1 = Patron("abc", "Felicity")
# p2 = Patron("bcd", "Waldo")
#
# print('p1 ID, Name, Checked Items, Fine', p1.get_patron_id(), p1.get_name(), p1.get_checked_out_items(),
#       p1.get_fine_amount())
# print('p2 ID, Name, Checked Items, Fine', p2.get_patron_id(), p2.get_name(), p2.get_checked_out_items(),
#       p2.get_fine_amount())
#
# lib = Library()
# lib.add_library_item(b1)
# lib.add_library_item(a1)
# lib.add_library_item(m1)
# print('b1 title:', lib.lookup_library_item_from_id(b1.get_library_item_id()).get_title())
# print('b1 location', lib.lookup_library_item_from_id(b1.get_library_item_id()).get_location())
# print('b1 checked out by:', lib.lookup_library_item_from_id(b1.get_library_item_id()).get_checked_out_by())
# print('b1 requested by:', lib.lookup_library_item_from_id(b1.get_library_item_id()).get_requested_by())
# print('b1 date checked:', lib.lookup_library_item_from_id(b1.get_library_item_id()).get_date_checked_out())
# print()
#
# print('a1 title:', lib.lookup_library_item_from_id(a1.get_library_item_id()).get_title())
# print('a1 location', lib.lookup_library_item_from_id(a1.get_library_item_id()).get_location())
# print('a1 checked out by:', lib.lookup_library_item_from_id(a1.get_library_item_id()).get_checked_out_by())
# print('a1 requested by:', lib.lookup_library_item_from_id(a1.get_library_item_id()).get_requested_by())
# print('a1 date checked:', lib.lookup_library_item_from_id(a1.get_library_item_id()).get_date_checked_out())
# print()
#
# print('c1 item:', lib.lookup_library_item_from_id(c1.get_library_item_id()))
# print()
#
# lib.add_patron(p1)
# lib.add_patron(p2)
#
# lib.check_out_library_item("bcd", "456")
# for _ in range(7):
#     lib.increment_current_date()  # 7 days pass
# lib.check_out_library_item("abc", "567")
# print('b1 title:', lib.lookup_library_item_from_id(b1.get_library_item_id()).get_title())
# print('b1 location', lib.lookup_library_item_from_id(b1.get_library_item_id()).get_location())
# print('b1 checked out by:', lib.lookup_library_item_from_id(b1.get_library_item_id()).get_checked_out_by())
# print('b1 date checked:', lib.lookup_library_item_from_id(b1.get_library_item_id()).get_date_checked_out())
# print()
#
# print('a1 title:', lib.lookup_library_item_from_id(a1.get_library_item_id()).get_title())
# print('a1 location', lib.lookup_library_item_from_id(a1.get_library_item_id()).get_location())
# print('a1 checked out by:', lib.lookup_library_item_from_id(a1.get_library_item_id()).get_checked_out_by().get_name())
# print('a1 date checked:', lib.lookup_library_item_from_id(a1.get_library_item_id()).get_date_checked_out())
# print()
#
# print('m1 title:', lib.lookup_library_item_from_id(m1.get_library_item_id()).get_title())
# print('m1 location', lib.lookup_library_item_from_id(m1.get_library_item_id()).get_location())
# print('m1 checked out by:', lib.lookup_library_item_from_id(m1.get_library_item_id()).get_checked_out_by().get_name())
# print('m1 date checked:', lib.lookup_library_item_from_id(m1.get_library_item_id()).get_date_checked_out())
# print()
#
# print('a1 location', a1.get_location())
#
# lib.request_library_item("abc", "456")
# print('a1 requested by:', lib.lookup_library_item_from_id(a1.get_library_item_id()).get_requested_by().get_patron_id())
# print()
#
# for _ in range(57):
#     lib.increment_current_date()  # 57 days pass
# p2_fine = p2.get_fine_amount()
# print('p2 fine', p2.get_fine_amount())
#
# lib.pay_fine("bcd", p2_fine)
# print('p2 pay fine', p2.get_fine_amount())
#
# lib.return_library_item("456")
# print('a1 location', lib.lookup_library_item_from_id(a1.get_library_item_id()).get_location())
