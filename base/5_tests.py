"""
Написание тестов
"""
# Юнит тесты

import unittest


def add(x, y):
    return x + y


class TestAdd(unittest.TestCase):
    """Тестирование функции add."""

    def test_add_positive_numbers(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_add_negative_numbers(self):
        result = add(-2, -3)
        self.assertEqual(result, -5)

    def test_add_zero(self):
        result = add(0, 5)
        self.assertEqual(result, 5)

    def test_add_negative_and_positive(self):
        result = add(-2, 5)
        self.assertEqual(result, 3)

    def test_add_zero_and_zero(self):
        result = add(0, 0)
        self.assertEqual(result, 0)

    def test_add_large_numbers(self):
        result = add(999999999, 1)
        self.assertEqual(result, 1000000000)

    def test_add_floats(self):
        result = add(1.2, 3.4)
        self.assertAlmostEqual(result, 4.6)

    def test_add_string(self):
        with self.assertRaises(TypeError):
            add('one', 2)

    def test_add_none(self):
        with self.assertRaises(TypeError):
            add(None, 2)

    def test_add_boolean(self):
        result1 = add(True, 2)
        result2 = add(False, 4)
        self.assertEqual(result1, 3)
        self.assertEqual(result2, 4)


if __name__ == '__main__':
    unittest.main()
