# Limitation of the code is that if the input is less than 2 then this program will not work properly.

def prime_checker(n1, n2):
    if n1 > 1:
        for numbers in range(n1, n2):

            for digit in range(2, numbers):
                if numbers % digit == 0:
                    print("It's not a prime number", numbers)
                    break
            else:
                print("It's a prime number", numbers)
    else:
        print("It's not a prime number")



first_number = int(input("Beginning number: "))
second_number = int(input("Ending number: "))
prime_checker(first_number, second_number)
