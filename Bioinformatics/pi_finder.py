"""
def fact(num):
	result = 1
	for i in range(2, num + 1):

		result *= i

	return result

def pow(taban, üs):

	result = 1

	for i in range(üs):
		result *= taban

	return result
"""

"""
n = int(input("Bir sayı giriniz: "))

result = 0

for i in range(n):

	result += (pow(2, i + 1)) * (pow(fact(i), 2)) / (fact(2 * i + 1))

print(result)
"""
"""

def fact_rec(num):

	if num == 1:
		return num

	return num * fact_rec(num - 1)


while 1:
	print(fact(int(input())))
"""

import math


yogusma_sicakligi = 115.6#float(input("Yoğuşma sıcaklığı giriniz: "))

kazanin_ic_capi = .656#float(input("Kazanın iç çapını giriniz: "))

kazanin_yuksekligi = .984#float(input("Kazanın yüksekliğini giriniz: "))

# Taban kavislidir ama düz kabul edilecektir.
# Taban ve yanlar da mantolanmıştır.

mantolama_yuksekligi = .656#float(input("Mantolama yüksekliğini giriniz: "))

# Kazan yüzeyi pasalanmaz çeliktir.
kazan_yuzeyi = 3.2#float(input("Kazan yüzeyi kalınlığını giriniz:"))

kazan_yuzeyi_isi_iletim_sayisi = 16.27#float(input("Kazan yüzeyi ısı iletim sayısı((W / m) * k): "))

ceketin_icindeki_yogusma_katsayisi = 10200.0#float(input("Ceketin içindeki yoğuşma katsayısı: "))

control = .0 		# While döngüsüne girmesi için doğru bir başlangıç değeri atadım.

tw2 = .0

h0degeri = 0.0

tw = 95.0

iteration_num = 0

while tw <= 115:

	tsat = 100.0

	if tw == 100:

		tw = 100.1

	deltaT = tw - tsat

	ho = 5.56 * (math.pow(deltaT, 3))

	# A 1m^2 kabul edilmiştir.

	ri = 1 / (ceketin_icindeki_yogusma_katsayisi * 1) # (hi)

	rw = (kazan_yuzeyi / 1000) / (kazan_yuzeyi_isi_iletim_sayisi * 1) # mm to m

	ro = 1.0 / (ho * 1.0)

	rToplam = ri + rw + ro

	deltaT2 = (ro / rToplam) * (yogusma_sicakligi - tsat)

	tw2 = deltaT2 + tsat

	control = tw2 - tw

	if (control <= 0.01 and control >= -0.01):


		break

	tw += 0.1

	iteration_num += 1
print("En yakın Tw = ", tw2)
print("h0degeri = ", ho)
print("R0 = ", ro)
print("Iter num = ", iteration_num)



