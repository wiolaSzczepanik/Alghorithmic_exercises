"""Define a function max_of_three() that takes three numbers as arguments and returns the largest of them."""

def _max(a,b,c):
    if a > b:
        if a > c:
            return a
    if b > a:
        if b > c:
            return b
    if c > a:
        if c > b:
            return c

def test(a,b,c, expected_result):
    actual_result = _max(a,b,c)
    if actual_result == expected_result:
        print("PASS")
    else:
        print("FAIL. Max({},{},{}) is {} not {}".format(a,b,c, expected_result, actual_result))

def main():
    test(1,2,3,3)
    test(-1,-2,-3,-1)
    test(5,3,2,5)
    test(0,1,2,2)
    test(15,0,2,15)
    test(15,30,2,30)



main()
