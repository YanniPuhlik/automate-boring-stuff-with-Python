# automate-boring-stuff-with-Python

def Collatz(number):
    if number%2==0:
        result=number//2
    elif number%2==1:
        result=number*3+1
    return result
while True:
    try:
        number = int(input("Enter the number: "))
        print(Collatz(number))
    except ValueError:
        print('This is not a number. Please enter the number')
