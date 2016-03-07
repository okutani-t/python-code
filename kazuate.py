# -*- coding: utf-8 -*-

import random

i = random.randint(1,50)
n = 0
count = 5
#答えnとユーザの入力した値iが間違っている間ループ
while n != i :
	print"あと"+ str(count) + "回遊べるよ"
	count -= 1
	n = input("Please Input Number 1-50:")
	if count ==0 and n != i:
		break
	if n>i:
		if n==i+1:
			print"おしい！もう少し小さい数！"
		else:
			print"もっと小さい数だよ！"
	elif n<i:
		if n==i-1:
			print"おしい！もう少し大きい数！"
		else:
			print"もっと大きい数だよ！"
	else:
		pass

if count==0 and n != i	:
	print"※※※※※残念！正解は"+ str(i) + "でした！※※※※※"
else:
	print"※※※※※正解！"+ str(i) + "だったよ※※※※※"