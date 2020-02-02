#coding:utf-8

str = "a"

print str.isalpha()

def test(s):
    l = len(s)
    start = 0
    end = len(s)-1
    for i in range(len(s)):

        if s[start].islower()==s[end].islower():
            continue
        else:
            if s[start].isalpha():
                if s[end].isalpha():
                    return False
                else:
                    end-=1
            else:
                start+=1
        return True