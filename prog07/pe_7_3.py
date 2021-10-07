#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback, collections

"""
Programming
Practice Exercise 7.2
(c) 2021 Hogeschool Utrecht,
Tijmen Muller en 
Bart van Eijkelenburg (bart.vaneijkelenburg@hu.nl)


Opdracht:
Werk onderstaande functie(s) uit.
Voeg commentaar toe om je code toe te lichten.
"""


def gemiddelde_per_student(studentencijfers):
    """
    Deze functie ontvangt een lijst studentcijfers, waarbij de lijst per
    student een sublijst bevat met drie resultaten. Voor een resultaat geldt dat
    0 <= resultaat <= 100). Voorbeeld:

        [ [17, 16, 30], [18, 92, 88] ]

    Bepaal per student het gemiddelde van de drie resultaten, en plaats deze
    gemiddelden in een één-dimensionale lijst. Houdt bij deze lijst met gemiddelden
    dezelfde volgorde aan als in de lijst met studentencijfers! Het resultaat van
    deze functie bij de gegeven voorbeeldlijst zou '[ 21.0, 66.0 ]' zijn.

    Args:
        studentencijfers (list): studentcijfers met per student een sublijst met  drie resultaten
    Returns:
        list: per student het gemiddelde cijfer van de drie resultaten
    """
    return


def gemiddelde_van_alle_studenten(studentencijfers):
    """
    Deze functie ontvangt een lijst studentcijfers, waarbij de lijst per
    student een sublijst bevat met drie resultaten. Voor een resultaat geldt dat
    0 <= resultaat <= 100). Voorbeeld:

        [ [17, 16, 30], [18, 92, 88] ]

    Bepaal het totaalgemiddelde van van alle resultaten van alle studenten.

    Args:
        studentencijfers (list): studentcijfers met per student een sublijst met  drie resultaten
    Returns:
        float: het totaalgemiddelde van alle resultaten van alle studenten
    """
    return


def development_code():
    # Plaats hieronder eventueel code om je functies tussentijds te testen. Bijv:
    print("Gemiddelde van [[17, 16, 30], [18, 92, 88]]:", gemiddelde_per_student([[17, 16, 30], [18, 92, 88]]))


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


def test_gemiddelde_per_student():
    for test in testcases():
        __my_assert_args(gemiddelde_per_student, (test.studentgradeslist,), test.average_per_student)


def test_gemiddelde_van_alle_studenten():
    for test in testcases():
        __my_assert_args(gemiddelde_van_alle_studenten, (test.studentgradeslist,), test.overall_average)


def testcases():
    case = collections.namedtuple('case', 'studentgradeslist overall_average average_per_student')

    return [ case(([17, 15, 30], [19, 46, 75]), 33.666666666666664, [20.666666666666668, 46.666666666666664]),
             case(([31, 96, 54], [16, 37, 56], [94, 64, 55], [41, 36, 66], [51, 16, 28], [99, 96, 45], [69, 38, 63], [52, 73, 72]), 56.16666666666667, [60.333333333333336, 36.333333333333336, 71.0, 47.666666666666664, 31.666666666666668, 80.0, 56.666666666666664, 65.66666666666667]),
             case(([93, 48, 36],), 59.0, [59.0]),
             case(([33, 60, 17], [84, 12, 50], [34, 77, 94], [88, 72, 24]), 53.75, [36.666666666666664, 48.666666666666664, 68.33333333333333, 61.333333333333336]),
             case(([71, 29, 77], [17, 32, 82], [83, 14, 90], [31, 58, 66], [14, 39, 72], [53, 53, 41], [19, 84, 67], [66, 77, 81], [46, 32, 65]), 54.03703703703704, [59.0, 43.666666666666664, 62.333333333333336, 51.666666666666664, 41.666666666666664, 49.0, 56.666666666666664, 74.66666666666667, 47.666666666666664]),
             case(([99, 46, 74], [44, 35, 27], [100, 17, 41], [24, 71, 48], [12, 41, 87], [31, 59, 56], [80, 32, 20]), 49.714285714285715, [73.0, 35.333333333333336, 52.666666666666664, 47.666666666666664, 46.666666666666664, 48.666666666666664, 44.0]),
             case(([35, 52, 64], [40, 48, 42], [62, 22, 17], [42, 16, 78], [82, 85, 14], [23, 54, 43], [49, 32, 13], [96, 71, 95], [80, 25, 54]), 49.407407407407405, [50.333333333333336, 43.333333333333336, 33.666666666666664, 45.333333333333336, 60.333333333333336, 40.0, 31.333333333333332, 87.33333333333333, 53.0]),
             case(([80, 55, 45], [25, 36, 39], [84, 69, 94], [60, 63, 66], [31, 61, 34], [33, 30, 51]), 53.111111111111114, [60.0, 33.333333333333336, 82.33333333333333, 63.0, 42.0, 38.0]),
             case(([71, 91, 42], [41, 14, 39], [41, 72, 70], [30, 14, 58], [20, 15, 57], [46, 24, 85], [74, 92, 61], [36, 27, 30]), 47.916666666666664, [68.0, 31.333333333333332, 61.0, 34.0, 30.666666666666668, 51.666666666666664, 75.66666666666667, 31.0]),
             case(([11, 74, 84], [35, 66, 26], [23, 90, 46], [10, 21, 81], [79, 51, 12], [44, 23, 38]), 45.22222222222223, [56.333333333333336, 42.333333333333336, 53.0, 37.333333333333336, 47.333333333333336, 35.0]) ]


def __run_tests():
    """ Test alle functies. """
    test_functions = [ test_gemiddelde_per_student, test_gemiddelde_van_alle_studenten ]

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