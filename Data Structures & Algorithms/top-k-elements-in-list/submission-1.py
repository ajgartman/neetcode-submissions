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
        sorted_list = sorted(count_dict.items(), key = lambda x: x[1], reverse = True)
        output_list = [item[0] for item in sorted_list]

        return output_list[:k]