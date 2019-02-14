from unittest import TestCase
from Rational import Rational
import math
class TestRational(TestCase):
    def testAddIrrationalNumber(self):
        r = Rational()
        self.assertRaises(Exception, r.__add__(math.sqrt(1)))

    def testAddABoolean(self):
        r = Rational()
        self.assertRaises(Exception, r.__add__(True))

    def testDivideByZero(self):
        r = Rational(0)
self.assertRaises(Exception)