import unittest
from hamcrest import *
from assertpy import *
from sample.Planets import *


class Test(unittest.TestCase):
    def setUp(self):
        self.temp = Age()

    def testZiemia(self):
        assert_that(self.temp.getAge(1000, "Ziemia"), equal_to(round(1000 / 31557600, 2)))

    def testJowisz(self):
        assert_that(self.temp.getAge(10000000, "Jowisz"), less_than(549877549874387687))

    def testNeptun(self):
        assert_that(self.temp.getAge(1212121212, "Neptun"), is_(round(1212121212 / 31557600 / 164.79132, 2)))

    def testFloats(self):
        assert_warn(self.temp.getAge(1234.55, "Ziemia"))

    def testInstance(self):
        assert_that(self.temp, not_none())

    def testInstance2(self):
        assert_that(self.temp, instance_of(Age))

    def testRaiseExceptions(self):
        assert_warn(self.temp.getAge, 1000, "Ziemniak")

    def test_greater(self):
        assert_that(self.temp.getAge(200000000, "Ziemia"), greater_than(150000))

    def testanything(self):
        one = Age()
        two = Age()
        three = Age()
        assert_that(all_of(instance_of(Age), one, two, three))


    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
