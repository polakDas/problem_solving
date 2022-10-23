def bigMod(base, power, mod):
    if power == 0:
        return 1 % mod
    x = bigMod(base, power // 2, mod)
    x = (x * x) % mod
    if power % 2 == 1:
        x = (x * base) % mod

    return x

def main():
    # 2^5 % 6
    print(bigMod(2, 100, 6))

if __name__ == "__main__":
    main()
