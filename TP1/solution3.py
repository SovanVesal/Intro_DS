#convert the temperature

def celsius_to_fahrenheit(celsius, round_to=1):
    temp = celsius * 9/5 + 32
    return temp
def fahrenheit_t0_celsius(fahrenhiet,round_to=1):
    temp = (fahrenhiet - 32) * 5/9
    return temp

print("\n  °C  |  °F")
print(("------+--------"))
for celsius in range (0,101,20):
    print("   ",celsius,"|",celsius_to_fahrenheit(celsius))
print("98.6°F   =",fahrenheit_t0_celsius(98.6),"°C")
print("37°C     =",celsius_to_fahrenheit(37),"°F")


    

