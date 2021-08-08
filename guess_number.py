# 猜數字遊戲練習

import random
print('猜數字遊戲')
lower_limit = input('請輸入下限： ')
lower_limit = int(lower_limit)
upper_limit = input('請輸入上限：')
upper_limit = int(upper_limit)

r = random.randint(lower_limit, upper_limit)
count = 0
while True:
	count = count + 1 # count += 1
	guess = input('猜到算你厲害： ')
	guess = int(guess)
	if guess == r:
		print('恭喜你猜對了！', '這是你猜的第', count, '次')
		break
	elif guess > r:
		print('比答案大')
	else :
		print('比答案小')
	print('這是你猜的第', count, '次')