#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback
import collections
import builtins
import sys

"""
Programming
Practice Exercise 8.4
(c) 2021 Hogeschool Utrecht,
Tijmen Muller en 
Bart van Eijkelenburg (bart.vaneijkelenburg@hu.nl)


Opdracht:
Werk onderstaande functie(s) uit.
Voeg commentaar toe om je code toe te lichten.
"""


def tickers_to_dict(filename):
    """
    De functie leest uit de file alle bedrijfsnamen met bijbehorende
    ticker-symbolen en slaat die op in een dictionary. Hierbij is de
    bedrijfsnaam steeds een sleutel (key) en het symbool de waarde
    (value). Return de nieuwe dictionary.

    Args:
        filename (str): Het bestand waarin de ticker-symbolen staan
    Returns:
        dict: dictionary ticker-symbolen
    """
    return


def name_to_symbol(name, ticker_dict):
    """
    De functie zoekt in de dictionary (parameter ticker_dict) het ticker-
    symbool op van een bedrijfsnaam (parameter name). De returnwaarde is
    het tickersymbool, of None als de naam niet gevonden werd.

    Args:
        name (str): De bedrijfsnaam waarvan het ticker-symbol gezocht wordt
        ticker_dict (dict): De dictionary met de ticker-symbolen
    Returns:
        str: ticker-symbol bij de bedrijfsnaam, of None
    """
    return



def symbol_to_name(symbol, ticker_dict):
    """
    De functie zoekt in de dictionary (parameter ticker_dict) de bedrijfs-
    naam op van een ticker-symbool (parameter symbol). De returnwaarde is het
    tickersymbool, of None als het ticker-symbol niet gevonden werd.

    Args:
        symbol (str): Het ticker-symbol waarvan de bedrijfsnaam gezocht wordt
        ticker_dict (dict): De dictionary met de ticker-symbolen
    Returns:
        str: bedrijfsnaam bij het ticker-symbol, of None
    """
    return


def development_code():
    # Plaats hieronder eventueel code om je functies tussentijds te testen. Bijv:
    tickers = tickers_to_dict('tickers.txt')

    name = input('Enter Company name: ')
    print(f"Ticker symbol: {name_to_symbol(name, tickers)}")

    symbol = input('Enter Ticker symbol: ')
    print(f"Company name: {symbol_to_name(symbol, tickers)}")


def module_runner():
    development_code()      # Comment deze regel om je 'development_code' uit te schakelen
    __run_tests()           # Comment deze regel om de HU-tests uit te schakelen


"""
==========================[ HU TESTRAAMWERK ]================================
Hieronder staan de tests voor je code -- daaraan mag je niets wijzigen!
"""


def __my_test_file():
    return "pe_8_4_testtickers.txt"


def __create_test_file(tickers, testfile=__my_test_file()):
    print(f"Voor testdoeleinden wordt bestand {testfile} aangemaakt met {len(tickers)} tickers... ", end="")

    try:
        with open(testfile, 'w') as dummy_file:
            for company, ticker in tickers.items():
                dummy_file.write(f"{company}:{ticker}\n")
    except:
        print(f"\nFout: bestand {testfile} kon niet worden aangemaakt. Python-error:")
        print(traceback.format_exc())
        sys.exit()

    print("Klaar.")


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


def test_tickers_to_dict():
    function = tickers_to_dict

    case = collections.namedtuple('case', 'tickers')
    testcases = [case({"YAHOO":"YHOO", "GOOGLE INC":"GOOG", "Harley-Davidson":"HOG",
                       "Yamana Gold":"AUY", "Sotheby's":"BID", "inBev":"BUD"}),
                 case({"Apple Inc.": "AAPL", "Ford Motor Company": "F"}),
                 case({})]

    for test in testcases:
        __create_test_file(test.tickers)

        original_open = builtins.open
        builtins.open = lambda file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None: \
            original_open(__my_test_file(), mode=mode, buffering=buffering, encoding=encoding, errors=errors, newline=newline, closefd=closefd, opener=opener)

        try:
            __my_assert_args(function, (__my_test_file(),), test.tickers, check_type=True)
        finally:
            builtins.open = original_open


def test_name_to_symbol():
    function = name_to_symbol

    case = collections.namedtuple('case', 'tickers company_name expected_symbol')
    testcases = [case({"YAHOO":"YHOO", "GOOGLE INC":"GOOG", "Harley-Davidson":"HOG",
                       "Yamana Gold":"AUY", "Sotheby's":"BID", "inBev":"BUD"}, "Harley-Davidson", "HOG"),
                 case({"Apple Inc.": "AAPL", "Ford Motor Company": "F"}, "Apple Inc.", "AAPL"),
                 case({}, 'Test', None)]

    for test in testcases:
        __create_test_file(test.tickers)

        original_open = builtins.open
        builtins.open = lambda file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None: \
            original_open(__my_test_file(), mode=mode, buffering=buffering, encoding=encoding, errors=errors, newline=newline, closefd=closefd, opener=opener)

        try:
            __my_assert_args(function, (test.company_name, tickers_to_dict(__my_test_file())), test.expected_symbol, check_type=True)
        finally:
            builtins.open = original_open


def test_symbol_to_name():
    function = symbol_to_name

    case = collections.namedtuple('case', 'tickers ticker_symbol expected_company')
    testcases = [case({"YAHOO":"YHOO", "GOOGLE INC":"GOOG", "Harley-Davidson":"HOG",
                       "Yamana Gold":"AUY", "Sotheby's":"BID", "inBev":"BUD"}, "AUY", "Yamana Gold"),
                 case({"Apple Inc.": "AAPL", "Ford Motor Company": "F"}, "F", "Ford Motor Company"),
                 case({}, 'TST', None)]

    for test in testcases:
        __create_test_file(test.tickers)

        original_open = builtins.open
        builtins.open = lambda file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None: \
            original_open(__my_test_file(), mode=mode, buffering=buffering, encoding=encoding, errors=errors, newline=newline, closefd=closefd, opener=opener)

        try:
            __my_assert_args(function, (test.ticker_symbol, tickers_to_dict(__my_test_file())), test.expected_company, check_type=True)
        finally:
            builtins.open = original_open


def __run_tests():
    """ Test alle functies. """
    test_functions = [test_tickers_to_dict, test_name_to_symbol, test_symbol_to_name]

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