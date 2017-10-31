"""Define a function sum() and a function multiply() that sums and multiplies
(respectively) all the numbers in a list of numbers. For example,
sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return
24."""


def sum(list_of_numbers):
    number_sum = 0
    for number in list_of_numbers:
        number_sum += number
    return number_sum


def multiply(list_of_numbers):
    number_multi = 1
    for number in list_of_numbers:
        number_multi *= number
    return number_multi


def test_sum(list_of_numbers, expected_result):
    actual_result = sum(list_of_numbers)
    if actual_result == expected_result:
        print("PASS")
    else:
        print("Sum of {} is {} not {}".format(
                            list_of_numbers, expected_result, actual_result))


def test_multi(list_of_numbers, expected_result):
    actual_result = multiply(list_of_numbers)
    if actual_result == expected_result:
        print("PASS")
    else:
        print("Multiply of {} is {} not {}".format(
                            list_of_numbers, expected_result, actual_result))


def main():
    test_sum([1, 2], 3)
    test_sum([-1, 2], 1)
    test_sum([-1, -2], -3)
    test_sum([1], 1)
    print("------->")
    test_multi([1, 2], 2)
    test_multi([-1, 2], -2)
    test_multi([-1, -2], 2)
    test_multi([1, 2, 3, 4], 24)


main()
