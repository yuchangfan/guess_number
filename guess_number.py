# 猜數字遊戲練習

import random
r = random.randint(1, 100)
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