class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # sentence=list(map(str,sentence.split(" ")))
        # print(sentence)
        sentence=sentence.split()
        for i in range(len(sentence)):
            if sentence[i].startswith(searchWord):
                return i+1
        return -1