#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback, collections

"""
Programming
Oefening PROG4.6
(c) 2021 Hogeschool Utrecht,
Tijmen Muller en 
Bart van Eijkelenburg (bart.vaneijkelenburg@hu.nl)


Opdracht:
Werk onderstaande functie(s) uit.
Voeg commentaar toe om je code toe te lichten.
"""


def wijzig(letterlijst):
    """
    Deze functie heeft één parameter: letterlijst. Zorg dat de functie de lijst
    leegt en de letters [ ‘d’, ‘e’, ‘f’ ] toevoegt aan de lijst.

    Args:
        letterlijst (list): Een lijst met een aantal losse karakters
    Returns:
        Er is geen return-waarde!
    """
    return


def development_code():
    # Plaats hieronder eventueel code om je functies tussentijds te testen. Bijv:
    lijst = ['a', 'b', 'c']
    print(lijst)
    wijzig(lijst)
    print(lijst)


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


def test_wijzig():
    case = collections.namedtuple('case', 'characterlist expected_output')

    testcases = [ case(['a', 'b', 'c'], None),
                  case([], None) ]

    for test in testcases:
        tmp_list = test.characterlist.copy()

        __my_assert_args(wijzig, (test.characterlist,), test.expected_output)

        check = 'd' in test.characterlist and 'e' in test.characterlist and 'f' in test.characterlist
        msg = f"Fout: Na functie wijzig({tmp_list}) bevat de meegegeven lijst {test.characterlist} in plaats van {['d', 'e', 'f']}"

        assert check, msg


def __run_tests():
    """ Test alle functies. """
    test_functions = [ test_wijzig ]

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