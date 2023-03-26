# 1. adım: Girilen şifrenin çözülme adım sayısını bulan fonksiyon
import itertools
import random


abc = list(itertools.product(["0", "1","2","3","4","5","6","7","8","9"], repeat = 6))

def password_checker(try_passw):

	count = 0
	for i in abc:

		if list(i) == try_passw:
			#print(i)
			break
		count += 1

	return count

while True:
	test = random.choice(abc)
	if password_checker(test) > 800000:
		print(test)
