price = float(input("请输入商品总价："))
if price >= 500:
    final_price = price * 0.8
    discount = "8折"
elif price >= 200:
    final_price = price *0.9
    discount = "9折"
else:
    final_price = price
    discount = "不打折"
print(f"原价:{price:.2f}元")
print(f"折扣：{discount}")
print(f"实际付款：{final_price:.2f}元")