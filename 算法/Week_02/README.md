学习笔记

#### 1、树的前序遍历
##### 1.1、递归比较简单，忽略
##### 1.2、迭代法
- 普遍都是利用栈的数据结构，然后遍历右子树，再遍历左子树，一次将节点push到stack中
- 二叉树，n叉树都是如此
```
1、定义一个栈结构(stack)，初始放入root节点
2、while stack: 将栈顶元素pop出来，取出节点值，再遍历子节点
3、遍历子节点是先右子树，再左子树，n叉树即为root.children[::-1]
4、直到stack为空
```

#### 2、树的后序遍历
##### 2.1、递归忽略
##### 2.2、迭代法
- 利用栈的数据结构，先遍历左子树，再遍历右子树，最后将结果保存在数组中，直接返回反转数组
- n叉树，二叉树一样的解法
```
1、定义一个栈结构，初始放入root节点
2、while stack；将栈顶pop出来，先遍历左子树，再遍历右子树，最后将节点值保存数组中，
3、待stack不满足循环条件之后，将结果反转返回即可，切记反转、反转、反转

```

#### 3、层次遍历bfs
##### 3.1、bfs模板
```
if not root: return []  # 判断条件
res = []
queue = [root]
while queue:   # 循环条件
    temp = [] # 存储每一层级的元素列表
    nodes = [] #存储下一层级的所有节点
    for i in queue:
        temp.append(i)
        for c in i.children:
            nodes.append(c)
    res.append(temp) # 依次将每一层级的节点加入结果集中
    queue = nodes # 替换循环条件
return res

```
##### 3.2、dfs模板
```
res = []
def dfs(root, depth):
    if not root: return []
    if len(res) <= depth: # 判断条件，当前结果集长度<=递归层级长度，结果集中添加一个空列表，相当于占位
        res.append([])
    res[depth].append(root.val) # 将节点值加入占位列表中
    for ch in root.children: # 再遍历子节点，递归执行
        dfs(ch, depth + 1)

dfs(root, 0)
return res

```

#### 4、二叉树的中序遍历
##### 4.1、递归忽略
##### 4.2、迭代法
- n叉树没有中序遍历，因为子节点无法确定先后顺序
- 利用栈数据结构，用来保存已经遍历过，但还没处理的节点
- 遍历从根节点开始，从左子树遍历，只要有左子树，就继续遍历，在遍历的同时，将节点保存到stack结构中，即保存遍历过的节点
- 当遍历左子树没有节点的时候，从stack中弹出节点，弹出的节点就可以处理或保存值
- 遍历有右子树
```
模板稍微复杂一点点

stack = []
res = []
p = root
while p or stack:
    while p: # 一直找左子树，直到没有左子树节点位置
        stack.append(p) # 左子树节点存下来
        p = p.left
    p = stack.pop() # 将最深层的节点从stack弹出
    res.append(p.val) #
    p = p.right
return res

```
#### 5、topk问题
##### 5.1、通用方法：先统计，再遍历，或 先排序，再遍历。如果长度比较短的数组，此方法可通
##### 5.2、如果数组是海量的，内存根本不够用，可以试试大顶堆、小顶堆的方法，即优先队列 时间复杂度O(nlogk)
```
python:  自带模块heapq 内部采用堆排序
1、heapq.heapify(list) 即堆化，不是严格递增，但第一个元素(即堆顶元素)永远是最小的。这个特性很重要！！！
默认实现的是小顶堆，如果需要大顶堆的话，其实放入堆内的元素取反即可
2、heapq.heappop(hp) 删除堆顶元素
3、heapq.heappush(hp,arr[i]) 替换堆顶元素，并重新排序,而且永远保持第一个(堆顶)元素是最小的。

```