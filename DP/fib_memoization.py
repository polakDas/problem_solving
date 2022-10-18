# It gives me factorial of 50 is almost instant!! How Rickdiculous is this!! It takes O(n) space complexity.
# This is called memoization technique. It's a top-down approch

def fib(n, lookup):
    if n <= 1:
        lookup[n] = n
    
    if lookup[n] is None:
        lookup[n] = fib(n-1, lookup) + fib(n-2, lookup)

    return lookup[n]

def main():
    n = int(input("Enter a number: "))
    lookup = [None] * (n + 1)
    print("Result is: " , fib(n, lookup))

if __name__ == '__main__':
    main()
