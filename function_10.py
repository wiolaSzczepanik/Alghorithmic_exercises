"""Define a function overlapping() that takes two lists and returns True if
they have at least one member in common, False otherwise. You may use your
is_member() function, or the in operator, but for the sake of the exercise, you
should (also) write it using two nested for-loops."""

def overlapping(list_1, list_2):
    for item in list_1:
        for ele in list_2:
            if ele == item:
                return True
    return False


def test(list_1, list_2, expected_result):
    actual_result = overlapping(list_1, list_2)
    if actual_result == expected_result:
        print("PASS")
    else:
        print("FAIL. ")


def main():
    test(['a','b'],['b','c'], True)
    test([1,2,3,4,],[3,4,5,6], True)


main()
