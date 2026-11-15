
"""CSC 1001 - Programming Assignment 1: Student-written unit tests."""

import unittest
import data
import hw1


class TestHomework1(unittest.TestCase):

    # Part 1: vowel_count
    def test_vowel_count_case_insensitive(self):
        self.assertEqual(hw1.vowel_count('AEiou Apple'), 7)

    def test_vowel_count_empty_string(self):
        self.assertEqual(hw1.vowel_count(''), 0)

    # Part 2: short_lists
    def test_short_lists_mixed_lengths(self):
        values = [[1], [2, 3], [], [4, 5, 6], [7, 8]]
        self.assertEqual(hw1.short_lists(values), [[2, 3], [7, 8]])

    def test_short_lists_no_matching_lengths(self):
        self.assertEqual(hw1.short_lists([[], [1], [2, 3, 4]]), [])

    # Part 3: ascending_pairs
    def test_ascending_pairs_reversed_pairs(self):
        values = [[9, 2], [3, 1], [5, 5]]
        self.assertEqual(hw1.ascending_pairs(values), [[2, 9], [1, 3], [5, 5]])

    def test_ascending_pairs_other_lengths_unchanged(self):
        values = [[], [3], [3, 1, 2], [2, 4]]
        self.assertEqual(hw1.ascending_pairs(values), values)

    # Part 4: add_prices
    def test_add_prices_no_cents_carry(self):
        result = hw1.add_prices(data.Price(2, 15), data.Price(3, 20))
        self.assertEqual(result, data.Price(5, 35))

    def test_add_prices_with_cents_carry(self):
        result = hw1.add_prices(data.Price(3, 75), data.Price(2, 50))
        self.assertEqual(result, data.Price(6, 25))

    # Part 5: rectangle_area
    def test_rectangle_area_standard_rectangle(self):
        rectangle = data.Rectangle(data.Point(1, 7), data.Point(5, 2))
        self.assertAlmostEqual(hw1.rectangle_area(rectangle), 20)

    def test_rectangle_area_negative_coordinates(self):
        rectangle = data.Rectangle(data.Point(-5, 3), data.Point(-1, -3))
        self.assertAlmostEqual(hw1.rectangle_area(rectangle), 24)

    # Part 6: books_by_author
    def test_books_by_author_matching_authors(self):
        book1 = data.Book(['Neil Gaiman', 'Terry Pratchett'], 'Good Omens')
        book2 = data.Book(['Neil Gaiman'], 'Coraline')
        book3 = data.Book(['Terry Pratchett'], 'Mort')
        self.assertEqual(hw1.books_by_author('Neil Gaiman', [book1, book2, book3]),
                         [book1, book2])

    def test_books_by_author_no_matches(self):
        books = [data.Book(['Terry Pratchett'], 'Mort')]
        self.assertEqual(hw1.books_by_author('Neil Gaiman', books), [])

    # Part 7: circle_bound
    def test_circle_bound_square(self):
        rectangle = data.Rectangle(data.Point(0, 2), data.Point(2, 0))
        circle = hw1.circle_bound(rectangle)
        self.assertEqual(circle.center, data.Point(1, 1))
        self.assertAlmostEqual(circle.radius, 2 ** 0.5)

    def test_circle_bound_non_square_rectangle(self):
        rectangle = data.Rectangle(data.Point(-2, 4), data.Point(4, -4))
        circle = hw1.circle_bound(rectangle)
        self.assertEqual(circle.center, data.Point(1, 0))
        self.assertAlmostEqual(circle.radius, 5)

    # Part 8: below_pay_average
    def test_below_pay_average_different_pay_rates(self):
        employees = [data.Employee('Amy', 10), data.Employee('Ben', 20),
                     data.Employee('Cara', 30), data.Employee('Dan', 15)]
        self.assertEqual(hw1.below_pay_average(employees), ['Amy', 'Dan'])

    def test_below_pay_average_empty_list(self):
        self.assertEqual(hw1.below_pay_average([]), [])


if __name__ == '__main__':
    unittest.main()
