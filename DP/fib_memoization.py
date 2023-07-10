# It gives me factorial of 50 almost instantly!! How Rickdiculous is this!!
# It takes O(n) space complexity.
# This is called memoization technique. It's a top-down approch

def fib(n, lookup):
    '''
    It takes a list to store the values of different factorials.
    When a numbers factorial is stored in the lookup list, it'll return the value.
    If we don't use this extra list, we have to calculate these values again and again
    '''
    if lookup[n] != None:
        return lookup[n]
    
    if n <= 2:
        result = 1
    else:
        result = fib(n - 1, lookup) + fib(n - 2, lookup)
    lookup[n] = result
    
    return result

def main():
    n = int(input("Enter a number: "))
    lookup = [None] * (n + 1)
    print("Result is: " , fib(n, lookup))

if __name__ == '__main__':
    main()
