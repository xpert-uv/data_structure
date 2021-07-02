import unittest
from recursion import product, longest, every_other, is_palendrome, find_index
from recursion import reverse_string, gather_strings

class TestRecursiveFunctions(unittest.TestCase):
    def test_product(self):
        self.assertEqual(product([2, 3, 4]), 24)
        self.assertEqual(product([1, -1, 1, -1, 1, -1]), -1)
        self.assertEqual(product([10]), 10)

    def test_longest(self):
        self.assertEqual(longest(["hello", "hi", "hola"]), 5)
        self.assertEqual(longest(["abcdefg", "hijklmnop", "qrs", "tuv", "wx", "y", "z"]), 9)
        self.assertEqual(longest(["a", "b", "c", "d", "e"]), 1)
        self.assertEqual(longest(["abcde"]), 5)

    def test_every_other(self):
        self.assertEqual(every_other("hello"), "hlo")
        self.assertEqual(every_other("banana stand"), "bnn tn")
        self.assertEqual(every_other("ddoouubbllee"), "double")
        self.assertEqual(every_other("hi"), "h")
        self.assertEqual(every_other("z"), "z")

    def test_is_palendrome(self):
        self.assertEqual(is_palendrome("tacocat"), True)
        self.assertEqual(is_palendrome("racecar"), True)
        self.assertEqual(is_palendrome("a"), True)
        self.assertEqual(is_palendrome("helloolleh"), True)
        self.assertEqual(is_palendrome("tacodog"), False)
        self.assertEqual(is_palendrome("az"), False)
        self.assertEqual(is_palendrome("goodbye"), False)

    def test_find_index(self):
        animals = ["duck", "cat", "pony", "cat"]
        self.assertEqual(find_index(animals, "duck"), 0)
        self.assertEqual(find_index(animals, "cat"), 1)
        self.assertEqual(find_index(animals, "pony"), 2)
        self.assertEqual(find_index(animals, "turtle"), -1)

    def test_reverse_string(self):
        self.assertEqual(reverse_string("porcupine"), "enipucrop")
        self.assertEqual(reverse_string("pony"), "ynop")
        self.assertEqual(reverse_string("a"), "a")

    def test_gather_strings(self):
        map = { "firstName": "Lester",
                "favoriteNumber": 22,
                "moreData": { "lastName": "Testowitz"},
                "funFacts": { "moreStuff": {
                    "anotherNumber": 100,
                    "deeplyNestedString": {"almostThere": {"success": "you made it!"}}
                    },
                    "favoriteString": "nice!"
                }
            }
        strings = ["Lester", "Testowitz", "you made it!", "nice!"]
        self.assertEqual(gather_strings(map), strings)
