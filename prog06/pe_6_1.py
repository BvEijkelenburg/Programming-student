#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback, collections

"""
Programming
Oefening PROG6.1
(c) 2021 Hogeschool Utrecht,
Tijmen Muller en 
Bart van Eijkelenburg (bart.vaneijkelenburg@hu.nl)


Opdracht:
Werk onderstaande functie(s) uit.
Voeg commentaar toe om je code toe te lichten.
"""


def analyzer(integerstring):
    """
    Deze functie ontvangt een string met gehele getallen (parameter integerstring),
    waarbij de getallen gescheiden zijn door streepjes Voorbeeld:

     "5-9-7-1-7-8-3-2-4-8-7-9"

    De string moet in een lijst van getallen (ints) gesplitst worden. Sorteer de
    lijst van klein naar groot. Return daarna een tuple met de volgende informatie:

        ( <gesorteerde lijst>, <grootste waarde>, <kleinste waarde>,
                <aantal getallen>, <som van de getallen>, <gemiddelde> )

    Args:
        integerstring (string): Een string met gehele getallen, gescheiden door streepjes ('-')
    Returns:
        tuple: met daarin de berekende waarden zoals hierboven beschreven
    """
    return


def development_code():
    # Plaats hieronder eventueel code om je functies tussentijds te testen. Bijv:
    resultaat = analyzer("5-9-7-1-7-8-3-2-4-8-7-9")
    print("Gesorteerde list van ints:", " <vervang dit door de gesorteerde lijst van getallen> ")
    print("Grootste getal:", " <vervang dit door het grootste getal> ", "en Kleinste getal:", " <vervang dit door het kleinste getal> ")
    print("Aantal getallen:", " <vervang dit door 'aantal getallen'> ", "en Som van de getallen:", " <vervang dit door de som> ")
    print("Gemiddelde:", " <vervang dit door het gemiddelde> ")



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


def test_analyzer():
    case = collections.namedtuple('case', 'integerstring expected_output')
    result = collections.namedtuple('result', "sorted_list largest smallest count sum average")

    testcases = [ case("9-9-6-1-6-9-6-5-9-6-3-3", result([ 1, 3, 3, 5, 6, 6, 6, 6, 9, 9, 9, 9 ], 9, 1, 12, 72, 6.0)),
                  case("6-4-0-8-0-6-2-7-5-8", result([ 0, 0, 2, 4, 5, 6, 6, 7, 8, 8 ], 8, 0, 10, 46, 4.6)),
                  case("1-4-6-6-2-5", result([ 1, 2, 4, 5, 6, 6 ], 6, 1, 6, 24, 4.0)),
                  case("3-1", result([ 1, 3 ], 3, 1, 2, 4, 2.0)),
                  case("3-2-1-4-7", result([ 1, 2, 3, 4, 7 ], 7, 1, 5, 17, 3.4)),
                  case("4-3-2-7", result([ 2, 3, 4, 7 ], 7, 2, 4, 16, 4.0)),
                  case("6-4-2-0-7-6-7-4-6-2-0-4-4", result([ 0, 0, 2, 2, 4, 4, 4, 4, 6, 6, 6, 7, 7 ], 7, 0, 13, 52, 4.0)),
                  case("3-1-0-5-9-4-1-9-2-0-3-5", result([ 0, 0, 1, 1, 2, 3, 3, 4, 5, 5, 9, 9 ], 9, 0, 12, 42, 3.5)),
                  case("9-0-1-0-0-9-8-4", result([ 0, 0, 0, 1, 4, 8, 9, 9 ], 9, 0, 8, 31, 3.875)),
                  case("5-9", result([ 5, 9 ], 9, 5, 2, 14, 7.0)) ]

    for test in testcases:
        try:
            __my_assert_args(analyzer, (test.integerstring,), tuple(test.expected_output))
        except AssertionError as ae:
            raise AssertionError(f"{ae.args[0]}\n\n -> toelichting op verwachte waarden: {str(test.expected_output)[6:]}") from ae


def __run_tests():
    """ Test alle functies. """
    test_functions = [ test_analyzer ]

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