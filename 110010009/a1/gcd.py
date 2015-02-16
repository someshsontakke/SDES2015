def gcd(int1, int2):
    """Returns the GCD of two integers, both need to be non negative

    Arguments:
    int1: an integer
    int2: an integer

    Returns: GCD of int1 and int2
    """
    if int1<=0 or int2<=0:
        raise ValueError("The numbers entered are not positive.")
    a = type(0)
    b = type(int1)
    c = type(int2)
    if a==b and a==c:
        while int2:
            int1, int2 = int2, int1%int2
        return int1
    else: 
        raise TypeError("The numbers must be integers.")
    
