# This is fucking insane. It takes only O(n) time complexity for that loop.
# It's a bottom up approach.

def fib(n):
    '''
    Counting fib number one by one and store it to a list.
    '''
    f = [0] * (n + 1)

    f[1] = 1

    for i in range(2, n+1):
        f[i] = f[i - 1] + f[i - 2]
    return f

def main():
    n = int(input("Enter a number: "))
    print("Result is ", fib(n))

if __name__ == "__main__":
    main()
