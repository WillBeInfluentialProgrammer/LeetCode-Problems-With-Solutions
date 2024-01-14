class Solution:
    def LongestSubstringPalindrome(self, s: str) -> str:
        result = ""
        result_length = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > result_length:
                    result = s[l:r + 1]
                    result_length = r - l + 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > result_length:
                    result = s[l:r + 1]
                    result_length = r - l + 1
                l -= 1
                r += 1

        return result

sol = Solution()
string = "bdbdcde"
result = sol.LongestSubstringPalindrome(string)
print(result)



                     
        

        
