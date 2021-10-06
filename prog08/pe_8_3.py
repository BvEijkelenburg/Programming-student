#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback, collections

"""
Programming
Practice Exercise 8.3
(c) 2021 Hogeschool Utrecht,
Tijmen Muller en 
Bart van Eijkelenburg (bart.vaneijkelenburg@hu.nl)


Opdracht:
Werk onderstaande functie(s) uit.
Voeg commentaar toe om je code toe te lichten.
"""


def hoogvliegers(dict_studenten_cijfers):
    """
    De parameter is een dictionary met studentnamen als sleutels (keys),
    en de cijfers (per student één cijfer) zijn de waarden (values). De
    functie moet een nieuwe dictionary returnen, met daarin de namen (en
    het cijfer) van studenten die een cijfer hoger dan 9,0 hebben.

    Dus {"Gerald": 9.5, "Berend": 4.5, "Bart": 1.0, "Martin": 9.0} levert
    als antwoord: {"Gerald": 9.5, "Martin": 9.0 }]

    Args:
        dict_studenten_cijfers (dict): dictionary met resultaten
    Returns:
        dict: dictionary met resultaten >= 9
    """
    return


def development_code():
    # Plaats hieronder eventueel code om je functies tussentijds te testen. Bijv:
    print("De hoogvliegers:", hoogvliegers({"Gerald": 9.5, "Berend": 4.5, "Bart": 1.0, "Martin": 9.0}))


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
    case = collections.namedtuple('case', 'result_dictionary expected_output')

    testcases = [case({"Gerald": 9.5, "Berend": 4.5, "Bart": 1.0, "Leo": 2.5, "Martin": 8.0, "Gera": 7.5, "Jan": 9.2, "David": 9.0, "Sanne": 8.2, "Brian": 10.0 }, {'Gerald': 9.5, 'Jan': 9.2, 'Brian': 10.0}),
                 case({"Gerald": 1.0, "Berend": 3.5, "Bart": 2.0, "Leo": 3.5, "Martin": 7.0, "Gera": 4.5, "Jan": 8.2, "David": 8.1, "Sanne": 9.2, "Brian": 6.9}, {'Sanne': 9.2}),
                 case({"Gerald": 9.4, "Berend": 8.5, "Bart": 4.0, "Leo": 9.5, "Martin": 5.0, "Gera": 3.5, "Jan": 6.2, "David": 4.8, "Sanne": 4.2, "Brian": 7.7}, {'Gerald': 9.4, 'Leo': 9.5}),
                 case({"Gerald": 8.7, "Berend": 9.6, "Bart": 9.0, "Leo": 8.5, "Martin": 8.9, "Gera": 9.9, "Jan": 2.2, "David": 3.2, "Sanne": 5.2, "Brian": 4.5}, {'Berend': 9.6, 'Gera': 9.9})]

    for test in testcases:
        __my_assert_args(hoogvliegers, (test.result_dictionary,), test.expected_output)


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