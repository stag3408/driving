country = input('請輸入國家: ')
age = input('請輸入年齡: ')
age = int(age)

if country == '台灣':
	if age >= 18:
		print('你可以開車')
	else:
		print('你不能開車')
elif country == '美國':
	if age >= 16:
		print('你可以開車')
	else:
		print('你不能開車')
else:
	print('你只能輸入台灣或美國')