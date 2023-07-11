#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback, builtins, sys

"""
Programming
Oefening PROG5.2
(c) 2021 Hogeschool Utrecht,
Tijmen Muller en 
Bart van Eijkelenburg (bart.vaneijkelenburg@hu.nl)


Opdracht:
Werk onderstaande functie(s) uit.
Voeg commentaar toe om je code toe te lichten.
"""


def pretty_print():
    """
    Lees een bestand met klantenkaartnummers en namen uit,
    en plaats deze informatie netjes leesbaar in een string.

    Uitgangspunt: het bestand bevat per regel de gegevens van 1
    kaart; telkens eerst het nummer, dan een komma, en dan de naam
    van de klant. Elke regel sluit af met een enter. Maak voor deze
    functie eerst zo'n  bestand aan. Bijv:

        325255, Jan Jansen
        334343, Erik Materus
        235434, Ali Ahson
        645345, Eva Versteeg
        534545, Jan de Wilde
        345355, Henk de Vries

    Bij deze gegevens zou de volgende string geproduceerd moeten worden:

        Jan Jansen heeft kaartnummer: 325255
        Erik Materus heeft kaartnummer: 334343
        Ali Ahson heeft kaartnummer: 235434
        Eva Versteeg heeft kaartnummer: 645345
        Jan de Wilde heeft kaartnummer: 534545
        Henk de Vrie heeft kaartnummer: 345355

    Vanzelfsprekend zou de functie ook moeten werken met bestanden
    met andere kaartgegevens!

    Returns:
        string: De string met de kaartgegevens
    """
    return


def development_code():
    # Plaats hieronder eventueel code om je functies tussentijds te testen. Bijv:
    print("Klanten uit bestand:\n", pretty_print(), sep="")


def module_runner():
    development_code()      # Comment deze regel om je 'development_code' uit te schakelen
    __run_tests()           # Comment deze regel om de HU-tests uit te schakelen


"""
==========================[ HU TESTRAAMWERK ]================================
Hieronder staan de tests voor je code -- daaraan mag je niets wijzigen!
"""


def __my_test_file():
    return "pe_6_2_generated.txt"


def __create_fake_open(original_open):
    def fake_open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        return original_open(__my_test_file(), mode=mode, buffering=buffering, encoding=encoding, errors=errors,
                      newline=newline, closefd=closefd, opener=opener)
    return fake_open


def test_pretty_print():
    cards = { 455684: "Erik Materus",
              334343: "Jan Jansen",
              234646: "Henk de Vries",
              645345: "Jan de Wilde",
              538795: "Eva Versteeg",
              123355: "Ali Ahson" }

    print(f"Voor de test wordt bestand {__my_test_file()} aangemaakt, met de volgende inhoud: ")
    try:
        with open(__my_test_file(), 'w') as dummy_file:
            for number, name in cards.items():
                dummy_file.write(f"{number}, {name}\n")
                print(f"{number}, {name}\n", end="")
    except:
        print(f"Fout: bestand {__my_test_file()} kon niet worden aangemaakt. Python-error:")
        print(traceback.format_exc())
        sys.exit()

    print("\nKlaar... de test wordt nu uitgevoerd...")

    original_open = builtins.open
    builtins.open = __create_fake_open(original_open)

    function_result = pretty_print()
    builtins.open = original_open

    assert function_result is not None, f"Fout: pretty_print() geeft None terug in plaats van string"
    assert isinstance(function_result, str), f"Fout: pretty_print() geeft geen string terug als return-type"

    for number, name in cards.items():
        expected_in_result = f"{name} heeft kaartnummer: {number}"
        msg = f"Fout: returnwaarde van pretty_print() bevat niet de tekst '{expected_in_result}'"
        assert expected_in_result in function_result, msg


def __run_tests():
    """ Test alle functies. """
    test_functions = [ test_pretty_print ]

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