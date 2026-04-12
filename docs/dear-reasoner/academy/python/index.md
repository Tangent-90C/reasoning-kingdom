# 兔狲学院：Python编程语法与数据结构

> 兔狲教授的亲切提示：编程不是关于记忆语法规则，而是关于表达思想和解决问题的艺术。Python以其简洁优雅的语法，成为学习计算思维的理想语言。本章不仅教你Python基础语法，更重要的是教你四种基础数据结构：哈希表、链表、树和图。让我们跟随小小猪的动手精神和小海豹的系统思维，一起探索这个强大的工具。

**学习目标**：
1. 掌握Python基础语法和编程思维
2. 理解四种基础数据结构的原理和实现
3. 学会用Python实现常见算法
4. 通过小例题培养解决问题的能力

**章节结构**：
1. **第一部分：Python基础语法**——编程的积木
2. **第二部分：基础数据结构**——组织数据的方式
3. **第三部分：算法与例题**——解决问题的艺术
4. **第四部分：Python进阶**——面向对象与函数式编程

---

# 第一部分：Python基础语法——编程的积木

## 词条1：变量、数据类型与运算符

### 官方解释
**变量**是存储数据的容器，通过标识符（变量名）引用。**数据类型**定义了数据的种类和可执行的操作。**运算符**用于对数据进行操作。

Python基本数据类型：
- 整数（int）：如 42, -3, 0
- 浮点数（float）：如 3.14, 2.0, -0.5
- 字符串（str）：如 "hello", 'Python', """多行"""
- 布尔值（bool）：True 或 False
- 列表（list）：有序可变序列，如 [1, 2, 3]
- 元组（tuple）：有序不可变序列，如 (1, 2, 3)
- 字典（dict）：键值对集合，如 {"name": "Alice", "age": 20}

### 兔狲老师解释
变量就像"贴标签的盒子"。

小小猪的比喻：
- 变量名：盒子上的标签
- 值：盒子里的东西
- 数据类型：东西的种类（书、水果、玩具...）
- 运算符：对东西进行操作的工具（加、减、比较等）

Python是动态类型语言：不用声明类型，解释器自动推断。

### 思考题1：动手题
问题：在Python交互环境中执行以下代码，观察结果：

```python
# 定义变量
x = 10
y = 3.14
name = "兔狲教授"
is_student = True

# 打印类型
print(type(x))
print(type(y)) 
print(type(name))
print(type(is_student))

# 类型转换
print(float(x))  # 整数转浮点数
print(int(y))    # 浮点数转整数（注意！）
print(str(x) + name)  # 连接字符串

# 运算符
a = 10
b = 3
print(f"加法: {a} + {b} = {a + b}")
print(f"除法: {a} / {b} = {a / b}")
print(f"整除: {a} // {b} = {a // b}")
print(f"取余: {a} % {b} = {a % b}")
print(f"幂运算: {a} ** {b} = {a ** b}")

# 比较运算符
print(f"{a} > {b}: {a > b}")
print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")

# 逻辑运算符
print(f"True and False: {True and False}")
print(f"True or False: {True or False}")
print(f"not True: {not True}")
```

记录每个print语句的输出，并解释发生了什么。

### 思考题2：动脑题
问题：为什么编程语言需要不同的数据类型和运算符？

思考方向：
- 整数和浮点数在内存中如何存储？为什么需要区分？
- 字符串为什么需要引号？单引号和双引号有什么区别？
- 列表和元组有什么区别？什么时候用哪个？
- 运算符的优先级是什么？为什么需要括号？
- 在现实世界中，数据类型和运算符对应什么概念？

---

## 词条2：控制结构与函数——程序的逻辑

### 官方解释
**控制结构**决定程序的执行流程：
1. 顺序结构：语句按顺序执行
2. 选择结构：根据条件选择执行路径（if-elif-else）
3. 循环结构：重复执行代码块（for, while）

**函数**是一段可重复使用的代码块，接受输入（参数），执行操作，返回输出（返回值）。

### 兔狲老师解释
控制结构让程序"有脑子"，函数让程序"模块化"。

小小猪的流程图：
```
开始 → 条件判断 → 是 → 执行A → 结束
              ↓
              否 → 执行B → 结束
```

循环就像"重复劳动"：
- for循环：知道要重复多少次（遍历列表）
- while循环：重复直到条件不满足

函数就像"预制菜"或"工具箱"：
- 避免重复：写一次，用多次
- 模块化：复杂问题分解为小函数
- 抽象：隐藏实现细节，暴露清晰接口

### 思考题3：动手题
问题：编写一个综合程序，包含控制结构和函数：

```python
# 1. 控制结构示例：成绩评级
def grade_evaluator(score):
    """根据成绩返回等级"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# 2. 循环示例：打印乘法表
def print_multiplication_table(n):
    """打印n×n的乘法表"""
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i}×{j}={i*j}", end="\t")
        print()  # 换行

# 3. 函数示例：计算阶乘和判断素数
def factorial(n):
    """计算n的阶乘"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def is_prime(num):
    """判断一个数是否为素数"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# 4. 主程序
def main():
    # 测试成绩评级
    scores = [85, 92, 78, 45, 100]
    for score in scores:
        grade = grade_evaluator(score)
        print(f"成绩{score}的等级是：{grade}")
    
    print("\n" + "="*50 + "\n")
    
    # 打印乘法表
    print("5×5乘法表：")
    print_multiplication_table(5)
    
    print("\n" + "="*50 + "\n")
    
    # 测试阶乘和素数
    print("阶乘计算：")
    for i in range(1, 6):
        print(f"{i}! = {factorial(i)}")
    
    print("\n素数判断：")
    numbers = [2, 3, 4, 5, 17, 21, 29]
    for n in numbers:
        prime_status = "是" if is_prime(n) else "不是"
        print(f"{n} {prime_status}素数")

# 运行主程序
if __name__ == "__main__":
    main()
```

运行并理解每个部分的工作原理。

### 思考题4：动脑题
问题：函数式编程和命令式编程有什么不同？

思考方向：
- 命令式编程强调什么？（步骤、状态变化）
- 函数式编程强调什么？（纯函数、不可变数据、高阶函数）
- Python支持哪种范式？还是都支持？
- 在解决不同问题时，如何选择范式？
- 递归和循环有什么区别？什么时候用递归？

---

# 第二部分：基础数据结构——组织数据的方式

## 词条3：哈希表（字典）——快速查找的魔法

### 官方解释
**哈希表**（Hash Table）是一种通过键（key）直接访问值（value）的数据结构。在Python中，字典（dict）就是哈希表的实现。核心原理：通过哈希函数将键映射到数组的索引，实现O(1)的平均查找时间。

### 兔狲老师解释
哈希表就像"智能电话簿"：知道名字（键），直接找到电话号码（值）。

小小猪的比喻：
- 哈希函数：把名字变成数字编号的机器
- 哈希冲突：两个名字得到相同编号（需要解决）
- 负载因子：电话簿使用率（太满需要扩容）

Python字典的特性：
- 键必须是不可变类型（字符串、数字、元组）
- 值可以是任意类型
- 无序（Python 3.7+保持插入顺序）

### 思考题5：动手题
问题：实现一个简单的哈希表并理解其原理：

```python
# 1. Python字典的基本操作
phonebook = {}  # 创建空字典
phonebook["Alice"] = "123-4567"
phonebook["Bob"] = "987-6543"
phonebook["Charlie"] = "555-1234"

print("电话簿：", phonebook)
print("Alice的电话：", phonebook.get("Alice"))
print("David的电话：", phonebook.get("David", "未找到"))

# 2. 遍历字典
print("\n遍历电话簿：")
for name, phone in phonebook.items():
    print(f"{name}: {phone}")

# 3. 字典推导式
squares = {x: x*x for x in range(1, 6)}
print("\n平方字典：", squares)

# 4. 模拟哈希冲突解决（分离链接法）
class SimpleHashTable:
    """简单的哈希表实现"""
    
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # 每个桶是一个列表
    
    def _hash(self, key):
        """简单的哈希函数：字符串的ASCII和取模"""
        if isinstance(key, str):
            return sum(ord(c) for c in key) % self.size
        return hash(key) % self.size
    
    def put(self, key, value):
        """插入键值对"""
        index = self._hash(key)
        bucket = self.table[index]
        
        # 检查是否已存在该键
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # 更新
                return
        
        # 不存在，添加新项
        bucket.append((key, value))
    
    def get(self, key):
        """获取值"""
        index = self._hash(key)
        bucket = self.table[index]
        
        for k, v in bucket:
            if k == key:
                return v
        
        raise KeyError(f"Key '{key}' not found")
    
    def __str__(self):
        result = []
        for i, bucket in enumerate(self.table):
            if bucket:
                result.append(f"桶[{i}]: {bucket}")
        return "\n".join(result)

# 测试简单哈希表
print("\n" + "="*50)
print("简单哈希表实现：")
ht = SimpleHashTable(size=5)
ht.put("apple", 1)
ht.put("banana", 2)
ht.put("cherry", 3)
ht.put("date", 4)
ht.put("elderberry", 5)

print(ht)
print("\n获取'banana':", ht.get("banana"))
print("获取'cherry':", ht.get("cherry"))

# 测试哈希冲突
ht.put("apple", 10)  # 更新值
print("\n更新后的哈希表：")
print(ht)
```

### 思考题6：动脑题
问题：哈希表为什么能实现快速查找？有什么局限性？

思考方向：
- 哈希函数的理想特性是什么？（确定性、均匀分布、快速计算）
- 什么是哈希冲突？有哪些解决方法？（分离链接法、开放寻址法）
- 为什么Python字典的键必须是不可变类型？
- 哈希表的时间复杂度是多少？最坏情况是什么？
- 在实际应用中，如何设计好的哈希函数？

---

## 词条4：链表——灵活的动态序列

### 官方解释
**链表**（Linked List）是一种线性数据结构，由一系列节点组成，每个节点包含数据和指向下一个节点的指针。与数组不同，链表在内存中不必连续存储，插入和删除操作更高效（O(1)），但随机访问较慢（O(n)）。

链表类型：
- 单向链表：每个节点指向下一个节点
- 双向链表：每个节点指向前一个和后一个节点
- 循环链表：尾节点指向头节点

### 兔狲老师解释
链表就像"火车车厢"：每节车厢（节点）连接着下一节，可以轻松添加或移除车厢。

小小猪的比喻：
- 节点：车厢（数据 + 连接）
- 头指针：火车头
- 尾指针：最后一节车厢
- 空链表：没有车厢的火车

与数组（列表）比较：
- 数组：连续内存，快速访问，插入删除慢
- 链表：分散内存，访问慢，插入删除快

### 思考题7：动手题
问题：实现单向链表和双向链表：

```python
# 1. 单向链表节点
class SinglyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)

# 单向链表
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self, data):
        """在末尾添加节点"""
        new_node = SinglyNode(data)
        
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
        self.size += 1
    
    def prepend(self, data):
        """在开头添加节点"""
        new_node = SinglyNode(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def insert(self, index, data):
        """在指定位置插入节点"""
        if index < 0 or index > self.size:
            raise IndexError("索引超出范围")
        
        if index == 0:
            self.prepend(data)
            return
        
        new_node = SinglyNode(data)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self.size += 1
    
    def delete(self, data):
        """删除第一个匹配的节点"""
        if self.head is None:
            return False
        
        # 如果要删除的是头节点
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return True
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        
        return False
    
    def search(self, data):
        """查找节点"""
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1
    
    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) if elements else "空链表"
    
    def __len__(self):
        return self.size

# 2. 双向链表节点
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
    def __str__(self):
        return str(self.data)

# 双向链表
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, data):
        """在末尾添加节点"""
        new_node = DoublyNode(data)
        
        if self.head is None:  # 空链表
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
    
    def prepend(self, data):
        """在开头添加节点"""
        new_node = DoublyNode(data)
        
        if self.head is None:  # 空链表
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.size += 1
    
    def delete(self, data):
        """删除第一个匹配的节点"""
        current = self.head
        
        while current:
            if current.data == data:
                # 调整前后节点的指针
                if current.prev:
                    current.prev.next = current.next
                else:  # 删除的是头节点
                    self.head = current.next
                
                if current.next:
                    current.next.prev = current.prev
                else:  # 删除的是尾节点
                    self.tail = current.prev
                
                self.size -= 1
                return True
            
            current = current.next
        
        return False
    
    def forward_traversal(self):
        """前向遍历"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) if elements else "空链表"
    
    def backward_traversal(self):
        """后向遍历"""
        elements = []
        current = self.tail
        while current:
            elements.append(str(current.data))
            current = current.prev
        return " <- ".join(elements) if elements else "空链表"
    
    def __str__(self):
        return f"前向: {self.forward_traversal()}\n后向: {self.backward_traversal()}"
    
    def __len__(self):
        return self.size

# 测试单向链表
print("单向链表测试：")
sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
sll.prepend(0)
sll.insert(2, 1.5)

print("链表:", sll)
print("长度:", len(sll))
print("查找2的位置:", sll.search(2))

sll.delete(1.5)
print("删除1.5后:", sll)

print("\n" + "="*50)

# 测试双向链表
print("双向链表测试：")
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.prepend(0)

print(dll)
print("长度:", len(dll))

dll.delete(2)
print("\n删除2后:")
print(dll)
```

### 思考题8：动脑题
问题：链表和数组（列表）各有什么优缺点？如何选择？

思考方向：
- 在什么情况下应该使用链表而不是数组？
- 链表的插入删除为什么是O(1)？数组为什么是O(n)？
- 链表的随机访问为什么是O(n)？数组为什么是O(1)？
- 内存局部性对性能有什么影响？
- 实际应用中，哪些数据结构基于链表实现？（栈、队列、哈希表的冲突解决）

---

## 词条5：树——层次化数据结构

### 官方解释
**树**（Tree）是一种层次化的非线性数据结构，由节点和边组成。每个树有一个根节点，每个节点可以有零个或多个子节点，没有子节点的节点称为叶节点。

常见树类型：
- 二叉树：每个节点最多有两个子节点（左子节点、右子节点）
- 二叉搜索树（BST）：左子树所有节点值小于根节点，右子树所有节点值大于根节点
- 平衡二叉树（AVL树、红黑树）：保持树的高度平衡
- 堆：完全二叉树，满足堆属性（最大堆、最小堆）

### 兔狲老师解释
树就像"家族族谱"或"公司组织结构"。

小小猪的比喻：
- 根节点：家族的祖先或公司CEO
- 子节点：后代或下属
- 叶节点：没有后代的人或基层员工
- 深度：从根到节点的边数
- 高度：从节点到最深叶节点的边数

树的遍历方式：
- 前序遍历：根→左→右
- 中序遍历：左→根→右（对BST得到有序序列）
- 后序遍历：左→右→根
- 层序遍历：按层次从上到下、从左到右

### 思考题9：动手题
问题：实现二叉树和二叉搜索树：

```python
# 1. 二叉树节点
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.value)

# 二叉树
class BinaryTree:
    def __init__(self, root_value=None):
        if root_value is not None:
            self.root = TreeNode(root_value)
        else:
            self.root = None
    
    # 遍历方法
    def preorder(self, node=None, result=None):
        """前序遍历：根→左→右"""
        if result is None:
            result = []
        if node is None:
            node = self.root
        
        if node:
            result.append(node.value)
            self.preorder(node.left, result)
            self.preorder(node.right, result)
        
        return result
    
    def inorder(self, node=None, result=None):
        """中序遍历：左→根→右"""
        if result is None:
            result = []
        if node is None:
            node = self.root
        
        if node:
            self.inorder(node.left, result)
            result.append(node.value)
            self.inorder(node.right, result)
        
        return result
    
    def postorder(self, node=None, result=None):
        """后序遍历：左→右→根"""
        if result is None:
            result = []
        if node is None:
            node = self.root
        
        if node:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(node.value)
        
        return result
    
    def level_order(self):
        """层序遍历"""
        if not self.root:
            return []
        
        result = []
        queue = [self.root]
        
        while queue:
            node = queue.pop(0)
            result.append(node.value)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result
    
    def height(self, node=None):
        """计算树的高度"""
        if node is None:
            node = self.root
        
        if node is None:
            return 0
        
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        
        return max(left_height, right_height) + 1
    
    def __str__(self):
        return f"前序: {self.preorder()}\n中序: {self.inorder()}\n后序: {self.postorder()}\n层序: {self.level_order()}"

# 2. 二叉搜索树
class BinarySearchTree(BinaryTree):
    def insert(self, value):
        """插入值到二叉搜索树"""
        if self.root is None:
            self.root = TreeNode(value)
            return
        
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = TreeNode(value)
                    break
                else:
                    current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = TreeNode(value)
                    break
                else:
                    current = current.right
            else:
                # 值已存在，不插入重复值
                break
    
    def search(self, value):
        """在二叉搜索树中查找值"""
        current = self.root
        
        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        
        return False
    
    def find_min(self, node=None):
        """找到最小值节点"""
        if node is None:
            node = self.root
        
        while node and node.left:
            node = node.left
        
        return node.value if node else None
    
    def find_max(self, node=None):
        """找到最大值节点"""
        if node is None:
            node = self.root
        
        while node and node.right:
            node = node.right
        
        return node.value if node else None

# 测试二叉树
print("二叉树测试：")
bt = BinaryTree(1)
bt.root.left = TreeNode(2)
bt.root.right = TreeNode(3)
bt.root.left.left = TreeNode(4)
bt.root.left.right = TreeNode(5)
bt.root.right.left = TreeNode(6)
bt.root.right.right = TreeNode(7)

print(bt)
print("树的高度:", bt.height())

print("\n" + "="*50)

# 测试二叉搜索树
print("二叉搜索树测试：")
bst = BinarySearchTree()
values = [50, 30, 70, 20, 40, 60, 80]
for v in values:
    bst.insert(v)

print(bst)
print("查找40:", bst.search(40))
print("查找90:", bst.search(90))
print("最小值:", bst.find_min())
print("最大值:", bst.find_max())
```

### 思考题10：动脑题
问题：树结构在计算机科学中有哪些重要应用？

思考方向：
- 文件系统如何用树结构组织？
- 数据库索引为什么常用B树、B+树？
- HTML/XML文档为什么是树结构？
- 决策树在机器学习中如何工作？
- 游戏中的AI决策树是什么？

---

## 词条6：图——复杂关系的网络

### 官方解释
**图**（Graph）是由顶点（Vertex）和边（Edge）组成的非线性数据结构，用于表示对象之间的关系。图是树的一般化形式（树是无环连通图）。

图的分类：
- 无向图：边没有方向
- 有向图：边有方向
- 加权图：边有权重
- 连通图：任意两个顶点都有路径相连
- 完全图：每对顶点之间都有边

图的表示方法：
- 邻接矩阵：二维数组，matrix[i][j]表示顶点i到j的边
- 邻接表：数组的数组，每个顶点有一个邻居列表

### 兔狲老师解释
图就像"社交网络"或"交通网络"。

小小猪的比喻：
- 顶点：人（社交网络）或城市（交通网络）
- 边：朋友关系或道路
- 权重：亲密度或距离
- 路径：从一个人到另一个人的朋友链

图算法应用：
- 最短路径：导航软件找最短路线
- 最小生成树：电网布线最省材料
- 拓扑排序：课程安排、任务调度
- 连通分量：社交网络中的朋友圈

### 思考题11：动手题
问题：实现图的基本结构和算法：

```python
# 1. 图的邻接表表示
class Graph:
    def __init__(self, directed=False):
        self.vertices = {}  # 顶点字典：顶点名 -> 顶点对象
        self.directed = directed  # 是否是有向图
    
    def add_vertex(self, name):
        """添加顶点"""
        if name not in self.vertices:
            self.vertices[name] = Vertex(name)
    
    def add_edge(self, from_vertex, to_vertex, weight=1):
        """添加边"""
        if from_vertex not in self.vertices:
            self.add_vertex(from_vertex)
        if to_vertex not in self.vertices:
            self.add_vertex(to_vertex)
        
        self.vertices[from_vertex].add_neighbor(to_vertex, weight)
        
        if not self.directed:  # 无向图需要添加反向边
            self.vertices[to_vertex].add_neighbor(from_vertex, weight)
    
    def get_vertices(self):
        """获取所有顶点"""
        return list(self.vertices.keys())
    
    def get_edges(self):
        """获取所有边"""
        edges = []
        for from_vertex in self.vertices:
            for to_vertex, weight in self.vertices[from_vertex].neighbors.items():
                edges.append((from_vertex, to_vertex, weight))
        return edges
    
    def __str__(self):
        result = []
        for vertex_name, vertex in self.vertices.items():
            neighbors = ", ".join([f"{n}({w})" for n, w in vertex.neighbors.items()])
            result.append(f"{vertex_name}: {neighbors}")
        return "\n".join(result)

class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}  # 邻居字典：邻居名 -> 权重
    
    def add_neighbor(self, neighbor, weight=1):
        """添加邻居"""
        self.neighbors[neighbor] = weight
    
    def __str__(self):
        return self.name

# 2. 图的遍历算法
def bfs(graph, start):
    """广度优先搜索"""
    if start not in graph.vertices:
        return []
    
    visited = set()
    queue = [start]
    result = []
    
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            
            # 添加所有未访问的邻居
            for neighbor in graph.vertices[vertex].neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return result

def dfs(graph, start):
    """深度优先搜索（递归）"""
    if start not in graph.vertices:
        return []
    
    visited = set()
    result = []
    
    def dfs_recursive(vertex):
        visited.add(vertex)
        result.append(vertex)
        
        for neighbor in graph.vertices[vertex].neighbors:
            if neighbor not in visited:
                dfs_recursive(neighbor)
    
    dfs_recursive(start)
    return result

# 3. 最短路径算法（Dijkstra）
import heapq

def dijkstra(graph, start, end):
    """Dijkstra算法求最短路径"""
    if start not in graph.vertices or end not in graph.vertices:
        return float('inf'), []
    
    # 初始化距离字典
    distances = {vertex: float('inf') for vertex in graph.vertices}
    distances[start] = 0
    
    # 初始化前驱字典
    predecessors = {vertex: None for vertex in graph.vertices}
    
    # 优先队列
    pq = [(0, start)]
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        # 如果找到更短的路径，跳过
        if current_distance > distances[current_vertex]:
            continue
        
        # 遍历邻居
        for neighbor, weight in graph.vertices[current_vertex].neighbors.items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))
    
    # 重建路径
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = predecessors[current]
    path.reverse()
    
    return distances[end], path if distances[end] != float('inf') else []

# 测试图
print("图结构测试：")
g = Graph(directed=False)

# 添加边（模拟城市交通）
g.add_edge("北京", "上海", 1000)
g.add_edge("北京", "广州", 2000)
g.add_edge("上海", "广州", 1500)
g.add_edge("上海", "成都", 1800)
g.add_edge("广州", "成都", 1200)
g.add_edge("成都", "西安", 800)
g.add_edge("北京", "西安", 1100)

print("图结构：")
print(g)
print("\n所有顶点:", g.get_vertices())
print("所有边:", g.get_edges())

print("\n" + "="*50)

# 测试遍历算法
print("遍历算法测试：")
print("BFS从北京开始:", bfs(g, "北京"))
print("DFS从北京开始:", dfs(g, "北京"))

print("\n" + "="*50)

# 测试最短路径
print("最短路径测试：")
distance, path = dijkstra(g, "北京", "成都")
print(f"北京到成都的最短距离: {distance} km")
print(f"路径: {' -> '.join(path)}")

distance, path = dijkstra(g, "上海", "西安")
print(f"\n上海到西安的最短距离: {distance} km")
print(f"路径: {' -> '.join(path)}")
```

### 思考题12：动脑题
问题：图论在现实世界中有哪些重要应用？

思考方向：
- 社交网络分析如何用图论？
- 网页排名算法（PageRank）如何用图？
- 推荐系统如何用图表示用户-物品关系？
- 物流配送如何用图优化路线？
- 电路设计如何用图表示连接关系？

---

# 第三部分：算法与例题——解决问题的艺术

## 词条7：排序与搜索算法

### 官方解释
**排序算法**将数据按特定顺序排列，**搜索算法**在数据集中查找特定元素。这是计算机科学中最基础、最重要的算法类别。

常见排序算法：
- 冒泡排序：简单但低效，O(n²)
- 选择排序：每次选择最小元素，O(n²)
- 插入排序：像整理扑克牌，O(n²)
- 归并排序：分治策略，O(n log n)
- 快速排序：分治策略，平均O(n log n)

常见搜索算法：
- 线性搜索：逐个检查，O(n)
- 二分搜索：要求有序，O(log n)

### 兔狲老师解释
排序就像"整理书架"，搜索就像"在书架上找书"。

小小猪的比喻：
- 冒泡排序：像气泡上浮，小的往上冒
- 快速排序：选一个"基准"，小的放左边，大的放右边
- 二分搜索：每次排除一半，快速缩小范围

算法复杂度：
- 时间复杂度：算法执行时间随输入规模的增长
- 空间复杂度：算法需要的内存空间

### 思考题13：动手题
问题：实现几种排序和搜索算法：

```python
# 1. 排序算法实现
def bubble_sort(arr):
    """冒泡排序"""
    n = len(arr)
    for i in range(n):
        # 最后i个元素已经排好序
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    """选择排序"""
    n = len(arr)
    for i in range(n):
        # 找到最小元素的索引
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # 交换
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    """插入排序"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # 将比key大的元素向右移动
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    """归并排序"""
    if len(arr) <= 1:
        return arr
    
    # 分割
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # 合并
    return merge(left, right)

def merge(left, right):
    """合并两个有序数组"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr):
    """快速排序"""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # 选择中间元素作为基准
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# 2. 搜索算法实现
def linear_search(arr, target):
    """线性搜索"""
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

def binary_search(arr, target):
    """二分搜索（要求数组已排序）"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# 测试排序算法
print("排序算法测试：")
test_array = [64, 34, 25, 12, 22, 11, 90]
print("原始数组:", test_array)

print("\n冒泡排序:", bubble_sort(test_array.copy()))
print("选择排序:", selection_sort(test_array.copy()))
print("插入排序:", insertion_sort(test_array.copy()))
print("归并排序:", merge_sort(test_array.copy()))
print("快速排序:", quick_sort(test_array.copy()))

print("\n" + "="*50)

# 测试搜索算法
print("搜索算法测试：")
sorted_array = [11, 12, 22, 25, 34, 64, 90]
print("有序数组:", sorted_array)

target = 25
print(f"\n线性搜索 {target}: 索引 {linear_search(sorted_array, target)}")
print(f"二分搜索 {target}: 索引 {binary_search(sorted_array, target)}")

target = 100
print(f"\n线性搜索 {target}: 索引 {linear_search(sorted_array, target)}")
print(f"二分搜索 {target}: 索引 {binary_search(sorted_array, target)}")
```

### 思考题14：动脑题
问题：如何选择合适的排序算法？

思考方向：
- 数据规模小时，为什么插入排序可能比快速排序快？
- 什么时候应该用稳定排序？（稳定排序：相等元素的相对顺序不变）
- 内存受限时应该选择什么排序算法？
- 数据几乎有序时，什么排序算法最快？
- 在实际应用中，Python的sorted()函数用什么算法？

---

## 词条8：动态规划与贪心算法

### 官方解释
**动态规划**（Dynamic Programming）通过将复杂问题分解为重叠子问题来求解，保存子问题的解避免重复计算。**贪心算法**（Greedy Algorithm）每一步都选择当前最优解，希望最终得到全局最优解。

动态规划特点：
- 最优子结构：问题的最优解包含子问题的最优解
- 重叠子问题：子问题会被重复计算
- 记忆化：保存已计算子问题的结果

贪心算法特点：
- 局部最优选择
- 不保证全局最优
- 通常更简单高效

### 兔狲老师解释
动态规划就像"建备忘录"，贪心算法就像"眼前利益最大化"。

小小猪的比喻：
- 动态规划：爬楼梯问题，记住每步的结果
- 贪心算法：找零钱问题，每次选最大面额

适用场景：
- 动态规划：背包问题、最长公共子序列、最短路径
- 贪心算法：霍夫曼编码、最小生成树、活动选择

### 思考题15：动手题
问题：实现动态规划和贪心算法解决经典问题：

```python
# 1. 动态规划：斐波那契数列
def fibonacci_dp(n):
    """动态规划求斐波那契数列"""
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

def fibonacci_memo(n, memo=None):
    """记忆化递归求斐波那契数列"""
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

# 2. 动态规划：0-1背包问题
def knapsack_01(weights, values, capacity):
    """0-1背包问题动态规划"""
    n = len(weights)
    # dp[i][w] 表示前i个物品，容量为w时的最大价值
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # 选择：放入或不放入
                dp[i][w] = max(
                    dp[i - 1][w],  # 不放入
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]  # 放入
                )
            else:
                dp[i][w] = dp[i - 1][w]  # 放不下
    
    # 回溯找出选择的物品
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i - 1)
            w -= weights[i - 1]
    
    selected.reverse()
    return dp[n][capacity], selected

# 3. 贪心算法：找零钱问题
def coin_change_greedy(coins, amount):
    """贪心算法找零钱（硬币面额递减）"""
    coins.sort(reverse=True)  # 从大到小排序
    result = []
    
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
    
    return result if amount == 0 else None

# 4. 贪心算法：活动选择问题
def activity_selection(start_times, finish_times):
    """贪心算法选择最多互不冲突的活动"""
    # 按结束时间排序
    activities = sorted(zip(start_times, finish_times), key=lambda x: x[1])
    
    selected = []
    last_finish = 0
    
    for start, finish in activities:
        if start >= last_finish:
            selected.append((start, finish))
            last_finish = finish
    
    return selected

# 测试动态规划
print("动态规划测试：")
print("斐波那契数列（动态规划）:")
for i in range(10):
    print(f"F({i}) = {fibonacci_dp(i)}", end="  ")
print()

print("\n斐波那契数列（记忆化递归）:")
for i in range(10):
    print(f"F({i}) = {fibonacci_memo(i)}", end="  ")
print()

print("\n" + "="*50)

# 测试0-1背包问题
print("0-1背包问题测试：")
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 8

max_value, selected_items = knapsack_01(weights, values, capacity)
print(f"物品重量: {weights}")
print(f"物品价值: {values}")
print(f"背包容量: {capacity}")
print(f"最大价值: {max_value}")
print(f"选择的物品索引: {selected_items}")
print(f"选择的物品重量: {[weights[i] for i in selected_items]}")
print(f"选择的物品价值: {[values[i] for i in selected_items]}")

print("\n" + "="*50)

# 测试贪心算法
print("贪心算法测试：")
print("找零钱问题：")
coins = [1, 5, 10, 25]
amount = 63
change = coin_change_greedy(coins, amount)
print(f"硬币面额: {coins}")
print(f"金额: {amount}")
print(f"找零方案: {change}")
print(f"硬币数量: {len(change)}")

print("\n活动选择问题：")
start_times = [1, 3, 0, 5, 8, 5]
finish_times = [2, 4, 6, 7, 9, 9]
selected_activities = activity_selection(start_times, finish_times)
print(f"开始时间: {start_times}")
print(f"结束时间: {finish_times}")
print(f"选择的活动: {selected_activities}")
print(f"活动数量: {len(selected_activities)}")
```

### 思考题16：动脑题
问题：动态规划和贪心算法各有什么优缺点？如何选择？

思考方向：
- 什么情况下贪心算法能得到最优解？
- 动态规划的时间复杂度和空间复杂度如何？
- 记忆化搜索和自底向上动态规划有什么区别？
- 在实际问题中，如何判断是否具有最优子结构？
- 分治算法和动态规划有什么区别？

---

# 第四部分：Python进阶——面向对象与函数式编程

## 词条9：面向对象编程高级特性

### 官方解释
**面向对象编程**（OOP）不仅包括基本的类、对象、继承，还有更多高级特性：多重继承、抽象类、接口、属性装饰器、类方法、静态方法、魔术方法等。

Python OOP特性：
- 多重继承：一个类可以继承多个父类
- 抽象基类（ABC）：定义接口，不能实例化
- 属性装饰器：@property, @setter, @deleter
- 类方法和静态方法：@classmethod, @staticmethod
- 魔术方法：`__init__`, `__str__`, `__len__`等

### 兔狲老师解释
OOP高级特性让代码更灵活、更安全、更易维护。

小小猪的比喻：
- 多重继承：像混血儿，继承父母双方特征
- 抽象类：像设计规范，规定必须实现的方法
- 属性装饰器：像智能门卫，控制对属性的访问
- 魔术方法：像魔法咒语，让对象有特殊行为

设计原则：
- 单一职责原则：一个类只做一件事
- 开放封闭原则：对扩展开放，对修改封闭
- 里氏替换原则：子类可以替换父类
- 接口隔离原则：接口要小而专
- 依赖倒置原则：依赖抽象，不依赖具体

### 思考题17：动手题
问题：实现OOP高级特性示例：

```python
# 1. 多重继承
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "..."

class Mammal(Animal):
    def give_birth(self):
        return f"{self.name} gives birth to live young"

class Bird(Animal):
    def lay_eggs(self):
        return f"{self.name} lays eggs"

class Platypus(Mammal, Bird):
    """鸭嘴兽：既是哺乳动物又是卵生"""
    def speak(self):
        return "Quack?"

# 2. 抽象基类
from abc import ABC, abstractmethod

class Shape(ABC):
    """形状抽象基类"""
    
    @abstractmethod
    def area(self):
        """计算面积"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """计算周长"""
        pass
    
    def describe(self):
        """通用描述方法"""
        return f"这是一个形状，面积={self.area():.2f}，周长={self.perimeter():.2f}"

class Circle(Shape):
    """圆形"""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """矩形"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# 3. 属性装饰器
class BankAccount:
    """银行账户"""
    
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self._balance = initial_balance  # 私有属性
    
    @property
    def balance(self):
        """获取余额"""
        return self._balance
    
    @balance.setter
    def balance(self, amount):
        """设置余额（有验证）"""
        if amount < 0:
            raise ValueError("余额不能为负数")
        self._balance = amount
    
    @balance.deleter
    def balance(self):
        """删除余额（实际是重置）"""
        print(f"警告：正在重置{self.owner}的余额")
        self._balance = 0
    
    def deposit(self, amount):
        """存款"""
        if amount <= 0:
            raise ValueError("存款金额必须为正数")
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        """取款"""
        if amount <= 0:
            raise ValueError("取款金额必须为正数")
        if amount > self.balance:
            raise ValueError("余额不足")
        self.balance -= amount
        return self.balance

# 4. 类方法和静态方法
class Date:
    """日期类"""
    
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"
    
    @classmethod
    def from_string(cls, date_string):
        """从字符串创建日期对象（类方法）"""
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)
    
    @staticmethod
    def is_leap_year(year):
        """判断是否为闰年（静态方法）"""
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    @property
    def is_leap(self):
        """判断当前年份是否为闰年（属性）"""
        return self.is_leap_year(self.year)

# 测试多重继承
print("多重继承测试：")
perry = Platypus("Perry the Platypus")
print(f"名字: {perry.name}")
print(f"叫声: {perry.speak()}")
print(f"繁殖方式1: {perry.give_birth()}")
print(f"繁殖方式2: {perry.lay_eggs()}")

print("\n" + "="*50)

# 测试抽象基类
print("抽象基类测试：")
circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"圆形: {circle.describe()}")
print(f"矩形: {rectangle.describe()}")

print("\n" + "="*50)

# 测试属性装饰器
print("属性装饰器测试：")
account = BankAccount("小小猪", 1000)
print(f"账户所有者: {account.owner}")
print(f"初始余额: {account.balance}")

account.deposit(500)
print(f"存款500后余额: {account.balance}")

account.withdraw(300)
print(f"取款300后余额: {account.balance}")

try:
    account.withdraw(2000)
except ValueError as e:
    print(f"取款失败: {e}")

print("\n" + "="*50)

# 测试类方法和静态方法
print("类方法和静态方法测试：")
date1 = Date(2023, 12, 25)
date2 = Date.from_string("2024-02-29")

print(f"日期1: {date1}")
print(f"日期2: {date2}")
print(f"2023是闰年吗？{Date.is_leap_year(2023)}")
print(f"2024是闰年吗？{Date.is_leap_year(2024)}")
print(f"日期2的年份是闰年吗？{date2.is_leap}")
```

### 思考题18：动脑题
问题：面向对象设计原则在实际编程中如何应用？

思考方向：
- 如何判断一个类是否违反了单一职责原则？
- 在什么情况下应该使用组合而不是继承？
- 接口隔离原则如何提高代码的可维护性？
- 依赖注入是什么？如何实现？
- 设计模式（工厂、观察者、策略等）如何体现设计原则？

---

## 词条10：函数式编程与Pythonic代码

### 官方解释
**函数式编程**（Functional Programming）是一种编程范式，强调纯函数、不可变数据、高阶函数、函数组合。Python虽然不是纯函数式语言，但支持许多函数式特性。

Python函数式特性：
- 高阶函数：函数可以作为参数或返回值
- 匿名函数：lambda表达式
- 内置高阶函数：map, filter, reduce
- 列表推导式、字典推导式、集合推导式
- 生成器：惰性求值，节省内存

Pythonic代码：
- 简洁、清晰、易读
- 利用Python特有语法和特性
- 符合"Python之禅"（import this）

### 兔狲老师解释
函数式编程让代码更简洁、更可预测、更易测试。

小小猪的比喻：
- 纯函数：像数学函数，相同输入总是相同输出
- 高阶函数：像函数工厂，生产或消费函数
- 生成器：像流水线，需要时才生产数据
- 装饰器：像包装纸，给函数添加功能

Pythonic哲学：
- 优美胜于丑陋
- 明了胜于晦涩
- 简洁胜于复杂
- 可读性很重要

### 思考题19：动手题
问题：实践函数式编程和Pythonic代码：

```python
# 1. 高阶函数和lambda
def apply_operation(numbers, operation):
    """应用操作到每个数字（高阶函数）"""
    return [operation(n) for n in numbers]

# 使用lambda定义简单操作
numbers = [1, 2, 3, 4, 5]
print("原始数字:", numbers)

double = lambda x: x * 2
square = lambda x: x ** 2
increment = lambda x: x + 1

print("加倍:", apply_operation(numbers, double))
print("平方:", apply_operation(numbers, square))
print("加1:", apply_operation(numbers, increment))

# 2. 内置高阶函数
print("\n内置高阶函数：")
print("map加倍:", list(map(double, numbers)))
print("filter偶数:", list(filter(lambda x: x % 2 == 0, numbers)))

from functools import reduce
print("reduce求和:", reduce(lambda x, y: x + y, numbers))
print("reduce求积:", reduce(lambda x, y: x * y, numbers))

# 3. 列表推导式 vs 传统循环
print("\n列表推导式 vs 传统循环：")

# 传统方式
squares_old = []
for n in numbers:
    squares_old.append(n ** 2)

# Pythonic方式
squares_new = [n ** 2 for n in numbers]

print("传统方式:", squares_old)
print("Pythonic方式:", squares_new)

# 带条件的列表推导式
even_squares = [n ** 2 for n in numbers if n % 2 == 0]
print("偶数的平方:", even_squares)

# 4. 字典推导式和集合推导式
print("\n字典推导式和集合推导式：")

# 字典推导式
square_dict = {n: n ** 2 for n in numbers}
print("数字平方字典:", square_dict)

# 集合推导式（自动去重）
numbers_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_squares = {n ** 2 for n in numbers_with_duplicates}
print("唯一平方集合:", unique_squares)

# 5. 生成器
print("\n生成器：")

def fibonacci_generator(n):
    """生成斐波那契数列的生成器"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

print("斐波那契数列（前10个）:")
for num in fibonacci_generator(10):
    print(num, end=" ")

print("\n\n生成器表达式:")
# 生成器表达式（惰性求值）
big_numbers = (x ** 2 for x in range(1000000) if x % 100000 == 0)
print("大数字生成器（前5个）:")
for i, num in enumerate(big_numbers):
    if i >= 5:
        break
    print(num, end=" ")

# 6. 装饰器
print("\n\n装饰器：")

def timer_decorator(func):
    """计时装饰器"""
    import time
    
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} 执行时间: {end_time - start_time:.6f}秒")
        return result
    
    return wrapper

def cache_decorator(func):
    """缓存装饰器（记忆化）"""
    cache = {}
    
    def wrapper(*args):
        if args in cache:
            print(f"从缓存获取 {func.__name__}{args}")
            return cache[args]
        result = func(*args)
        cache[args] = result
        print(f"计算并缓存 {func.__name__}{args} = {result}")
        return result
    
    return wrapper

@timer_decorator
@cache_decorator
def slow_fibonacci(n):
    """慢速斐波那契计算（用于演示）"""
    if n <= 1:
        return n
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)

print("\n带装饰器的斐波那契计算:")
print(f"F(5) = {slow_fibonacci(5)}")
print(f"F(5) = {slow_fibonacci(5)}")  # 第二次应该从缓存获取
print(f"F(6) = {slow_fibonacci(6)}")
```

### 思考题20：动脑题
问题：函数式编程和面向对象编程如何结合使用？

思考方向：
- 在什么场景下函数式编程更有优势？
- 如何用函数式思想改进面向对象代码？
- Python的装饰器如何体现函数式特性？
- 不可变数据在并发编程中有什么优势？
- 如何平衡Pythonic代码和性能优化？

---

## 兔狲学院Python小结

### 学习收获
通过本章学习，你掌握了：

1. **Python基础语法**：
   - 变量、数据类型、运算符
   - 控制结构、函数、模块化编程

2. **四种基础数据结构**：
   - **哈希表（字典）**：快速查找的魔法
   - **链表**：灵活的动态序列
   - **树**：层次化数据结构
   - **图**：复杂关系的网络

3. **算法思维**：
   - 排序与搜索算法
   - 动态规划与贪心算法
   - 时间复杂度与空间复杂度分析

4. **Python进阶**：
   - 面向对象编程高级特性
   - 函数式编程与Pythonic代码
   - 设计原则与最佳实践

### 兔狲教授的最后一课
"亲爱的未来推理科学家：

编程不是关于记忆语法，而是关于表达思想；不是关于控制计算机，而是关于解决问题。

Python就像一支好用的笔，数据结构就像不同的纸张，算法就像写作技巧。好的程序员不是记住所有语法，而是知道如何选择合适的工具解决问题。

记住：
1. **代码是写给人看的**，只是恰好能被计算机执行
2. **清晰的思维产生清晰的代码**，清晰的代码解决复杂的问题
3. **数据结构是算法的基石**，选择合适的数据结构事半功倍
4. **算法是解决问题的艺术**，理解原理比记住实现更重要
5. **编程是终身学习**，保持好奇，持续实践

现在，你拥有了从基础语法到数据结构的完整工具箱。但工具的价值在于使用。用这些工具去实现你的想法，解决真实的问题，创造有用的程序。

推理的民主化不是让每个人成为专家，而是让每个人都能使用这些强大的思维工具。Python降低了编程的门槛，让你能专注于思考而不是语法。

现在，轮到你去探索、去创造、去推理了。

兔狲教授在黑石屋的书房里，泡好茶，运行着Python解释器，等着看你的代码。"

---

## 兔狲学院四章总结

经过四章的学习，你已经掌握了从中学到大学过渡的完整知识体系：

1. **微积分**：理解变化与累积的语言
2. **线性代数**：处理多维数据的工具  
3. **西方近代以前哲学**：理性思维的基础训练
4. **Python编程与数据结构**：计算思维的实践工具

这些知识不是孤立的学科，而是相互关联的思维框架：
- 用微积分理解变化，用线性代数处理结构
- 用哲学追问根本，用编程实现想法
- 用数据结构组织信息，用算法解决问题

**致未来的推理科学家**：
你现在拥有了探索知识世界的基本工具。但记住，工具的价值在于使用。真正的学习发生在实践中，在解决问题中，在创造价值中。

推理的民主化意味着每个人都应该有机会掌握这些强大的思维工具。现在，这个机会在你手中。

去探索吧，去创造吧，去推理吧。世界需要更多像你一样的思考者。

兔狲教授在黑石屋的书房里，泡好茶，运行着Python解释器，等着听你的发现。"