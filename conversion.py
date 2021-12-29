CONVERT_MILES = 1.60934
CONVERT_INCH = 2.54
CONVERT_FOOT = 30.48
CONVERT_POUNDS = 0.453592


def milestoKM(miles):
    return f'{round(miles * CONVERT_MILES, 2)} km'


def kmtoMiles(km):
    return f'{round(km / CONVERT_MILES, 2)} mi'


def inchtoCm(inch):
    return f'{round(inch * CONVERT_INCH, 2)} cm'


def cmtoInch(cm):
    return f'{round(cm / CONVERT_INCH, 2)} "'


def foottoCM(foot):
    return f'{round(foot * CONVERT_FOOT, 2)} cm"'


def foottoMeter(foot):
    return f'{round(foot * CONVERT_FOOT / 100, 2)} m'


def metertoFoot(meter):
    return f'{round((meter * 100) / CONVERT_FOOT, 2)} ft'


def poundstoKg(pounds):
    return f'{round(pounds * CONVERT_POUNDS, 2)} kg'


def kilogrammtoPounds(kilogramms):
    return f'{round(kilogramms / CONVERT_POUNDS, 2)} lbs'


def celsiustoFahrenheit(celsius):
    return f'{round((celsius * (9 / 5)) + 32, 2)} °F'


def fahrenheittoCelsius(fahrenheit):
    return f'{round((fahrenheit - 32) * 5 / 9, 2)} °C'


def grammtoPounds(gram):
    return f'{round(gram / (CONVERT_POUNDS * 1000), 2)} lbs'
