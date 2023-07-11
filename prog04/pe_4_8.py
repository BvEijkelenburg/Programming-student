#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback, collections

"""
Programming
Oefening PROG4.8
(c) 2021 Hogeschool Utrecht,
Tijmen Muller en 
Bart van Eijkelenburg (bart.vaneijkelenburg@hu.nl)


Opdracht:
Werk onderstaande functie(s) uit.
Voeg commentaar toe om je code toe te lichten.
"""


def convert(celcius_temp):
    """
    Zet de gegeven temperatuur in graden Celsius om naar graden Fahrenheit.
    Je kunt de temperatuur in Fahrenheit berekenen met de formule:

        T°F = T°C × 1.8 + 32.

    Dus 25 °C = 25 × 1.8 + 32 = 77 °F.

    Args:
        celcius_temp (int): De temperatuur in graden Celsius
    Returns:
        float: De berekende temperatuur in graden Fahrenheit
    """
    return


def table():
    """
    Plaats met een for-loop de waarden -30°C t/m 40°C (in stappen van 10 graden) in
    een string, en zet de temperatuur in Fahrenheit ernaast. Gebruik voor de berekening
    de functie convert(..)!

    Zorg middels een geformatteerde output voor dezelfde precisie en uitlijning als
    het voorbeeld hieronder.

          F       C
        -22.0   -30.0
         -4.0   -20.0
         14.0   -10.0
         32.0     0.0
         50.0    10.0
         68.0    20.0
         86.0    30.0
        104.0    40.0

    Let op: deze functie wordt al aangeroepen vanuit de functie 'development_code()'

    Returns:
        string: De gecreëerde string met de tabel
    """
    return


def development_code():
    # Plaats hieronder eventueel code om je functies tussentijds te testen. Bijv:
    print("Conversietabel graden Celsius:", table(), sep="\n")


def module_runner():
    development_code()      # Comment deze regel om je 'development_code' uit te schakelen
    __run_tests()           # Comment deze regel om de HU-tests uit te schakelen


"""
==========================[ HU TESTRAAMWERK ]================================
Hieronder staan de tests voor je code -- daaraan mag je niets wijzigen!
"""


def __my_assert_args(function, args, expected_output, check_type=False):
    """
    Controleer of gegeven functie met gegeven argumenten het verwachte resultaat oplevert.
    Optioneel wordt ook het return-type gecontroleerd.
    """
    argstr = str(args).replace(',)', ')')
    output = function(*args)

    # Controleer eerst het return-type (optioneel)
    if check_type:
        msg = f"Fout: {function.__name__}{argstr} geeft geen {type(expected_output).__name__} terug als return-type"
        assert type(output) is type(expected_output), msg

    # Controleer of de functie-uitvoer overeenkomt met de gewenste uitvoer
    if str(expected_output) == str(output):
        msg = f"Fout: {function.__name__}{argstr} geeft {output} ({type(output).__name__}) " \
              f"in plaats van {expected_output} (type {type(expected_output).__name__})"
    else:
        msg = f"Fout: {function.__name__}{argstr} geeft {output} in plaats van {expected_output}"

    if type(expected_output) is float and isinstance(output, (int, float, complex)):
        # Vergelijk bij float als return-type op 7 decimalen om afrondingsfouten te omzeilen
        assert round(output - expected_output, 7) == 0, msg
    else:
        assert output == expected_output, msg


def test_convert():
    case = collections.namedtuple('case', 'celcius expected_output')

    testcases = [ case(-100, -148.0), case(-99, -146.2), case(-98, -144.4), case(-97, -142.6), case(-96, -140.8),
                  case(-95, -139.0),  case(-94, -137.2), case(-93, -135.4), case(-92, -133.6), case(-91, -131.8),
                  case(-90, -130.0),  case(-89, -128.2), case(-88, -126.4), case(-87, -124.6), case(-86, -122.8),
                  case(-85, -121.0),  case(-84, -119.2), case(-83, -117.4), case(-82, -115.6), case(-81, -113.8),
                  case(-80, -112.0),  case(-79, -110.2), case(-78, -108.4), case(-77, -106.6), case(-76, -104.8),
                  case(-75, -103.0),  case(-74, -101.2), case(-73, -99.4),  case(-72, -97.6),  case(-71, -95.8),
                  case(-70, -94.0),   case(-69, -92.2),  case(-68, -90.4),  case(-67, -88.6),  case(-66, -86.8),
                  case(-65, -85.0),   case(-64, -83.2),  case(-63, -81.4),  case(-62, -79.6),  case(-61, -77.8),
                  case(-60, -76.0),   case(-59, -74.2),  case(-58, -72.4),  case(-57, -70.6),  case(-56, -68.8),
                  case(-55, -67.0),   case(-54, -65.2),  case(-53, -63.4),  case(-52, -61.6),  case(-51, -59.8),
                  case(-50, -58.0),   case(-49, -56.2),  case(-48, -54.4),  case(-47, -52.6),  case(-46, -50.8),
                  case(-45, -49.0),   case(-44, -47.2),  case(-43, -45.4),  case(-42, -43.6),  case(-41, -41.8),
                  case(-40, -40.0),   case(-39, -38.2),  case(-38, -36.4),  case(-37, -34.6),  case(-36, -32.8),
                  case(-35, -31.0),   case(-34, -29.2),  case(-33, -27.4),  case(-32, -25.6),  case(-31, -23.8),
                  case(-30, -22.0),   case(-29, -20.2),  case(-28, -18.4),  case(-27, -16.6),  case(-26, -14.8),
                  case(-25, -13.0),   case(-24, -11.2),  case(-23, -9.4),   case(-22, -7.6),   case(-21, -5.8),
                  case(-20, -4.0),    case(-19, -2.2),   case(-18, -0.4),   case(-17, 1.4),    case(-16, 3.2),
                  case(-15, 5.0),     case(-14, 6.8),    case(-13, 8.6),    case(-12, 10.4),   case(-11, 12.2),
                  case(-10, 14.0),    case(-9, 15.8),    case(-8, 17.6),    case(-7, 19.4),    case(-6, 21.2),
                  case(-5, 23.0),     case(-4, 24.8),    case(-3, 26.6),    case(-2, 28.4),    case(-1, 30.2),
                  case(0, 32.0),      case(1, 33.8),     case(2, 35.6),     case(3, 37.4),     case(4, 39.2),
                  case(5, 41.0),      case(6, 42.8),     case(7, 44.6),     case(8, 46.4),     case(9, 48.2),
                  case(10, 50.0),     case(11, 51.8),    case(12, 53.6),    case(13, 55.4),    case(14, 57.2),
                  case(15, 59.0),     case(16, 60.8),    case(17, 62.6),    case(18, 64.4),    case(19, 66.2),
                  case(20, 68.0),     case(21, 69.8),    case(22, 71.6),    case(23, 73.4),    case(24, 75.2),
                  case(25, 77.0),     case(26, 78.8),    case(27, 80.6),    case(28, 82.4),    case(29, 84.2),
                  case(30, 86.0),     case(31, 87.8),    case(32, 89.6),    case(33, 91.4),    case(34, 93.2),
                  case(35, 95.0),     case(36, 96.8),    case(37, 98.6),    case(38, 100.4),   case(39, 102.2),
                  case(40, 104.0),    case(41, 105.8),   case(42, 107.6),   case(43, 109.4),   case(44, 111.2),
                  case(45, 113.0),    case(46, 114.8),   case(47, 116.6),   case(48, 118.4),   case(49, 120.2),
                  case(50, 122.0),    case(51, 123.8),   case(52, 125.6),   case(53, 127.4),   case(54, 129.2),
                  case(55, 131.0),    case(56, 132.8),   case(57, 134.6),   case(58, 136.4),   case(59, 138.2),
                  case(60, 140.0),    case(61, 141.8),   case(62, 143.6),   case(63, 145.4),   case(64, 147.2),
                  case(65, 149.0),    case(66, 150.8),   case(67, 152.6),   case(68, 154.4),   case(69, 156.2),
                  case(70, 158.0),    case(71, 159.8),   case(72, 161.6),   case(73, 163.4),   case(74, 165.2),
                  case(75, 167.0),    case(76, 168.8),   case(77, 170.6),   case(78, 172.4),   case(79, 174.2),
                  case(80, 176.0),    case(81, 177.8),   case(82, 179.6),   case(83, 181.4),   case(84, 183.2),
                  case(85, 185.0),    case(86, 186.8),   case(87, 188.6),   case(88, 190.4),   case(89, 192.2),
                  case(90, 194.0),    case(91, 195.8),   case(92, 197.6),   case(93, 199.4),   case(94, 201.2),
                  case(95, 203.0),    case(96, 204.8),   case(97, 206.6),   case(98, 208.4),   case(99, 210.2) ]

    for test in testcases:
        __my_assert_args(convert, (test.celcius,), test.expected_output)


def __run_tests():
    """ Test alle functies. """
    test_functions = [ test_convert ]

    try:
        for test_function in test_functions:
            func_name = test_function.__name__[5:]

            print(f"\n======= Test output '{test_function.__name__}()' =======")
            test_function()
            print(f"Je functie {func_name} werkt goed!")

        print("\nGefeliciteerd, alles lijkt te werken!")

    except AssertionError as e:
        print(e.args[0])
    except Exception as e:
        print(f"Fout: er ging er iets mis! Python-error: \"{e}\"")
        print(traceback.format_exc())


if __name__ == '__main__':
    module_runner()