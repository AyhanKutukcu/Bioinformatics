# -*- coding: utf-8 -*-
from rna_codons import RNA_Codons
a = "GUGCCAAUAGGAUCUACCGGGAUA"
dna_dizisi_liste = []


for i in a:
    dna_dizisi_liste.append(i)
    
    
dna_dizisi_üçlü_string = ''    

count = len(dna_dizisi_liste)
count_2 = 0

while count > 0 :
   dna_dizisi_üçlü_string += dna_dizisi_liste[count_2]
   count_2 += 1
   
   if (count_2 % 3 == 0):
       print(RNA_Codons[dna_dizisi_üçlü_string])
       dna_dizisi_üçlü_string = ''
   count -= 1
   

