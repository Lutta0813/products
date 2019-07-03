import os

products = []

# 確認檔案是否存在
if os.path.isfile('products.csv'):
	print('Data existed')
	# 讀取檔案
	with open('products.csv', 'r', encoding = 'utf-16') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])

	print(products)
else:
	print('Data does not exist, Please build a new File')

# 讓使用者輸入

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


#寫入所有購買紀錄
with open('products.csv', 'w', encoding = 'utf-16') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')