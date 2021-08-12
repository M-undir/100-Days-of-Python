# Prime number checker

def prime_checker(number):
    num = 0
    for i in range(2, number):
        if number % i == 0:
            num += 1
    if num > 0:
        print("Not a prime")
    else:
        print("Prime")


n = int(input("Check this number: "))
prime_checker(number=n)
