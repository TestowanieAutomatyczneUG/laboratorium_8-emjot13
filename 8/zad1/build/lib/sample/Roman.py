class Roman:
    def roman(self, num):
        convert_table = [[1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"], [90, "XC"], [50, "L"],
                         [40, "XL"],
                         [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]]
        res = ""
        if num == 0:
            raise ValueError("Romans did not use number 0")
        for value, text in convert_table:
            freq = num // value
            num = num % value
            res += text * freq