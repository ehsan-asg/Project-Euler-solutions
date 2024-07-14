def fibo(n):
    if n == 0:
        return  0
    elif n == 1 or n == 2:
        return n
    else:
        return  fibo(n-1)+fibo(n-2)

def sum_even():
    total = 0
    n = 0
    while fibo(n)< 4000000:
          if fibo(n) % 2 == 0:
            total +=fibo(n)
          n +=1
    return total
print(sum_even())
