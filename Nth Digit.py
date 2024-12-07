import math as m

def calculator(n: int, m_func: float):
    for i in range(1, n+1):
        print(round(m_func, i))

def nth_digit(n: int, s: str):
    if s == "pi":
        calculator(n, m.pi)
    elif s == "e":
        calculator(n, m.e)
    else:
        print("invalid input")
        
print("This program outputs π and e up to nth decimal places.")
num, sym = input("Input the digit followed by your choice of \"pi\" or \"e\" seperated by space. ").split()

num = int(num)
sym = str(sym)


nth_digit(num, sym)
