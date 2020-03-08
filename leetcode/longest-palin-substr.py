class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if not s:
            return ''
        
        start = .5
        longest = 1
        longest_str = s[0]
        N = len(s)
        
        while start < N - 1:
            
            if start % 1 == 0:
                lo, hi = int(start - 1), int(start + 1)
            else:
                lo, hi = int(start - .5), int(start + .5)
            
            changed = False
            while lo >= 0 and hi < N and s[lo] == s[hi]:
                lo -= 1
                hi += 1
                changed = True
            
            if changed:
                lo += 1
                hi -= 1
                size = hi - lo + 1
                if size > longest:
                    longest, longest_str = size, s[lo : hi + 1]
            
            start += .5
        
        return longest_str