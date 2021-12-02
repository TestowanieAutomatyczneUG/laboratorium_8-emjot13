class Age:
    def getAge(self, planet, seconds):
        planets = ["Ziemia", "Merkury", "Wenus", "Mars", "Jowisz", "Saturn", "Uran", "Neptun"]
        if planet not in planets:
            raise Exception("")

        if type(seconds) != int and type(seconds) != float or seconds < 0:
            raise Exception("")

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


obj = Age()
print(obj.getAge("Ziemia", -645324536))
