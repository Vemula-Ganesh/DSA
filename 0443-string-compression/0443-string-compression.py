class Solution:
    def compress(self, chars: List[str]) -> int:
        al=len(chars)
        prev=chars[0]
        c=1
        r=""
        for i in chars[1:]:
            if i!=prev:
                r+=prev+(str(c) if c>1 else "")
                prev=i
                c=1
            else:
                c+=1
        r+=prev+(str(c) if c>1 else "")
        chars.clear()
        chars.extend(list(r))
        return len(chars)
