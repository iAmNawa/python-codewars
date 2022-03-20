# Complete the function that takes a non-negative integer n as input, 
# and returns a list of all the powers of 2 with the exponent ranging 
# from 0 to n ( inclusive ).

def powers_of_two(n):
    list = [1]
    for i in range(1,n+2):
        if (i>1):
            list.append(list[i-2]*2)
    return list

powers_of_two(10)