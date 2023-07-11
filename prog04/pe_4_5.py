#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback, collections

"""
Programming
Oefening PROG4.5
(c) 2021 Hogeschool Utrecht,
Tijmen Muller en 
Bart van Eijkelenburg (bart.vaneijkelenburg@hu.nl)


Opdracht:
Werk onderstaande functie(s) uit.
Voeg commentaar toe om je code toe te lichten.
"""


def kwadraten_som(grondgetallen):
    """
    Bereken het kwadraat van alle positieve getallen in de meegegeven lijst met
    grondgetallen. Bepaal de som (optelling) van alle kwadraten.

    Voorbeeld: een lijst met de grondgetallen [4, 3, -5] levert als resultaat 25
               (namelijk 16 + 9, want -5 is geen positief getal).

    Args:
        grondgetallen (list): Een lijst met gehele (grond)getallen (ints)
    Returns:
        int: De som van de kwadraten van alle positieve getallen in de lijst!
    """
    return


def development_code():
    # Plaats hieronder eventueel code om je functies tussentijds te testen. Bijv:
    print("som van kwadraat van [4,3]:", kwadraten_som([4, 3]))


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


def test_kwadraten_som():
    case = collections.namedtuple('case', 'integerslist expected_output')

    testcases = [ case([-887, -901, -112, 209, 474], 268357 ), case([843, 612, 99, 857], 1829443 ),
                  case([-894, -876, 104, 954, -690], 920932 ), case([380, 852, 145, -97, 244, 516, 112, 230], 1282565 ),
                  case([-596, -998], 0 ), case([-469, 320, 305, -911, -208, -967, -998, -73], 195425 ),
                  case([-475, 220, -893, 175, -874, -236, 730], 611925 ),
                  case([915, 92, 279, 31, 373, 824, -579, 116, -181], 1756052 ),
                  case([-784, -194, 969, -584, -300, 316, -148, 756], 1610353 ),
                  case([889, -372, 187, 755, -19, -855, 626, 38, 784], 2403291 ),
                  case([-95, -821, -950, 87, 198, -15, -748, -666], 46773 ),
                  case([-671, -934, -630, -68, -164, 520], 270400 ), case([], 0 ),
                  case([767, -545, 916, -750, -475, 322], 1531029 ), case([-769, 698, 736], 1028900 ) ]

    for test in testcases:
        __my_assert_args(kwadraten_som, (test.integerslist,), test.expected_output)


def __run_tests():
    """ Test alle functies. """
    test_functions = [ test_kwadraten_som ]

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