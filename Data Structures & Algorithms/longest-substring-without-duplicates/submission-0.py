class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      
        uniqueChars = set()
        start = 0
        maxLen = 0

        for end in range(len(s)):
            while s[end] in uniqueChars:
                uniqueChars.remove(s[start])
                start += 1

            uniqueChars.add(s[end])
            length = end - start + 1
            maxLen = max(maxLen,length)

        return maxLen

                





        
        