class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        result=0
        prefixs=[s[:i+1] for i in range(len(s))]
        for word in words:
            if word in prefixs:
                result+=1
        return result


        
        