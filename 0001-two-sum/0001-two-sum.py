class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
#         nums_map = {}
#         # 키와 값을 바꿔서 딕셔너리로 저장
#         for i, num in enumerate(nums):
#             nums_map[num] = i
        
#         print(nums_map)
#         # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
#         for i, num in enumerate(nums):
#             if target - num in nums_map and i != nums_map[target - num]:
#                 return nums.index(num), nums_map[target - num]

        