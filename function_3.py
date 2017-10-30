""" Define a function that computes the length of a given list or string. (It is true that Python has the len()
function built in, but writing it yourself is nevertheless a good exercise.) """

def length_of_str(word):
    number_of_char = 0
    for char in word:
        number_of_char += 1
    return number_of_char


def test(word, expected_result):
    actual_result = length_of_str(word)
    if actual_result == expected_result:
        print("PASS")
    else:
        print("FAIL.Lenght {} is {} not {}".format(word, expected_result, actual_result))


def main():
    test("test", 4)
    test(" test ", 6)
    test(" test", 5)

main()
