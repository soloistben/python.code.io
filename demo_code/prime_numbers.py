# -*- coding: utf-8 -*-
def main():
    i = 0
    for n in primes():
        if n < 1000:
            if i%20==0:
                print()
            print(n,end=" ")
            i+=1
        else:
            break

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)    #it.next()
        yield n
        it = filter(_not_divisible(n), it)

if __name__ == '__main__':
    main()