scores = [78, 92, 65, 88, 92, 55, 80]

# 1
print("成绩列表：", scores)

# 2
print("学生人数：", len(scores))

# 3
print("第一个成绩：", scores[0])
print("最后一个成绩：", scores[-1])

# 4
print("前三个成绩：", scores[:3])

# 5
scores.append(86)
print("添加86后：", scores)

# 6
scores.insert(1, 90)
print("插入90后：", scores)

# 7
if 55 in scores:
    scores.remove(55)
print("删除55后：", scores)

# 8
last_score = scores.pop()
print("被删除的成绩：", last_score)
print("删除后列表：", scores)

# 9
print("92第一次出现的索引：", scores.index(92))

# 10
print("92出现的次数：", scores.count(92))

# 11
pass_scores = [score for score in scores if score >= 60]
print("及格成绩：", pass_scores)

# 12
scores.sort(reverse=True)
print("降序排序：", scores)

# 13
print("逐个输出成绩：")
for score in scores:
    print(score)

# 14
print("最高分：", max(scores))
print("最低分：", min(scores))
print("总分：", sum(scores))
print("平均分：", sum(scores) / len(scores))