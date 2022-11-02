def binarySearch(nums: list[int], target: int, left: int, right: int) -> int:
    if(left > right):
        return -1

    mid = (right + left) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
    return binarySearch(nums, target, left, right)

if __name__ == '__main__':
    nums = [1, 3, 5, 7]
    target = 7
    result = binarySearch(nums=nums, target=target, left=0, right=len(nums)-1)
    print(result)