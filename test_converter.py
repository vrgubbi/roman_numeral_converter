from roman_numeral_converter import get_roman_numerals

def test_converter1():
    assert get_roman_numerals(160) == 'CLX', "Should be CLX"

def test_converter2():
    assert get_roman_numerals(1776) == 'MDCCLXXVI', "Should be MDCCLXXVI"

# Should be Invalid Roman Number
def test_converter3():
    assert get_roman_numerals(4100) == 'Invalid Roman Number'

if __name__ == "__main__":
    test_converter1()
    test_converter2()
    test_converter3()
    print("Everything passed")