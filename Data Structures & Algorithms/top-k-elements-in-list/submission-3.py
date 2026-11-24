class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
    
        for number in nums:
            # Checking if number exists in the dictionary
            result = count_dict.get(number,None)
            if not result:
                count_dict[number] = 1
            else:
                count_dict[number] += 1
        # We need to return most frequent
        output_list = sorted(count_dict, key=count_dict.get, reverse=True)

        return output_list[:k]