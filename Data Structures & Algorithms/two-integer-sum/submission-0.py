class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array_len = len(nums)
        for i in range(0,array_len):
            for j in range(i,array_len):
                if nums[i] + nums[j] == target and i != j:
                    print("TARGET FOUND!")
                    print("Indexes: ",i,j)
                    return [i,j]
            