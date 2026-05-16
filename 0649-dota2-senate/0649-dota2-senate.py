from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = deque()
        d = deque()
        n = len(senate)

        for i in range(n):
            if senate[i] == 'R':
                r.append(i)
            else:
                d.append(i)

        while r and d:
            r_idx = r.popleft()
            d_idx = d.popleft()

            if r_idx < d_idx:
                r.append(r_idx + n)
            else:
                d.append(d_idx + n)

        return "Radiant" if r else "Dire"
#         # for i in range(0,len(senate)-1,2):
#         #     if senate[i]+senate[i+1]=="RR":
#         #         return "Radiant"
#         #     elif senate[i]+senate[i+1]=="DD":
#         #         return "Dire"
#         # if senate.count("R")==senate.count("D"):
#         #     if senate[0]=="R":
#         #         return "Radiant"
#         #     return "Dire"
#         # if senate.count("R")>senate.count("D"):
#         #     return "Radiant"
#         # if senate.count("R")<senate.count("D"):
#         #     return "Dire"
#         senat=senate
#         for i in senate:
#             # senate=senate.replace("R","D")
#             # print(senate)
#             if i=="R":
#                 senat=senate.replace("D","R")
#                 print(senate)
#             else:
#                 senat=senate.replace("R","D")
#         return "Radiant" if senat[0]=="R" else "Dire"    
            
