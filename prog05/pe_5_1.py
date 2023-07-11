#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback, builtins, collections

"""
Programming
Oefening PROG5.1
(c) 2021 Hogeschool Utrecht,
Tijmen Muller en 
Bart van Eijkelenburg (bart.vaneijkelenburg@hu.nl)


Opdracht:
Werk onderstaande functie(s) uit.
Voeg commentaar toe om je code toe te lichten.
"""


def gemiddelde():
    """
    Vraag de gebruiker om een willekeurige zin in te voeren. De functie
    geeft vervolgens de gemiddelde lengte van de woorden in de zin als
    returnwaarde terug, of 0 als de string leeg ('') is.

    Let op: de test gaat ervan uit dat de gebruiker de zin in één keer kan
    invoeren, en dat je in je functie dus slechts één keer de functie
    'input' gebruikt!

    Returns:
        float: De gemiddelde lengte van de woorden in de ingevoerde zin
    """
    return


def development_code():
    # Plaats hieronder eventueel code om je functies tussentijds te testen. Bijv:
    print("Gemiddelde lengte:", gemiddelde())


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


def test_gemiddelde():
    case = collections.namedtuple('case', 'simulated_input expected_average_length')
    testcases = [ case("klaveraas cacaodrank", 9.5),
                  case("vletschuit forumtopic Einaarstraat guerrilla-eenheden eenheidsinterval hulpbetoon gezoneerd temponorm Moermans redenering", 11.2),
                  case("cannabisproducten muskusos rammeide Linnaeusweg fulltimer Valeer columnpje rallycross", 9.75),
                  case("zabber verschraald langhariger sportkousen kerkvisitatie mobielst leenhulde regeringspartij", 10.5),
                  case("geheugenloos Pyrenese basketbalcoach rekwestrant luchttijd Rembrandtkade controlespoor buiiger", 10.875),
                  case("ondernemend Basilicum Sjirks paskaart talentelling", 9.2),
                  case("bijeenvegen honingzalfjes inriep theepotje spookfirma", 9.8),
                  case("overslagstation settopboxjes begripsmatig gewinnen", 11.75),
                  case("kapotgegaan Aijen opleidingstijd", 10.0),
                  case("huurquotes klauteren", 9.5),
                  case("bijvoedingen stijloefeningen", 13.5),
                  case ("afgeblazen cursusdoelen lenteachtig radiologische meetplek", 10.8),
                  case ("Mijnheer Haaksbergen Floortjes haatgevoelen schorsmolen antwoordkaarten schrijfwijs", 11.0),
                  case ("clusteroverleg laserstralen belasterend Otjes onweren toneelgroepjes bruikbaarste MMMDCLVIII uitvochten linkerschoen", 10.7),
                  case("prijskaartje bosvlam handelskredieten bevuil onbehouwenste publiciteitsservice eigendomsrecht themazitting autostuur tekstkaders", 11.9),
                  case("socialemediabedrijf ERP-technologie bloedpaspoort afgezwakt moerige echels bataljonscommandant Lovendaal verkneukel Pernilla", 11.5),
                  case ("dokterde Tasman", 7.0),
                  case("opbond", 6.0),
                  case("Andra Batavier vetbuik dichtst dekzand Kral bewandel opzuip meereed Katoele", 6.6),
                  case("lepelrek isotopen ingegaan Guinees Dijken Nooten Schimmer opgraaft Reppelse abacus", 7.3),
                  case ("otters kalkmelk feestje slipt Wu", 5.6),
                  case ("", 0),
                  case("afraas kennen Deil getorste berries", 6.2),
                  case ("lezing Noya creatuur tentjes cottage", 6.4),
                  case("fietslus trimpomp kruimels vuurzwam", 8.0),
                  case("lubberde", 8.0),
                  case("liggend klauw Tonnies kermes Zaza's", 6.2),
                  case("bereid salaris opera's uitspoot", 7.0) ]

    for test in testcases:
        original_input = builtins.input
        builtins.input = lambda prompt="": test.simulated_input

        try:
            __my_assert_args(gemiddelde, () ,test.expected_average_length)
        except AssertionError as ae:
            raise AssertionError(f"{ae.args[0]} (gesimuleerde invoer: '{test.simulated_input}')") from ae
        finally:
            builtins.input = original_input


def __run_tests():
    """ Test alle functies. """
    test_functions = [ test_gemiddelde ]

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