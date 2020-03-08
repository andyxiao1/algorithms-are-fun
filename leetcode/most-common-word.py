from collections import defaultdict

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        i, N = 0, len(paragraph)
        count = defaultdict(int)
        
        while i < N:
            start = i
            while i < N and paragraph[i].isalpha():
                i += 1
            word = paragraph[start:i]
            word = word.lower()
            
            if word not in banned:
                count[word] += 1
            
            while i < N and not paragraph[i].isalpha():
                i += 1
        
        return max(count.keys(), key=(lambda k : count[k]))