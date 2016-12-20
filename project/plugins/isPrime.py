

def import_to(env):
    env.add_command(IsPrimeCommand(), 'isPrime')

def remove_from(env):
    env.remove_command('isPrime')


class IsPrimeCommand():

    def execute(self, args, fields):
        if len(args) != 1:
            print("expects exactly 1 integer argument")
        else:
            try:
                num = int(args[0])
                if isPrime(num):
                    print("prime!")
                else:
                    print("not prime.")
            except ValueError as e:
                print("not a number!")


def isPrime(num):
    if num < 1:
        return False
    if num == 1 or num == 2:
        return True
    n = int(num / 2)
    while n >= 2:
        # print(num, '%', n, '=', num % n)
        if (num % n == 0):
            return False
        n -= 1
    return True
    
def explore():
    while True:
        userin = input()
        if (userin.startswith('q')):
            break
        else:
            print(isPrime(int(userin)))
            
def test():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    notPrimes = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40]
    failed = False
    for k in primes:
        if not isPrime(k):
            print('failed on', k)
    
    for k in notPrimes:
        if isPrime(k):
            print('failed on', k)
            
    if not failed:
        print('all tests passed')
            
if __name__ == "__main__":
    explore()