def count_dict(text):
    counter = {}
    for value in text:
        counter[value] = counter.get(value, 0) + 1
    return counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter_list = []
        for text in strs:
            counter_list.append(count_dict(text))

        current_dict = None
        i = 0
        group = []
        sub_group = []
        while(len(strs) != 0):
            print("counter_list", counter_list)
            if current_dict is None:
                current_dict = counter_list[0]
                sub_group = [strs[0]]
                counter_list.pop(0)
                strs.pop(0)
                i = 0
            while (i < len(strs)):
                if current_dict == counter_list[i]:
                    sub_group.append(strs[i])
                    counter_list.pop(i)
                    strs.pop(i)
                else: 
                    print("ELSE", current_dict, counter_list[i])
                    i = i + 1
            group.append(sub_group)
            print("sub_group", sub_group)
            current_dict = None
        return group
    