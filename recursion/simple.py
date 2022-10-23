def rec(n):
    if n < 0:
        return 0
    print(n)
    rec(n-2)

def main():
    rec(5)

if __name__ == "__main__":
    main()
