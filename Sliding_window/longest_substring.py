# Problem on longest substring without repeating characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        length = 0
        charSet = set()

        while r < len(s):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            length = max(length, r-l+1)
            r += 1

        return length
    
# Time complexity: O(n)
# Space complexity: O(n)
if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb")) # 3
    print(s.lengthOfLongestSubstring("bbbbb")) # 1
    print(s.lengthOfLongestSubstring("pwwwkew")) # 3
    print(s.lengthOfLongestSubstring(" ")) # 1
    print(s.lengthOfLongestSubstring("au")) # 2
    print(s.lengthOfLongestSubstring("dvdf")) # 3