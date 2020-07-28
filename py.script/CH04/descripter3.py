class Celsius:
    def __innit__(self):
        pass
    def to_fahrenheit(self):
        return (self._temperature *1.8) +32

    @property #get역할
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter #set역할
    def temperature(self, value):
        if value< -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

#main
temp = Celsius()
temp.temperature =40
print(temp.to_fahrenheit())
print(temp.temperature)
temp.temperature = 100
print(temp.to_fahrenheit())