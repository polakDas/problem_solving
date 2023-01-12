def search_insert(nums, target):
    for num in nums:
        if num >= target:
            return nums.index(num)
    return len(nums)

if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 5
    nums = [1,3,5,6]
    target = 2
    nums = [1,3,5,6]
    target = 7
    print(search_insert(nums, target))