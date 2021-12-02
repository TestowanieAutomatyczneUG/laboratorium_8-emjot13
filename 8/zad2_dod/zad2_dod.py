import unittest
from parameterized import parameterized, parameterized_class

class Age:
    def getAge(self, planet, seconds):
        planets = ["Ziemia", "Merkury", "Wenus", "Mars", "Jowisz", "Saturn", "Uran", "Neptun"]
        if planet not in planets:
            raise Exception("Enter a correct planet")


        if type(seconds) != int and type(seconds) != float or seconds < 0:
            raise Exception("Seconds variable must be a number bigger than 0")


        if planet == "Ziemia":
            age = round(seconds / 31557600, 2)
        if planet == "Merkury":
            age = round(seconds / 31557600 / 0.2408467, 2)
        if planet == "Wenus":
            age = round(seconds / 31557600 / 0.61519726, 2)
        if planet == "Mars":
            age = round(seconds / 31557600 / 1.8808158, 2)
        if planet == "Jowisz":
            age = round(seconds / 31557600 / 11.862615, 2)
        if planet == "Saturn":
            age = round(seconds / 31557600 / 29.447498, 2)
        if planet == "Uran":
            age = round(seconds / 31557600 / 84.016846, 2)
        if planet == "Neptun":
            age = round(seconds / 31557600 / 164.79132, 2)
        return age


@parameterized_class(("planet", "seconds", "output"),
                     [
                         ("Wenus", 21777889, 1.12),
                         ("Jowisz", 645324536, 1.72),
                         ("Neptun", 3221785589.444, 0.62),
                         ("Saturn", 444313, 0.0),
                         ("Uran", 100000, 0.0),
                         ("Neptun", 991199889, 0.19),
                         ("Mars", 9911990009, 167.0),
                         ("Ziemia", 999999999.42389, 31.69)
                     ])
class Test_With_Class_Assert_Equal(unittest.TestCase):

    def setUp(self):
        self.temp = Age()

    def test_positive(self):
        self.assertEqual(self.temp.getAge(self.planet, self.seconds), self.output)


@parameterized_class(("planet", "seconds", "exception"),
                     [
                         ("Ziemi", 32853289, Exception),
                         (5435435, "Mars", Exception),
                         (None, 89325, Exception),
                         ("ZiemIa", 3333, Exception),
                         ("", 552454677, Exception),
                         ("Mars", "", Exception),
                         ("Neptun", "55", Exception),
                         ("Uran", -24235, Exception),
                         ("Jowisz", [], Exception),
                         ("Merkury", {}, Exception)
                     ])
class Test_With_Class_Assert_Raises(unittest.TestCase):
    def setUp(self):
        self.temp = Age()

    def test_assert_raises(self):
        self.assertRaises(self.exception, self.planet, self.seconds)