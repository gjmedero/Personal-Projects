#Enter a number and have the program generate the Fibonacci sequence 
# to that number or to the Nth number.
def Fibonacci_Sequence(n: int):
    fib_list = [1, 0]
    current_f = 0
    
    if n == 0:
        print(n)
    
    if n <= 2:
        print(1)
    
    for i in range(1, n):
        f_result = fib_list[0] + fib_list[1]
        fib_list[1]  = fib_list[0]
        fib_list[0] = f_result
        print(f_result)

#Have the user enter a number and find all Prime Factors (if there are any) and display them.
def Prime_Factorization(n: int):
    prime_list = []
    a = 3
    flag = 0

    # Catch evens
    if n != 2 and n % 2 == 0:
        return "Not a prime number"
    
    prime_list.append(2)
    
    while a <= n:
        for i in range(2, a):
            if a % i == 0:
                flag = 1
        
        if flag == 0:
            prime_list.append(a)
        
        flag = 0
        a += 2
    
    return prime_list

try:
    number = int(input("Enter a number to get the fibonacci sequence up to that number: "))
    Fibonacci_Sequence(number)
except ValueError:
    print("That's not a valid number")

try:
    value = int(input("Enter a number to get the prime factors up to that number: "))
    print(Prime_Factorization(value))
except ValueError:
    print("Thats not a valid integer")