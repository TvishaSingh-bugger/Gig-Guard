def calculate_premium(aqi, rain):
    risk = 0

    if aqi > 300:
        risk += 0.4
    if rain > 50:
        risk += 0.4

    return 20 + int(risk * 100)