#The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

#Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

#NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

def isPrime(n):
    result = True
    if n < 2:
        result = False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                result = False
                break
    return result

def Truncating(n):
    final_list = []
    temp = n
    temp2 = n
    d = len(str(n))
    while temp >9:
        temp //= 10
        final_list.append(temp) #doesn't include original number (no need to check twice)
    while d > 1:
        temp2 -= int(str(temp2)[0])*10**(d-1)
        d = len(str(temp2))
        final_list.append(temp2)
    return final_list

def TruncatablePrimes():
    count = 0
    starting_number = 11
    final_list = []
    while count < 11:
        if isPrime(starting_number):
            new_list = Truncating(starting_number)
            result = True
            for eachNumber in new_list:
                if not isPrime(eachNumber):
                    result = False
                    break
            if result:
                count += 1
                final_list.append(starting_number)
        starting_number += 2
    return sum(final_list)


#print(Truncating(1009))
print(TruncatablePrimes())
#print(isPrime(0))