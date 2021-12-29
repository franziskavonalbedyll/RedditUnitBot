CONVERT_MILES = 1.60934
CONVERT_INCH = 2.54
CONVERT_FOOT = 30.48
CONVERT_POUNDS = 0.453592


def milestoKM(miles):
    return f'{miles * CONVERT_MILES} km'


def kmtoMiles(km):
    return f'{km / CONVERT_MILES} mi'


def inchtoCm(inch):
    return f'{inch * CONVERT_INCH} cm'


def cmtoInch(cm):
    return f'{cm / CONVERT_INCH} "'


def foottoCM(foot):
    return f'{foot * CONVERT_FOOT} cm"'


def cmtoFoot(cm):
    return f'{cm / CONVERT_FOOT} ft'


def foottoMeter(foot):
    return f'{foot * CONVERT_FOOT / 100} m'


def metertoFoot(meter):
    return f'{(meter * 100) / CONVERT_FOOT} ft'


def poundstoKg(pounds):
    return f'{pounds * CONVERT_POUNDS} kg'


def kilogrammtoPounds(kilogramms):
    return f'{kilogramms / CONVERT_POUNDS} lbs'


def celsiustoFahrenheit(celsius):
    return f'{(celsius * (9 / 5)) + 32} °F'


def fahrenheittoCelsius(fahrenheit):
    return f'{(fahrenheit - 32) * 5 / 9} °C'
