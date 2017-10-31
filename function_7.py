""" Define a function reverse() that computes the reversal of a string. For
example, reverse("I am testing") should return the string "gnitset ma I"."""


def reverse_string(sentence):
    # wersja 1
    # reverse_sentence = []
    # for char in sentence:
    #     reverse_sentence.insert(0, char)
    # return "".join(reverse_sentence)

    # wersja 2
    return sentence[::-1]


def test(sentence, expected_result):
    actual_result = reverse_string(sentence)
    if actual_result == expected_result:
        print("PASS")
    else:
        print("FAIL. Revers of {} is {} not {}".format(
                                    sentence, expected_result, actual_result))


def main():
    test("I am testing", "gnitset ma I")


main()
