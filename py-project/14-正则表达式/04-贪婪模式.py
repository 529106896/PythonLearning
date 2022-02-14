# 在正则表达式后加上问号，变为非贪婪模式，尽可能少的匹配
import re

rs = re.match(r'\d{6,9}', '111222333')
print(rs.group())

rs = re.match(r'\d{6,9}?', '111222333')
print(rs.group())

rs = re.match(r'a.*b', 'aacbacbc')
print(rs.group())  # 贪婪模式

rs = re.match(r'a.*?b', 'aacbacbc')
print(rs.group())  # 费贪婪模式
