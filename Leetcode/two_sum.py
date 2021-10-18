class Solution:

    def two_sum(self, nums: list[int], target: int) -> list[int]:

        dic = dict()
        
        for i in range(len(nums)):

            if nums[i] not in dic:

                dic[target - nums[i]] = i

            else:

                return [dic[nums[i]], i]

        return None
