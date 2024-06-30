'''
Recursive Printing 
Design a recursive function that accepts an integer argument, n, and prints 
the numbers 1 up through n. Test the function.

Recursive Multiplication
Design a recursive function that accepts two arguments into the parameters x and y. 
The function should return the value of x times y. Remember, multiplication can be performed as repeated 
addition as follows: 7 × 4 = 4 + 4 + 4 + 4 + 4 + 4 + 4 (To keep the function simple, assume x and y will 
always hold positive nonzero integers). Test the function.
'''

def recursive_print(n: int):
    if n == 0:
        return 
    recursive_print(n - 1)
    print(n, ' ')

def recursive_multiplication(x: int, y: int):
    if x == 1:
        return y
    return y + recursive_multiplication(x - 1, y)



