class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Approach ONE
        count_dict = {}
        for number in nums:
            result = count_dict.get(number,None)
            # If the value does not exist, create it, otherwise increment the counter
            if not result:
                count_dict[number] = 1
            else:
                count_dict[number] += 1
                
        result = False

        for entry,value in count_dict.items():
            if value > 1:
                result = True
        
        return result