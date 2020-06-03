#建造一个空列表
products = []
#输出商品的名字和价格
while True:
	name = input('请输入商品名称：')
	if name == 'q':
		break
	price = input('请输入商品价格：')
	#输出的所有东西都放进空列表
	products.append([name,price])
	#形成一个大列表中有好几个小列表
print(products)
#印出对应的名字和价格
for p in products:
    print(p[0],'的价格是',p[1])
#把所有数据都放进一个cvs
with open('products.txt','w') as f:
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')
