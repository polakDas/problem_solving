# Leetcode problem 198. House Robber

def rob(nums:list[int]) -> int:
    current, previous = 0, 0

    for num in nums:
        temp = max(num + previous, current)
        previous = current
        current = temp

    return current

def main():
    nums = [1, 5, 3, 6, 2, 7, 9, 3]
    print(rob(nums))

if __name__ == "__main__":
    main()
