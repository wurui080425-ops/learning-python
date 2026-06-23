#寻找回文数
n= int(input("请输入一个大于10的正整数："))

count = 0
total = 0

for num in range(10, n + 1):
    temp = num
    reversed_num = 0

    while temp > 0:
        last_digit = temp % 10
        reversed_num = reversed_num * 10 + last_digit
        temp //= 10

    if num == reversed_num:
        print(num)
        count += 1
        total += num    
    
print(f"回文数的个数为：{count}")
print(f"回文数的总和为：{total}")
