## 学习笔记
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