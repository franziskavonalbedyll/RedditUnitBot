import re
from enum import Enum

import conversion as conv


# examples = ["i have 5kgs of potatoes and 10 miles", "5 kg", "2 lbs", "10929092°C", "13 °C", "kg 192 ", "19.991 g",'292"']


class Units(Enum):
    KILOGRAM = ["kg", "KG", "Kilo", "Kgs", "kgs"]
    GRAM = ["g", "gram"]
    LBS = ["lbs"]
    MILES = ["mi", "MI", "miles"]
    KILOMETER = ["km", "KM"]
    INCH = ["in", "\""]
    FOOT = ["ft", "\'"]
    CM = ["cm", "CM"]
    CELSIUS = ["°C", "Celsius"]
    FAHRENHEIT = ["°F", "Fahrenheit"]

    @staticmethod
    def get_units():
        return [unit for unit_list in Units for unit in unit_list.value]


class Processor:
    PATTERN = r"(?P<value>\d+\.?,?\d*) ?(?P<potential_unit>[a-zA-Z°?\'?\"?]*)"

    @staticmethod
    def get_mentions_of_units(text: str) -> list:
        """ Takes a text unit as input and returns mentions of units and their respective value"""
        return [(float(val), str(unit)) for val, unit in re.findall(Processor.PATTERN, text) if
                unit in Units.get_units()]

    @staticmethod
    def convert_units(matches: list) -> list:
        conv_matches = []
        for value, unit in matches:
            if unit in Units.KILOGRAM.value:
                conv_matches.append(conv.kilogrammtoPounds(value))
            elif unit in Units.LBS.value:
                conv_matches.append(conv.poundstoKg(value))
            elif unit in Units.GRAM.value:
                conv_matches.append(conv.grammtoPounds(value))
            elif unit in Units.MILES.value:
                conv_matches.append(conv.milestoKM(value))
            elif unit in Units.KILOMETER.value:
                conv_matches.append(conv.kmtoMiles(value))
            elif unit in Units.INCH.value:
                conv_matches.append(conv.inchtoCm(value))
            elif unit in Units.FOOT.value:
                conv_matches.append(conv.foottoCM(value))
            elif unit in Units.CM.value:
                conv_matches.append(conv.cmtoInch(value))
            elif unit in Units.CELSIUS.value:
                conv_matches.append(conv.celsiustoFahrenheit(value))
            elif unit in Units.FAHRENHEIT.value:
                conv_matches.append(conv.fahrenheittoCelsius(value))
        return conv_matches

    @staticmethod
    def get_answer_text(original_text: str) -> str:
        """This method takes a text, searches for mentions of units, and if found, creates an answer text with the
        converted units. If no units are found, it returns an empty string"""
        original_units = Processor.get_mentions_of_units(original_text)
        if not original_units: return None
        converted_units = Processor.convert_units(original_units)
        conversions = ""
        for original_unit, converted_unit in zip(original_units, converted_units):
            conversions += f'{str(original_unit[0])} {original_unit[1]} equals {converted_unit}.\n'
        return conversions
