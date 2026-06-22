class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
            if text.count("b")==text.count("a")==text.count("n")==text.count("l")/2==text.count("o")/2:
                return text.count('b')
            return min(text.count("b"),text.count("a"),text.count("n"),text.count("l")//2,text.count("o")//2)
