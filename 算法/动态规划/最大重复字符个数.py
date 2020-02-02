#coding:utf-8
'''
abcddefadsfdfcgasd

'''

def test(array):
    a=[]
    count =0
    countNum=[]
    for i in array:
        if i not in a:
            a.append(i)
            count+=1
        else:
            a=[]
            countNum.append(count)
    return max(countNum)

if __name__ == '__main__':
    a="a0l245abcdefghacd"
    print(test(a))