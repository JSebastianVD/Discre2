import math

def is_prime(n):
  for i in range(2,int(math.sqrt(n))+1):
    if (n%i) == 0:
      return False
  return True

if __name__ == '__main__':
    n = int(input("Numero hasta donde quiera ver los primos: "))
    print(2)
    for i in range(3,n,2):
        if is_prime(i):
            print(i)