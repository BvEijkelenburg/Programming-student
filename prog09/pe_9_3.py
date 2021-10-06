#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback, collections

"""
Programming
Practice Exercise 9.3
(c) 2021 Hogeschool Utrecht,
Tijmen Muller en 
Bart van Eijkelenburg (bart.vaneijkelenburg@hu.nl)


Opdracht:
Werk onderstaande functie(s) uit.
Voeg commentaar toe om je code toe te lichten.
"""


def code(invoerstring):
    """
    Als extra beveiliging wil de NS op haar E-ticket nog een unieke code
    afbeelden. Er is gekozen voor een hele eenvoudige beveiliging: Neem de
    naam van de gebruiker+beginstation+eindstation, vertaal elk karakter
    naar ASCII en maak die waarde 3 groter.

    De “a” wordt dus een “d”, de “b” wordt een “e”, etc. De “A” wordt een “D”,
    de “W” wordt een “Z”, etc. En de spatie “ ” wordt een “#”.

    Zorg dat deze functie ieder teken van invoerstring omzet naar zijn
    rangordenummer met bibliotheekfunctie ord(), en – na er 3 bij te hebben
    opgeteld – die int-waarde weer terug vertaalt naar het bijbehorende ASCII-
    teken met bibliotheekfunctie chr().

    Voorbeeld: code("RutteAlkmaarDen Helder") levert op: UxwwhDonpdduGhq#Khoghu

    Args:
        invoerstring (str): De tekst die gecodeerd moet worden.
    Returns:
        string: De gecodeerde tekst.
    """
    return


def development_code():
    # Maak de code af; vraag de gebruiker om naam, beginstation en eindstation in te voeren.
    # Geef deze informatie als één string door aan de functie code, en print het resultaat.
    naam = input("Uw naam: ")


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


def test_code():
    case = collections.namedtuple('case', 'input expected_output')

    testcases = [case("BartUtrecht CSAmsterdam CS", "EduwXwuhfkw#FVDpvwhugdp#FV"),
                 case("RutteAlkmaarDen Helder", "UxwwhDonpdduGhq#Khoghu"),
                 case("Brian123De UithofUtrecht CS", "Euldq456Gh#XlwkriXwuhfkw#FV")]

    for test in testcases:
        __my_assert_args(code, (test.input,), test.expected_output)


def __run_tests():
    """ Test alle functies. """
    test_functions = [ test_code ]

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