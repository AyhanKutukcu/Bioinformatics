import random

cift_1 = ["A", "T"]
cift_2 = ["G", "C"]
count = 0
sign = 0

count2 = 0
sign2 = 0
for j in range(100000):

	for i in range(random.randint(1, 10000)):
		if i == random.randint(1, 10000):
			
			print(" "*(10-count),cift_1[i % 2], "="*count,"="*count, cift_1[i % 2 - 1])

			if count >= 10:
				sign = 1
			elif count == 1: 
				sign = 0

			if sign == 0:
				count += 1
			else:
				count -= 1	
			#------------------
			if count2 < 0:
				sign2 = 1
			elif count2 == 10: 
				sign2 = 0

			if sign2 == 0:
				count2 += 1
			else:
				count2 -= 1	

		if i == random.randint(1,10000):
			print(" "*(10-count),cift_2[i % 2], "="*count,"="*count , cift_2[i % 2 - 1])
			
			if count >= 10:
				sign = 1
			elif count == 1: 
				sign = 0

			if sign == 0:
				count += 1
			else:
				count -= 1	
			#------------------
			if count2 < 0:
				sign2 = 1
			elif count2 == 10: 
				sign2 = 0

			if sign2 == 0:
				count2 += 1
			else:
				count2 -= 1	