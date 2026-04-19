class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        result=[sum(i) for i in matrix]
        return result