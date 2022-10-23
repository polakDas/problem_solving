# Leetcode problem 213. House Robber 2

def rob(nums:list[int]) -> int:
    current, previous = 0, 0

    for num in nums:
        temp = max(num + previous, current)
        previous = current
        current = temp
    
    return current

def main():
    nums = [1,3,1,3,100]
    print(max(rob(nums[:-1]), rob(nums[1:])))

if __name__ == "__main__":
    main()