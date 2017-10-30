"""Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel,
    False otherwise. """

def is_vowel(char):
    vowel = ["a", "o", "i", "u", "e", "y"]
    if char in vowel:
        return True
    else:
        return False


def test(char, expected_result):
    actual_result = is_vowel(char)
    if actual_result == expected_result:
        print("PASS")
    else:
        print("FAIL. {} is not vowel".format(char))

def main():
    test("a", True)
    test("b", False)
