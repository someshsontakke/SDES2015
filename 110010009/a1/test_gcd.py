#file to test module gcd.py
import gcd

testing = [1, 2, 3, 4, 5]
b1 = [15, 48, 15.5, 15, "s"]
c1 = [4, 42, 4, -4, 4]
a1 = [1, 6]
def check_gcd(i):
    """function to check if the gcd calculated is correct.
    This is done using comparison with a precomputed answer saved in a1.

    Arguments:
    i: index in array testing

    Returns:
    void: only prints the output of the test.
    """
    temp_gcd = gcd.gcd(b1[i-1],c1[i-1])
    if temp_gcd==a1[i-1]:
        print "All fine, GCD of ",b1[i-1]," and ",c1[i-1]," is ",temp_gcd,"."
    else:
        print "GCD calculation is incorrect, GCD of ",b1[i-1]," and ",c1[i-1]," is ",a1[i-1],"."
for i in testing:
    check_gcd(i)
check_gcd(4)
