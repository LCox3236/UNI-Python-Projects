def readPrime():
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    while True:
        myPrime = int(input("Enter a prime number less      than 20: "))
        if myPrime in primes:
            break
        print("You entered", myPrime)
