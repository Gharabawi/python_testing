from re import A


def sum_eo (n, t):
    result =0
    if t == 'e':
        for i in range (1, n):
            if i%2 == 0:
                result +=i
        return(result)
    elif t =='o':
        for i in range (1, n):
            if i%2 !=0:
                result +=i
        return(result)
    else :
        return (-1)
temp = int(input())
stringTemp = str(input())
value = sum_eo(temp, stringTemp)
print (value)
        
# def sum_eo(n, t):
#     """Sum even or odd numbers in range.

#     Return the sum of even or odd natural numbers, in the range 1..n-1.

#     :param n: The endpoint of the range. The numbers from 1 to n-1 will be summed.
#     :param t: 'e' to sum even numbers, 'o' to sum odd numbers.
#     :return: The sum of the even or odd numbers in the range.
#             Returns -1 if `t` is not 'e' or 'o'.
#     """
#     if t == "e":
#         start = 2
#     elif t == 'o':
#         start = 1
#     else:
#         return -1

#     return sum(range(start, n, 2))


# x = sum_eo(11, 'spam')
# print(x)
