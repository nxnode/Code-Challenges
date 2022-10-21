# https://www.codewars.com/kata/520b9d2ad5c005041100000f

from code_challenges.code_wars.simple_pig_latin import pig_latinify


def test_pig_latinify():
    assert pig_latinify("Pig latin is cool") == "igPay atinlay siay oolcay"
    assert pig_latinify("This is my string") == "hisTay siay ymay tringsay"
    assert pig_latinify("O tempora o mores !") == "Oay emporatay oay oresmay !"
    assert (
        pig_latinify("Quis custodiet ipsos custodes ?")
        == "uisQay ustodietcay psosiay ustodescay ?"
    )
