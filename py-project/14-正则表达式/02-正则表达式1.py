'''
常用的匹配规则：
. 匹配任意一个字符，除了换行符
[abc] 匹配abc中任意一个字符
\d 匹配一个0-9数字
\D 非数字
\s 空白符
\S 非空白符
\w 单词字符，即a-z、A-Z、0-9、下划线
\W 非单词字符
'''

import re
from unicodedata import name

myString = 'aaaa'
pattern = '.'  # .是匹配除换行符之外的字符
result = re.match(pattern, myString)
print(result.group())
pattern = '..'
result = re.match(pattern, myString)
print(result.group())
myString = 'a1a1'
result = re.match(pattern, myString)
print(result.group())

names = 'method', 'memory', 'subString', 'money'
print(names)
pattern = 'me(.*)'
for item in names:
    res = re.match(pattern, item)
    if res is not None:
        print(res.group())

# []中括号的匹配规则是，匹配括号中任意一个字符
str1 = 'helloawdawdawd'
pattern1 = '[ha]'
res = re.match(pattern1, str1)  # 注意，match只能匹配以pattern开头的
print(res.group())

'''
匹配数量：
* 0或无限次
+ 1或无限次
\? 0或1次
{m} 出现m次
{m,} 至少m次
{n,m} 出现n到m次

开头结尾：
^ 匹配开头
$ 匹配结尾
'''

print(re.match("^p.*", "Python is the best language", re.I).group())
print(re.match("^p\w{5}", "Python is the best language", re.I).group())  # 取Python

# 匹配邮箱的结尾(必须以.com结尾)
print(re.match("[\w]{5,15}@[\w]{2,}.com$", "529106896@qq.com").group())
print(re.match("[\w]{5,15}@[\w]{2,}.com$", "529106896@gmail.com").group())
print(re.match("[\w]{5,15}@[\w]{2,}.com$", "529106896@gmail.com").group())

'''
分组匹配
| 匹配左右任意一个表达式
(ab) 将括号内字符作为一个分组
\num 引用分组num匹配到的字符串
(?P) 给分组起别名
(?P=name) 引用别名为name分组匹配到的字符串 
'''
res = re.match(r'([0-9]*)-(\d*)', '0391-21312424')
print(res.group())

# \num的用法，只有在有分组时才起效
test = "<html><h1>测试数据</h1></html>"
res = re.match(r'<(.+)><(.+)>(.+)</\2></\1>', test)  # \2是引用第二个分组，\1是引用第一个分组
print(res.group())

# 别名的使用  起名字(?P<name>)  引用(?P=name)
res = re.match(r'<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>', test)
print(res.group())
