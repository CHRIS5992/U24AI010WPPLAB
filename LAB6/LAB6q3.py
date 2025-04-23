class Converter:
    def __init__(self, length, unit):
        self.length = length
        self.unit = unit.lower()
        self.conversion_rates = {
            "inches": 1,
            "feet": 1 / 12,
            "yards": 1 / 36,
            "miles": 1 / 63360,
            "millimeters": 25.4,
            "centimeters": 2.54,
            "meters": 0.0254,
            "kilometers": 0.0000254
        }

    def convert_to(self, target_unit):
        target_unit = target_unit.lower()
        if target_unit in self.conversion_rates:
            return self.length * self.conversion_rates[self.unit] / self.conversion_rates[target_unit]
        else:
            return "Invalid unit!"


length = float(input("Enter the length: "))
unit = input("Enter the current unit (inches, feet, yards, miles, millimeters, centimeters, meters, kilometers): ")
target_unit = input("Enter the unit to convert to: ")

c = Converter(length, unit)
result = c.convert_to(target_unit)
print(f"{length} {unit} is equal to {result} {target_unit}")
