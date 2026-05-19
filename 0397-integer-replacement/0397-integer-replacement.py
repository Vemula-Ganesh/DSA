class Solution:
    def integerReplacement(self, n: int) -> int:
        # if n==1:return 0
        # result=0
        # if n%2!=0:
        #     n+=1
        #     result=1
        # while n!=1:
        #     n//=2
        #     if n%2!=0 and n!=1:
        #         n+=1
        #         result+=1
        #     print(n)
        #     result+=1
        # return result
 #------------------Chatgpt---------------------------------------------

        # steps = 0
        # while n != 1:
        #     if n % 2 == 0:
        #         n //= 2
        #     else:
        #         if n == 3 or n % 4 == 1:
        #             n -= 1
        #         else:
        #             n += 1
        #     steps += 1
        # return steps

 #------------------SIR---------------------------------------------

        total = 0
        while n > 1:
            total+=1
            if n%2==0:
                n>>=1
                continue
            if n==3 or n & 0b10 == 0:
                n -= 1
            else:
                n += 1
        return total
        
        