# coding:utf-8
'''
拿破仑席卷欧洲大陆之后，代表自由，平等，博爱的竖色三色旗也风靡一时。荷兰国旗就是一面三色旗（只不过是横向的），自上而下为红白蓝三色。

该问题本身是关于三色球排序和分类的，由荷兰科学家Dijkstra提出。由于问题中的三色小球有序排列后正好分为三类，Dijkstra就想象成他母国的国旗，于是问题也就被命名为荷兰旗问题（Dutch National Flag Problem）。
下面是问题的正规描述：
现有n个红白蓝三种不同颜色的小球，乱序排列在一起，请通过两两交换任意两个球，使得从左至右，依次是一些红球、一些白球、一些蓝球。
给定一个数组array=[0,2,1,2,1,0,0,0,1,2,1,0,2,1] # 0-red 1-white 2-blue

'''


def f(array):
    head = 0
    tail = len(array) - 1
    cur = 0
    while cur < tail:
        if array[cur] == 0:
            array[cur], array[head] = array[head], array[cur]
            cur += 1
            head += 1
        elif array[cur] == 1:
            cur += 1
        else:  # array[cur]==2
            array[cur], array[tail] = array[tail], array[cur]
            tail -= 1
    return array

a = [0,2,1,2,1,0,0,0,1,2,1,0,2,1]
print(f(a))
