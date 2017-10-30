"""Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language").
That is, double every consonant and place an occurrence of "o" in between. For example, translate("this is fun")
should return the string "tothohisos isos fofunon"."""

def translate(sentence):
    vowel = ['a', 'o', 'i', 'e', 'u', 'y', ' ']
    translate_sentence = ""
    for char in sentence:
        if char not in vowel:
            translate_sentence += char + "o" + char
        else:
            translate_sentence += char
    return translate_sentence


def test(sentence, expected_result):
    actual_result = translate(sentence)
    if actual_result == expected_result:
        print("PASS")
    else:
        print("FAIL. {} not equal {}".format(actual_result, expected_result))


def main():
    test("dog", "dodogog")
    test("this is fun", "tothohisos isos fofunon")


main()
