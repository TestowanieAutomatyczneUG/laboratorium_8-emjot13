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

class Tests(unittest.TestCase):
    def setUp(self):
        self.temp = Age()

    #z poziomu metod

    @parameterized.expand([
    ("Wenus", 21777889, 1.12),
    ("Jowisz", 645324536, 1.72),
    ("Neptun", 3221785589.444, 0.62),
    ("Saturn", 444313, 0.0),
    ("Uran", 100000, 0.0),
    ("Neptun", 991199889, 0.19),
    ("Mars", 9911990009, 167.0),
    ("Ziemia", 999999999.42389, 31.69)
    ])
    
    def test_parameterized(self, planet, seconds, output):
        self.assertEqual(self.temp.getAge(planet, seconds), output)

    @parameterized.expand([
        ("Ziemi", 32853289),
        (5435435, "Mars"),
        (None, 89325),
        ("ZiemIa", 3333),
        ("", 552454677),
        ("Mars", ""),
        ("Neptun", "55"),
        ("Uran", -24235),
        ("Jowisz", []),
        ("Merkury", {})
    ])

    def test_exceptions(self, planet, seconds):
        self.assertRaises(Exception, self.temp.getAge, planet, seconds)



