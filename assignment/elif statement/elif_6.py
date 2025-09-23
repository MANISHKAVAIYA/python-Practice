# TODO 6. Check if a temperature is cold (<15°C), moderate (15-30°C), or hot (>30°C). 

temperature = int(input("Enter the temperature : "))

if temperature < 15:
    print(f"temperature {temperature}°C is cold ")
elif 15 <= temperature <= 30:
    print(f"temperature {temperature}°C is moderate")
elif temperature > 30:
    print(f"temperature {temperature}°C is hot")
else:
    print("Invalid temperature")