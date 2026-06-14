class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes=[0]
        max=altitudes[0]
        # max=float(-inf)

        # for i in range(len(gain)-1):
        #     if i==O:
        #         altitudes.append(0)
        #     elif i==1:
        #         altitudes.append(gain[0])
        #     else:
        #         altitudes.append(gain[i-1]+gain[i])
        # sum=0
        # for i in gain[:]:
        #     altitudes.append(sum)
        #     sum+=i
        # return max(altitudes[:])
        for i in range(1,len(gain)+1):
            alt_i=altitudes[i-1]+gain[i-1]
            print(alt_i)
            altitudes.append(alt_i)
            if alt_i>max:
                max=alt_i
        return max





            