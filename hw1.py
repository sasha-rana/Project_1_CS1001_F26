
"""CSC 1001 - Programming Assignment 1: Functions and Compound Data."""

import math
import data


# Part 1: vowel_count
# Count vowels (a, e, i, o, u), regardless of case.
# Input: text as a string. Output: the number of vowels as an integer.
def vowel_count(text: str) -> int:
    count = 0
    for character in text.lower():
        if character in 'aeiou':
            count += 1
    return count


# Part 2: short_lists
# Select nested lists containing exactly two integers.
# Input: a list of integer lists. Output: a new list of the length-two lists.
def short_lists(values: list[list[int]]) -> list[list[int]]:
    result = []
    for inner_list in values:
        if len(inner_list) == 2:
            result.append(inner_list)
    return result


# Part 3: ascending_pairs
# Put values in each two-element nested list in non-descending order.
# Input: a list of integer lists. Output: a new outer list with ordered pairs.
def ascending_pairs(values: list[list[int]]) -> list[list[int]]:
    result = []
    for inner_list in values:
        if len(inner_list) == 2 and inner_list[0] > inner_list[1]:
            result.append([inner_list[1], inner_list[0]])
        else:
            result.append(inner_list.copy())
    return result


# Part 4: add_prices
# Add two prices and carry every 100 cents into one dollar.
# Inputs: two Price objects. Output: a new Price object containing their sum.
def add_prices(first: data.Price, second: data.Price) -> data.Price:
    total_cents = first.cents + second.cents
    dollars = first.dollars + second.dollars + total_cents // 100
    cents = total_cents % 100
    return data.Price(dollars, cents)


# Part 5: rectangle_area
# Find the area of an axis-aligned rectangle.
# Input: a Rectangle. Output: its area as a float.
def rectangle_area(rectangle: data.Rectangle) -> float:
    width = rectangle.bottom_right.x - rectangle.top_left.x
    height = rectangle.top_left.y - rectangle.bottom_right.y
    return width * height


# Part 6: books_by_author
# Find all books that list a particular author.
# Inputs: author name as a string and a list of Books.
# Output: a list of matching Book objects in their original order.
def books_by_author(author: str, books: list[data.Book]) -> list[data.Book]:
    result = []
    for book in books:
        if author in book.authors:
            result.append(book)
    return result


# Part 7: circle_bound
# Find the smallest circle containing an axis-aligned rectangle.
# Input: a Rectangle. Output: a new Circle centered on the rectangle.
def circle_bound(rectangle: data.Rectangle) -> data.Circle:
    center_x = (rectangle.top_left.x + rectangle.bottom_right.x) / 2
    center_y = (rectangle.top_left.y + rectangle.bottom_right.y) / 2
    width = rectangle.bottom_right.x - rectangle.top_left.x
    height = rectangle.top_left.y - rectangle.bottom_right.y
    radius = math.hypot(width, height) / 2
    return data.Circle(data.Point(center_x, center_y), radius)


# Part 8: below_pay_average
# Find names of employees paid strictly below the average pay rate.
# Input: a list of Employee objects. Output: a list of matching names.
# An empty employee list produces an empty name list.
def below_pay_average(employees: list[data.Employee]) -> list[str]:
    if not employees:
        return []
    average = sum(employee.pay_rate for employee in employees) / len(employees)
    result = []
    for employee in employees:
        if employee.pay_rate < average:
            result.append(employee.name)
    return result
