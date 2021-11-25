
CONVERT_MILES = 1.60934
CONVERT_INCH = 2.54
CONVERT_FOOT = 30.48
CONVERT_POUNDS = 0.453592

def milestoKM(miles):
    return miles*CONVERT_MILES
def kmtoMiles(km):
    return km/CONVERT_MILES
def inchtoCm(inch):
    return inch*CONVERT_INCH
def cmtoInch(cm):
    return cm/CONVERT_INCH
def foottoCM(foot):
    return foot*CONVERT_FOOT
def cmtoFoot(cm):
    return cm/CONVERT_FOOT
def foottoMeter(foot):
    return (foot*CONVERT_FOOT)/100
def metertoFoot(meter):
    return (meter*100)/CONVERT_FOOT
def poundstoKg(pounds):
    return pounds * CONVERT_POUNDS
def kilogrammtoPounds(kilogramms):
    return kilogramms / CONVERT_POUNDS
def celsiustoFahrenheit(celsius):
    return (celsius * (9/5)) + 32
def fahrenheittoCelsius(fahrenheit):
    return (fahrenheit - 32) * 5/9