import unittest
from Library import Library, Book, Album, Movie, Patron


class LibraryTest(unittest.TestCase):
    """inherit from unittest.TestCase giving access to many testing capabilities"""

    def test_add_library_item(self):
        """Check if b1 was added to the holdings"""
        b1 = Book("345", "Phantom Tollbooth", "Juster")
        lib = Library()
        lib.add_library_item(b1)

        self.assertIn(b1, lib._holdings)
        print('b1 is added to the library holding - PASS')

        self.assertEqual(lib.lookup_library_item_from_id('345'), b1)
        print('b1 searched by ID - PASS')

    def test_add_patron(self):
        """Check if p1 is added to members"""
        p1 = Patron('abc', 'Felicity')
        lib = Library()
        lib.add_patron(p1)

        self.assertIn(p1, lib._members)
        print('p1 is added to members - PASS')

        self.assertEqual(lib.lookup_patron_from_id('abc'), p1)
        print('p1 searched by ID - PASS')

    def test_check_out_library_item(self):
        """Test check_out_library_item method"""

        a1 = Album("456", "...And His Orchestra", "The Fastbacks")
        p2 = Patron("bcd", "Waldo")

        lib = Library()
        lib.add_library_item(a1)
        lib.add_patron(p2)

        removal = lib.check_out_library_item('bcd', '456')
        self.assertEqual(removal, 'check out successful')
        print('Available Item checkout - PASS')


if __name__ == '__main__':
    unittest.main()
