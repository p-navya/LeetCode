class Solution:
  def lengthOfLongestSubstring(self, s): # map for index
    d = {} # value => its index
    i = 0
    ans = 0
    for j, c in enumerate(s):
      if c in d:
        # mast max check i, example "abba"
        i = max(i, d[c] + 1)
      d[c] = j
      ans = max(ans, j - i + 1)
    return ans


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        l = 0  # left
        r = 0  # right

        result = 0
        isFoundInWindow = [False] * 256

        while r < len(s):

            while isFoundInWindow[ord(s[r])]:
                isFoundInWindow[ord(s[l])] = False
                l += 1

            isFoundInWindow[ord(s[r])] = True

            # check before shrink
            result = max(result, r - l + 1)

            r += 1

        return result

class Solution: # extra space for set()
    def lengthOfLongestSubstring(self, s: str) -> int:

        d = collections.defaultdict(int)
        start = 0
        ans = 0
        for i,c in enumerate(s):
            # shrink
            while d[c] > 0:
                d[s[start]] -= 1 # not s[start], not start
                start += 1
            ans = max(ans, i - start + 1)
            d[c] = 1
        return ans

############

class Solution(object):
  def _lengthOfLongestSubstring(self, s): # no extra data structure
    """
    :type s: str
    :rtype: int
    """
    d = collections.defaultdict(int)
    l = ans = 0
    for i, c in enumerate(s):
      while l > 0 and d[c] > 0:
        d[s[i - l]] -= 1
        l -= 1
      d[c] += 1
      l += 1
      ans = max(ans, l)
    return ans

############

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = set()
        i = ans = 0
        for j, c in enumerate(s):
            while c in ss:
                ss.remove(s[i])
                i += 1
            ss.add(c)
            ans = max(ans, j - i + 1)
        return ans