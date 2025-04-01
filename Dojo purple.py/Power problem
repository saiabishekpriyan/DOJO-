# Taking input
x = float(input())  
n = int(input())  


result = 1


if n < 0:
    x = 1 / x  
    n = -n  


while n > 0:
    if n % 2 == 1:  
        result *= x
    x *= x  
    n //= 2  


print(f"{result:.2f}")
