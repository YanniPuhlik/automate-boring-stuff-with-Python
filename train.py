#Practice Projects solution: collatz() function from the book https://automatetheboringstuff.com/chapter3/
#define function
def Collatz(number):
    #If number is even, then collatz() should print number // 2 and return this value.
    if number%2==0:
        result=number//2
     #If number is odd, then collatz() should print and return 3 * number + 1.
    elif number%2==1:
        result=number*3+1
    return result
# lop function
while True:
    try:
        number = int(input("Enter the number: "))
        print(Collatz(number))
 # if noninteger value entered print This is not a number. Please enter the number
    except ValueError:
        print('This is not a number. Please enter the number')
