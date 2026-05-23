class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # f=0
        # if dividend<0 and divisor>0:
        #     f=1
        #     dividend=-(dividend)
        # elif  dividend>0 and divisor<0:
        #     f=1
        #     divisor=-(divisor)
        # i=0
        # x=divisor
        # while dividend>=x:
        #     i+=1
        #     x+=divisor
        # if f:
        #     return -i
        # return i
        if (2**31 - 1)<int(dividend/divisor):
            return (2**31 - 1)
        elif -(2**31)>int(dividend/divisor):
            return -2**31
        return (int(dividend/divisor))
        