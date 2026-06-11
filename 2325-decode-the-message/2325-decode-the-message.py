class Solution(object):
    def decodeMessage(self, key, message):
        x=97
        d={}
        for i in key:
            if i not in d and i!=" ":
                d[i]=chr(x)
                # print(chr(x))
                x+=1
        d[" "]=" "
        # print(d.items())
        result=""
        for i in message:
            result+=(d[i])
            # print(result)
        return result

        # for i in key[:len(key):]:
        #     if i!=" ":
        #         # print(i)
        #         # print(x)
        #         d[i]=chr(x)
        #         # print(d[i])
        #         x+=1
        # print(d)
        # for i in range(len(message)):
        #     message[i]
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        