def solution(nums):
    set_nums = set(nums)
    return len(set_nums) if len(nums)//2 > len(set_nums) else len(nums)//2