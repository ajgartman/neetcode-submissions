class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output_vals = {}
        output_list = []

        for word in strs:
            name = []
            for letter in word:
                name.append(letter)

            sorted_set = sorted(name)
            value = output_vals.get(str(sorted_set),None)
            if not value:
                output_vals[str(sorted_set)] = [word]
            else:
                output_vals[str(sorted_set)].append(word)

        for values in output_vals.values():
            output_list.append(values)

        return output_list
        