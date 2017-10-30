"""Define a function max() that takes two numbers as arguments and returns the largest of them. Use the if-then-else
construct available in Python. (It is true that Python has the max() function built in, but writing it yourself is
nevertheless a good exercise.)"""

def _max(a,b):
    if a > b:
        return a
    else:
        return b


def test(a, b, expected_result):
    actual_result = _max(a,b)
    if actual_result == expected_result:
        print("PASS")
    else:
        print("FAIL. Max({},{}) = {} not {}".format(a,b,expected_result,actual_result))

def main():
    test(2,3,3)
    test(-1,0,0)
    test(-1000,-999,-999)
    test(150,1000,1000)
    test(2,8,8)

main()
