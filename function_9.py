"""Write a function is_member() that takes a value (i.e. a number, string, etc)
x and a list of values a, and returns True if x is a member of a, False
otherwise. (Note that this is exactly what the in operator does, but for the
sake of the exercise you should pretend Python did not have this operator.)"""
def is_member(list_value, value):
    for ele in list_value:
        if value == ele:
            return True
    return False

def test(list_value, value, expected_result):
    actual_result = is_member(list_value, value)
    if actual_result == expected_result:
        print("PASS")
    else:
        print("FAIL. {} is in {}, result is {}".format(value, list_value, expected_result))

def main():
    test(["a", "b"], "b", True)
    test([1, 2, 3, 4], 3, True)


main()
