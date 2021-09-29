#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback, collections

"""
Programming
Practice Exercise 5.2
(c) 2021 Hogeschool Utrecht,
Tijmen Muller en 
Bart van Eijkelenburg (bart.vaneijkelenburg@hu.nl)


Opdracht:
Werk onderstaande functie(s) uit.
Voeg commentaar toe om je code toe te lichten.
"""


def som(getallenLijst):
    """
    Tel de getallen in de lijst bij elkaar op!

    Args:
        getallenLijst (list): Een lijst met gehele getallen (int)
    Returns:
        int: De som (optelling) van de getallen in de lijst
    """
    return


def development_code():
    # Plaats hieronder eventueel code om je functies tussentijds te testen. Bijv:
    print("resultaat van optelling:", som([10, 8, 7]))


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


def test_som():
    case = collections.namedtuple('case', 'integerslist expected_output')

    testcases = [ case([984], 984), case([-353, 736, -230], 153), case([], 0), case([-344, -257, -780], -1381),
                  case([730, -241, 722, 344, -432], 1123), case([881, -50, -798], 33), case([976], 976),
                  case([114, -209, 500], 405), case([], 0), case([-497, -825, 992, -657], -987),
                  case([753, 74, 668], 1495), case([-999], -999), case([-235, -415], -650), case([-847, 831], -16),
                  case([303, 300, -652, 7, -653], -695), case([-684, 157, 718, 330, -857], -336), case([-773], -773),
                  case([-10], -10), case([], 0), case([-999], -999), case([-737, 716, -642], -663),
                  case([284, -596, -628, 409], -531), case([-307, 834], 527), case([-840], -840),
                  case([371, -715, -502], -846), case([-78, -267], -345), case([97, 383], 480), case([935], 935),
                  case([-500, 988, -651, 959], 796), case([-406, -990, -659], -2055) ]

    for test in testcases:
        __my_assert_args(som, (test.integerslist,), test.expected_output)


def __run_tests():
    """ Test alle functies. """
    test_functions = [ test_som ]

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