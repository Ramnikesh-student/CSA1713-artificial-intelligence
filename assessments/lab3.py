def temperature_control(temp):
    # Membership values for Cold, Warm and Hot
    cold = max(0, min(1, (25 - temp) / 15))
    warm = max(0, 1 - abs(temp - 25) / 15)
    hot = max(0, min(1, (temp - 25) / 15))

    print("Temperature:", temp, "°C")
    print("Cold Membership:", round(cold, 2))
    print("Warm Membership:", round(warm, 2))
    print("Hot Membership:", round(hot, 2))

    # Determine fan speed using fuzzy rules
    fan_speed = (cold * 20 + warm * 50 + hot * 100) / (cold + warm + hot)

    print("Fan Speed:", round(fan_speed, 2), "%")

    if fan_speed <= 35:
        print("Fan Status: Slow")
    elif fan_speed <= 70:
        print("Fan Status: Medium")
    else:
        print("Fan Status: Fast")


temperature = float(input("Enter temperature: "))
temperature_control(temperature)
