scores = [85, 92, 76, 88]
total = 0

for score in scores:
    total += score

average = total / len(scores)

print(f"总分：{total}")
print(f"平均分：{average:.1f}")

#append(x)	在末尾添加 x
#insert(i, x)	在索引 i 插入 x
# remove(x)	删除第一个 x
#pop(i)	删除并返回索引 i 的元素
#index(x)	查找第一个 x 的索引
#count(x)	统计 x 出现次数
#sort()	对元素排序
#reverse()	反转当前顺序


scores = [78, 92, 65, 88, 92]

# 添加一个成绩
scores.append(85)
print("添加后：", scores)

# 在开头插入一个成绩
scores.insert(0, 90)
print("插入后：", scores)

# 删除成绩65
if 65 in scores:
    scores.remove(65)
print("删除65后：", scores)

# 删除并保存最后一个成绩
deleted_score = scores.pop()
print("被删除的成绩：", deleted_score)
print("删除最后一个后：", scores)

# 查找92第一次出现的位置
position = scores.index(92)
print("92第一次出现的索引：", position)

# 统计92出现的次数
frequency = scores.count(92)
print("92出现的次数：", frequency)

# 从高到低排序
scores.sort(reverse=True)
print("从高到低排序：", scores)

# 创建只包含80分及以上成绩的新列表
good_scores = [score for score in scores if score >= 80]
print("80分及以上：", good_scores)
