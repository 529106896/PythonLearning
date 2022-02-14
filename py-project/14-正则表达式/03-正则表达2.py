# re.compile方法
# 把正则表达式编译成一个正则表达式对象，让正则表达式对象复用效率更高
import re
pat = re.compile("\d{4}")
res = pat.match("123456")
print(res.group())

# re.search 在全文中匹配一次，匹配到就返回
res = re.search("world", "Hello World", re.I)
print(res.group())

# findall返回所有匹配到的数据，常用于爬虫
data = "I am a Chinese, China love me. china Cheses"
res = re.findall(r"Chi[\w]{2,}", data, re.I)
print(res)

# sub 替换
# sub(pattern, repl, string, count, flags)
ret = re.sub("h", "H", "hello hello helloWorld")
print(ret)

str1 = "Python is the best language in the world"
pattern1 = r"^P([a-zA-Z]+)"
print(re.sub(pattern1, "Java", str1))

# subn 替换，并且返回替换的次数
str1 = "Python is the best language in the world. Python is a jiba"
pattern1 = r"P([a-zA-Z]+)"
print(re.subn(pattern1, "Java", str1))

# split 分割
# split(pattern, string, maxsplit, flags)
st1 = "Baidu  huawei Tencent MiHoYo        RedHat"
print(re.split("[ ]+", st1))
