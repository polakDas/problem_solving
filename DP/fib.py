# It gives me the factorial of 40 in almost 10+ second!!! Can you imagine how much it takes if I enter 45?

def fib(n):
    if n <= 1:
        return n
    
    return fib(n-1) + fib(n-2)

def main():
    n = int(input("Enter a number: "))
    print("Result is " , fib(n))

if __name__ == '__main__':
    main()
