from unittest import TestCase
from Rational import Rational
import math
class TestRational(TestCase):
    def testAddIrrationalNumber(self):
        r = Rational();
        self.assertRaises(Exception, r.__add__( math.sqrt(-1), math.sqrt(-1)));
    def testAddABoolean(self):
        r = Rational();
        self.assertRaises(Exception, r.__add__(true, 1));
        pass
