class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Approach TWO

        initial_length = len(nums)
        no_duplicate_length = len(set(nums))

        if initial_length != no_duplicate_length:
            return True
        else:
            return False