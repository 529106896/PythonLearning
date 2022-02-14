# 单分支：
# if 条件表达式:
#   代码
#   ...

score = 40
if score >= 60:  # 注意这里的冒号
    print("你合格了")
    pass  # 这个pass是一个空语句，结束当前if用。也可以直接取消缩进顶格写
print("退出if")

'''
多分支：
if 条件表达式:
    代码
    ...
    pass
else:
    代码
    pass
'''
if score >= 60:
    print("你合格了")
    pass
else:
    print("你不合格")
    pass

'''
第二种多分支：
if 条件表达式:
    代码
    pass
elif 条件表达式:
    代码
    pass
elif 条件表达式:
    代码
    pass
else:  （这个else可以没有）
    代码
    pass

'''
score = int(input('请输入你的成绩：'))
if score < 60 and score >= 0:
    print("你不合格")
elif score >= 60 and score < 80:
    print("表现得还行")
elif score >= 80 and score <= 100:
    print("表现得很好")
else:
    print("分数输入错误")
