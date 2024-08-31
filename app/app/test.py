"""
Sample tests
"""

from django.test import SimpleTestCase # type: ignore

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc Module."""

    def test_add_numbers(self):
        """Test adding number together."""
        res = calc.add(5,5)

        self.assertEqual(res, 10)

    def test_sub_numbers(self):
        """Test subtracting number together"""
        res = calc.subtract(5,3)

        self.assertEqual(res, 2)
