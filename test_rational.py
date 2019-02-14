from unittest import TestCase
from Rational import Rational
import math
class TestRational(TestCase):
    def testAddIrrationalNumber(self):
        r = Rational();
        self.assertRaises(Exception, r.add,  math.sqrt(-1), math.sqrt(-1));
    pass
