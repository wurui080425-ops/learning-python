for row in range(1, 4):
    for column in range(1, 3):
        print(row, column)
    
for i in range(1, 11):
    print(i)

n = int(input("请输入正整数："))
total = 0
for i in range(1, n + 1):
    total += i
print(f"1到{n}的和为：{total}")


n = int(input("请输入正整数："))
total = 0

for i in range(0, n+1):
    if i % 3== 0:
        print(i)
        total += i

print(f"总和：{total}")