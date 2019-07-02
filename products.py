products = []

while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':
		break
	price = input('請輸入商品價格： ')
	# p = []
	# p.append(name)
	# p.append(price)
	# p = [name, price]
	products.append([name, price])

print(products)


# 印出products內容
for p in products:
	print('------')
	print(p)


# p[0]為小清單中的第0項物品
# p[1]為小清單中的第1項物品
# 因為p代表的是小清單
for p in products:
	print(p[0], '的價格是', p[1], '元')