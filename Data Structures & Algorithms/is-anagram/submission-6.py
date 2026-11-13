class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        concat_string = s + t
        output = True
        set1 = set(s)
        set2 = set(t)

        if set1 != set2:
            return False

        if len(concat_string) != len(s)*2:
            return False

        count_dict = {}
        for letter in concat_string:
            result = count_dict.get(letter,None)
            if not result:
                count_dict[letter] = 1
            else:
                count_dict[letter] += 1
        
        for key, value in count_dict.items():
            print(key,value)
            if value % 2 != 0:
                output = False

        return output