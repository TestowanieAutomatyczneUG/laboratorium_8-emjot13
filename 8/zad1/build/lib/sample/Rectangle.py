class Rectangle:
    def draw(self, a, b):
        outcome = ""
        if type(a) != int or type(b) != int:
            raise Exception("Must be an integer")
        if a <= 0 or b <= 0:
            raise Exception("Number cannot be negative")

        for i in range(1, a + 1):
            for j in range(1, b + 1):
                if i == 1 or i == a or j == 1 or j == b:
                    outcome += "*"
                else:
                    outcome += " "
            outcome += "\n"
        return outcome