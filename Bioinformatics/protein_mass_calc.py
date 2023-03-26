# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 16:07:10 2022

@author: mitra
"""
from prot_mass_table import mass_table

a = "SKADYEK"

protein_list = []

for i in a:
    protein_list.append(i)
    
mass_sum = 0
count = 0

while count < len(protein_list):
    mass_sum = mass_sum + mass_table[protein_list[count]]
    count += 1
print("Result = ", round(mass_sum, 3))
