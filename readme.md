
```
本专栏定位为架构师必学技能,不再局限于算法方向的学习.
持续更新中
```

## 算法总结笔记

## 链表\数组\栈\队列总结

`主要练习链表、数组、栈队列、队列的算法题`

#### 链表类型 比较常见的解题方法使用双指针，快慢指针，比如验证是否有环，查找第k的元素，或中位数等等，这类题目没什么黑科技，还是多练习为主，通常能想到使用双指针就能解决。
#### 数组类的问题:一般对于数组的遍历的问题，尤其是对时间复杂度或者空间复杂度有要求的题目，首先想想是否能通过指针法能够解决，很多情况下，是能通过指针来解决，并且能解决时间复杂度最小的方式。
#### 关于栈和队列的问题：首先要了解他们的特性，这种数据结构通常适用于特殊的场景，效果会更好。


## 树总结

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

## 递归总结
#### 递归一直是我的薄弱项，有太多的为什么想要问，却不知道从哪问起，索性用做题来积累吧，刚开始递归确实也会陷进去，人肉递归，然后就晕菜了
#### 终于总结出递归的一些共同点：原来递归也是有套路的，切记下面的模板，很多递归的问题基本都是从模板演进过来的
#### 核心思想：1、避免人肉递归，2、找最近重复子问题 3、数学归纳法
### 递归模板
```
# Python
def recursion(level, param1, param2, ...): 
    # recursion terminator 
    if level > MAX_LEVEL: 
	   process_result 
	   return 
    # process logic in current level 
    process(level, data...) 
    # drill down 
    self.recursion(level + 1, p1, ...) 
    # reverse the current level status if needed
```


### 回溯模板
```
回溯的本质也是递归，只不过试探不同的路径，直到找到符合要求的路径
def backtrack(nums(选择列表),track(路径)):
    # 终止掉价
    if len(nums)==len(track):
        res.append(track[:]) # 因为track是引用，所有将副本结果保存
    # 去掉不合法的结果，也就是提前剪枝
    if level xxx
        continue
    for i in range(len(nums)):
        track.append()
        backtrack(nums,track)
        res.pop() 
    
```
### 分治模板
```
# Python
def divide_conquer(problem, param1, param2, ...): 
  # recursion terminator 
  if problem is None: 
	print_result 
	return 
  # prepare data 
  data = prepare_data(problem) 
  subproblems = split_problem(problem, data) 
  # conquer subproblems 
  subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
  subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
  subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
  …
  # process and generate the final result 
  result = process_result(subresult1, subresult2, subresult3, …)
	
  # revert the current level states

```

### dfs模板
#### 递归
```
visited = set() 
def dfs(node, visited):
    if node in visited: # terminator
    	# already visited 
    	return 
	visited.add(node) 
	# process current node here. 
	...
	for next_node in node.children(): 
		if next_node not in visited: 
			dfs(next_node, visited)

```
#### 非递归
```
def DFS(self, tree): 
	if tree.root is None: 
		return [] 
	visited, stack = [], [tree.root]
	while stack: 
		node = stack.pop() 
		visited.add(node)
		process (node) 
		nodes = generate_related_nodes(node) 
		stack.push(nodes) 
	# other processing work 
	...
```

### bfs模板
#### 非递归
```

# Python
def BFS(graph, start, end):
    visited = set()
	queue = [] 
	queue.append([start]) 
	while queue: 
		node = queue.pop() 
		visited.add(node)
		process(node) 
		nodes = generate_related_nodes(node) 
		queue.push(nodes)
	# other processing work 
	...

```

### 贪心算法
#### 贪心算法，如果有回退，那就是回溯，如果保存中间结果，并且可以回退，能得到全局最优解，就是动态规划
#### 贪心算法：只顾眼前的利益，只能当下最优解，而非全局最优解
#### 什么情况下能用贪心算法？
```
解决一些最优化的问题

一旦一个问题可以通过贪心法来解决，通常能得到最优解，能不用用贪心法，看数据结构

简单来讲：问题能够分解成子问题的来解决，子问题的最优解可以推导出最终问题的最优解，
这种子问题的最优解称最优子结构。


```

### 二分查找模板
```

# Python
left, right = 0, len(array) - 1 
while left <= right: 
	  mid = (left + right) / 2 
	  if array[mid] == target: 
		    # find the target!! 
		    break or return result 
	  elif array[mid] < target: 
		    left = mid + 1 
	  else: 
		    right = mid - 1

使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方
说明：同学们可以将自己的思路、代码写在学习总结中
```