def solution(nums):
    set_nums = set(nums)
    if len(nums)//2 > len(set_nums):
        return len(set_nums)
    else:
        return len(nums)//2