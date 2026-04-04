def check_trigger(aqi, rain):
    if aqi > 300 or rain > 50:
        return True
    return False