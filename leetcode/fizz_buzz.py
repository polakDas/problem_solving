def fizzBuzz(n):
    result = []
    for i in range(1, n+1):
        if i%15==0:
            result.append("FizzBuzz")
        elif i%3==0:
            result.append("Fizz")
        elif i%5==0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

if __name__=='__main__':
    print(fizzBuzz(15))