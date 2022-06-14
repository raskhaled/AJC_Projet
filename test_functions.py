from unittest import result
from main import count_char, check_if_maj, check_if_special, check_if_valid_password

def test_count_char():
    input ="Bonjour"
    expected = 7
    result = count_char(input)
    assert expected == result

def test_check_if_maj():
    input1 = "Bonjour"
    input2 = "bonjour"
    input3 = "bonjOur"

    expected1 = True
    expected2 = False
    expected3 = True

    result1 = check_if_maj(input1)
    result2 = check_if_maj(input2)
    result3 = check_if_maj(input3)

    assert expected1 == result1
    assert expected2 == result2
    assert expected3 == result3


def test_check_if_special():
    input1 = "Bonjo!!!!"
    input2 = "salut"

    expected1 = True
    expected2 = False

    result1 = check_if_special(input1)
    result2 = check_if_special(input2)
    
    assert expected1 == result1
    assert expected2 == result2

def test_if_valid_password():
    input1 = "atestEer!!!!!"
    expected1 = True
    result1 = check_if_valid_password(input1)

    input2 = "ausssi"
    expected2 = False
    result2 = check_if_valid_password(input2)

    input3 = "woaw-"    
    expected3 = False
    result3 = check_if_valid_password(input3)

    assert expected1 == result1
    assert expected2 == result2
    assert expected3 == result3



