class RomanConverter:
    def __init__(self, number):
        self.number = number

    def to_roman(self):
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        num = self.number
        roman = ""
        for i in range(len(val)):
            roman += syms[i] * (num // val[i])
            num %= val[i]
        return roman


# Main program
n = int(input("Enter a number (1-3999): "))
converter = RomanConverter(n)
print("Roman numeral:", converter.to_roman())