number = int(input("请输入整数："))
if number % 2 == 0:
    print(f"{number} 是偶数")
else:    print(f"{number} 是奇数")

grade = int(input("请输入成绩："))
if grade >= 90:
    print("成绩优秀")
elif grade >= 80:
    print("成绩良好")
elif grade >= 60:
    print("成绩及格")
else:    print("成绩不及格")    