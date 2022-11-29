def get_max():
    grades = [9.6, 9.2, 9.7]
    maxVal = max(grades)
    minVal = min(grades)
    return maxVal, minVal


maxVal = get_max()[0]
minVal = get_max()[1]
print(f"Max: {maxVal}, Min: {minVal}")

def get_maximum():
    celsius = [14, 15.1, 12.3]
    maximum = max(celsius)
    return maximum


celsius = get_maximum()
fahrenheit = celsius * 1.8 + 32
print(fahrenheit)