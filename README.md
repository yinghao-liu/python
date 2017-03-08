# python

python test
n中的变量不需要声明，给变量赋值即可创建该变量，使用del var_name可以删除变量var_name，变量本身没有类型，类型是指变量所指的内存对象中对象的类型，有以下几类：

- 数字
- 字符串 (str)
- 列表 (list)
- 元组（tuple）
- 集合（set）
- 字典（dict）

一个变量可以通过赋值指向不同类型的数据。

## 数字

有下面四种类型
- int （1）
- float （1.23）
- bool （True和False）
- complex （1+2j）


## 字符串

- 单引号和双引号用法一致
- 三引号（'''或者"""），多行字符串，方便排版
- 在字符串前加r或R，所见即所得
- 在字符串前加u或U，表示unicode字符串
- 'abcde'[0:-1] ： 截取从第一位到倒数第二位（即‘abcd’）
- 'abcde'+'fg' ：字符串连接，结果为'abcdefg'
- 'abcde' * 2 :字符串重复2次，结果为'abcdeabcde'
- 字符串内容不能被改变，形如str[1]='a'的赋值操作是错误的

## 列表

- 列表是python中使用最频繁的数据类型
- 列表元素写在“[]”内，以“,”分割，元素的类型可以是数字、字符串和列表
- 列表也支持截取、连接和重复操作（详见字符串部分）
- 与字符串不同，列表的元素是可以改变的


## 元组

元组和列表类似，只是元组元素不能修改,元组元素写在“()”内，以“,”分割
```
tup1 = ()   #空元组赋值
tup2 = (1,) #一个元素，需要在单个元素后加“,” 
```

## 集合

集合是一个无序不重复元素的序列，也就是说相同值的元素成员只有一个，可用以进行成员关系测试和删除重复元素，用“{}”或set()函数创建
```
setnone = set() #创建一个空集合，仅此一种方式，不能使用 setnone = {} ,这是字典
student = ({'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'})

print(student)   # 输出集合，重复的元素被自动去掉

# 成员测试
if('Rose' in student) :
    print('Rose 在集合中')
else :
    print('Rose 不在集合中')


# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)

print(a - b)     # a和b的差集

print(a | b)     # a和b的并集

print(a & b)     # a和b的交集

print(a ^ b)     # a和b中不同时存在的元素

```

## 字典

字典是一种映射类型，用“{}”标识，是一个无序的键(key):值(value)对集合，键（key）必须使用不可变类型，且在一个字典中，键（key）必须是唯一的。
```
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}


print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值
```

## 参考
1. [菜鸟教程](http://www.runoob.com/python3/python3-data-type.html)

