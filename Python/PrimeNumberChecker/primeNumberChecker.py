def prime_checker(n):
    if n > 1:
        for digit in range(2, n):
            if n % digit == 0:
                print("It's not a prime number")
                break
        else:
            print("It's a pirme number")
    else:
        print("It's not a prime number")



number = int(input("Check this number: "))
prime_checker(number)
