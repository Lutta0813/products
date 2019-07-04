import os

def read_file(filename):
	products = []
	# 讀取檔案
	with open(filename, 'r', encoding = 'utf-16') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

# 讓使用者輸入
def user_input(products):
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
	return products


# 印出products內容
# --------------------
# for p in products:
# 	print('------')
# 	print(p)

# p[0]為小清單中的第0項物品
# p[1]為小清單中的第1項物品
# 因為p代表的是小清單
# --------------------
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1], '元')


#寫入所有購買紀錄
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-16') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

def main(filename):
	if os.path.isfile(filename):
		products = read_file(filename)
		print('Data existed')
		print(products)
	else:
		print('Data does not exist, Please build a new File')
	products = user_input(products)
	print_products(products)
	write_file(filename, products)


main('products.csv')










