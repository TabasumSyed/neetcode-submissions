class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[j - 1] > nums[j]:
                    temp = nums[j - 1]
                    nums[j - 1] = nums[j]
                    nums[j] = temp
        return nums
