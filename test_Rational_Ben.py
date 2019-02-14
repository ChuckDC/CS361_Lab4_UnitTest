from unittest import TestCase
from Rational import Rational
import math
class TestRational_Ben(TestCase):

    def testToSTR(self):
        self.default = Rational()
        self.zero = Rational(0, 1)
        self.num1 = Rational(1, 1)
        self.num2 = Rational(1, 2)
        self.numNeg = Rational(1, -2)
        self.numReduced = Rational(2, 4)
        self.numFloat = Rational(1, 200000)

        self.assertEquals(self.default.__str__(), "0")
        self.assertEquals(self.zero.__str__(), "0")
        self.assertEquals(self.num1.__str__(), "1")
        self.assertEquals(self.num2.__str__(), "1/2")
        self.assertEquals(self.numNeg.__str__(), "1/-2")
        self.assertEquals(self.numReduced.__str__(), "1/2")
        self.assertEquals(self.numFloat.__str__(), "0.000005")

    def testToFloat(self):
        self.defaultFloat = Rational()
        self.floatZero = Rational(0, 1)
        self.float1 = Rational(1, 200000)
        self.float2 = Rational(1, 1)
        self.float3 = Rational(1559, 4420)
        self.floatNeg = Rational(5, -2)

        self.assertEquals(self.defaultFloat.__float__(), 0.0)
        self.assertEquals(self.floatZero.__float__(), 0.0)
        self.assertEquals(self.float1.__float__(), 0.000005)
        self.assertEquals(self.float2.__float__(), 1)
        self.assertEquals(self.float3.__float__(), 0.35271493212669683257918552036199)
        self.assertEquals(self.floatNeg.__float__(), -2.5)
