import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Use defaultdict to group anagrams
        dict = collections.defaultdict(list)

        for str in strs:
            # Sort the string and use it as the key
            key = ''.join(sorted(str))
            dict[key].append(str)

        # Return the groups of anagrams as a list
        return list(dict.values())
