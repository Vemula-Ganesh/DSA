class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        spc="!@#$%^&*()-+"
        if len(password)<8:
            return False
        lc=False
        uc=False
        d=False
        sc=False
        dc=False
        for i in range(len(password)-1):
            lc=lc or password[i].islower() or password[i+1].islower()
            uc=uc or password[i].isupper() or password[i+1].isupper()
            d=d or password[i].isnumeric() or password[i+1].isnumeric()
            sc=sc or password[i] in spc or password[i+1] in spc
            dc=dc or password[i]==password[i+1]
        print(lc,uc,d,sc,dc)
        return lc and uc and d and sc and not dc


        # =any(i.islower() for i in password)
        # =any(i.isupper() for i in password)
        # =any(i.isnumeric() for i in password)
        # return len(password)>=8 and  and any(i.islower() for i in password) and any