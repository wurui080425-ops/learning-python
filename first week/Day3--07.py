#水仙花数
for num in range(100, 1000):
    hundreds = num // 100
    tens = num // 10 % 10
    ones = num % 10

    total = hundreds ** 3 + tens ** 3 + ones ** 3

    if total == num:
        print(num)
#反转整数
num = int(input("请输入正整数："))
reversed_num = 0

while num > 0:
    last_digit = num % 10
    reversed_num = reversed_num * 10 + last_digit
    num //= 10

print(f"反转后的数字：{reversed_num}")      

#穷举法

for x in range(0, 11):
    for y in range(0,11 ):
        if x+y==10 and x>y:
            print(x, y)

#斐波那契数列
a = 0
b = 1

for _ in range(10):
    a, b = b, a + b
    print(a)

#判断素数
num = int(input("请输入大于1的整数："))
is_prime = True

for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

if is_prime:
    print(f"{num}是素数")
else:
    print(f"{num}不是素数")