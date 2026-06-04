class Solution(object):
    def simplifyPath(self, path):
        path=list(map(str,path.split("/")))
        result=[]
        for i in path:
            if i==".." and len(result)>0:
                result.pop()
            elif i!="" and i!="."and i!="..":
                result.append("/"+i)
        print(path)
        if len(result)==0:
            return "/"
        return "".join(result)
        # for i 
        """
        :type path: str
        :rtype: str
        """
        