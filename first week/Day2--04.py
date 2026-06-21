print(716+88)
print(716**2+88**2)
print(716*88)
print(716/2)
print((716%5)+88/4+2**2-(515//3))


a = 10
b = 3
a += b       
a *= a + 2    
print(a)  
print(a:=100)
print(a)


age = 18
height = 145
has_health_problem = False

height_ok = height >= 140
age_ok = age >= 12 and age <= 60
health_ok = not has_health_problem

can_ride = height_ok and age_ok and health_ok

print("身高合格：", height_ok)
print("年龄合格：", age_ok)
print("健康合格：", health_ok)
print("可以乘坐：", can_ride)

length = float(input("请输入长："))
width = float(input("请输入宽："))

area = length * width
perimeter = 2 * (length + width)
is_large = area > 100
print(f"面积：{area:.2f}")
print(f"周长：{perimeter:.2f}")
print(f"面积是否大于100：{is_large}")

