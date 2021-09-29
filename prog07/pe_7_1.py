#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback, collections

"""
Programming
Practice Exercise 7.1
(c) 2021 Hogeschool Utrecht,
Tijmen Muller en 
Bart van Eijkelenburg (bart.vaneijkelenburg@hu.nl)


Opdracht:
Werk onderstaande functie(s) uit.
Voeg commentaar toe om je code toe te lichten.
"""


def seizoen(maand):
    """
    Het functie-resultaat is het seizoen die bij het gegeven maandnummer hoort.
    Nummers 3 t/m 5 horen bij 'lente', 9 t/m 11 bij ‘herfst’, etc.

    Maandnummers < 1 of >= 13  leveren als resultaat de string 'ongeldig'.

    Args:
        maand (int): Een maandnummer waarvan het seizoen bepaald moet worden
    Returns:
        string: Het seizoen waarin de opgegeven maand valt, of 'ongeldig'
    """
    return


def development_code():
    # Plaats hieronder eventueel code om je functies tussentijds te testen. Bijv:
    print("Seizoen van maand 2:", seizoen(2))


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


def test_seizoen():
    case = collections.namedtuple('case', 'monthnumber expected_output')

    testcases = [ case(-1, "ongeldig"), case(0, "ongeldig"), case(1, "winter"), case(2, "winter"),
                  case(3, "lente"), case(4, "lente"), case(5, "lente"), case(6, "zomer"),
                  case(7, "zomer"), case(8, "zomer"), case(9, "herfst"), case(10, "herfst"),
                  case(11, "herfst"), case(12, "winter"), case(13, "ongeldig"), case(14, "ongeldig") ]

    for test in testcases:
        __my_assert_args(seizoen, (test.monthnumber,), test.expected_output)


def __run_tests():
    """ Test alle functies. """
    test_functions = [ test_seizoen ]

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