#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback, collections, random

"""
Programming
Practice Exercise 9.2
(c) 2021 Hogeschool Utrecht,
Tijmen Muller en 
Bart van Eijkelenburg (bart.vaneijkelenburg@hu.nl)


Opdracht:
Werk onderstaande functie(s) uit.
Voeg commentaar toe om je code toe te lichten.
"""


def monopolyworp():
    """
    Simuleer het gooien van twee dobbelstenen voor het spel Monopoly. Als
    beide stenen dezelfde waarde hebben, simuleer je nogmaals een worp. Na
    driemaal dubbel moet de speler naar de gevangenis!

    Print de worpen èn return de gegooide worp(en) als lijst of tuple. In
    de lijst plaats je per worp ook weer een tuple of lijst met de gegooide
    waarden. Mogelijke returnwaarden van de functie:

    [(1, 2)] - één keer gegooid, dus een lijst met één worp (als tuple)
    [(4, 4), (4, 5)] - twee keer gegooid (eerste keer dubbel)
    [(3, 3), (4, 4), (1, 1)] - drie keer gegooid (alle worpen dubbel)

    Returns:
        list/tuple: verzameling van alle gesimuleerde worpen.
    """
    return

def development_code():
    # Plaats hieronder eventueel code om je functies tussentijds te testen. Bijv:
    print("Monopolyworp(en): ", monopolyworp())


def module_runner():
    development_code()      # Comment deze regel om je 'development_code' uit te schakelen
    __run_tests()           # Comment deze regel om de HU-tests uit te schakelen


"""
==========================[ HU TESTRAAMWERK ]================================
Hieronder staan de tests voor je code -- daaraan mag je niets wijzigen!
"""


def __check_dices(result, dices):
    msg = f"Fout: je functie monopolyworp() geeft wel een {type(result).__name__}, maar een worp moet daarin " \
          f"weer als list of tuple geplaatst worden. Bijv. [(2,3)]. Functie monopolyworp() geeft nu: {result}"
    assert isinstance(dices, (tuple, list)), msg
    assert len(dices) == 2, f'Fout: per worp moeten twee dobbelstenen gegooid worden, nu gevonden: {dices}'

    msg = "Fout: type van dobbelsteenwaarde {} moet int zijn, nu gevonden: {} in {}"
    assert isinstance(dices[0], int), msg.format(dices[0], type(dices[0]).__name__, result)
    assert isinstance(dices[1], int), msg.format(dices[1], type(dices[1]).__name__, result)
    assert 0 < dices[0] <= 6, f'Fout: ongeldige dobbelsteen waarde: {dices[0]} in {result}'
    assert 0 < dices[1] <= 6, f'Fout: ongeldige dobbelsteen waarde: {dices[1]} in {result}'


def test_monopolyworp():
    for i in range(1000):
        result = monopolyworp()
        assert isinstance(result, (tuple, list)), f"Fout: monopolyworp() levert {result} ipv een tuple of list op!"

        assert len(result) > 0, f'Fout: monopolyworp geeft {result}, maar er moet minstens één keer een worp plaatsvinden!'
        __check_dices(result, result[0])

        if result[0][0] == result[0][1]:
            assert len(result) > 1, 'Fout: na de eerste keer dubbelgooien, moet nog een keer gegooid worden! {}'.format(result)
            __check_dices(result, result[1])

            if result[1][0] == result[1][1]:
                assert len(result) == 3, 'Fout: na de tweede keer dubbelgooien, mag niet nog een keer gegooid worden! Je functie geeft: {}'.format(result)
                __check_dices(result, result[2])


def __run_tests():
    """ Test alle functies. """
    test_functions = [ test_monopolyworp ]

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