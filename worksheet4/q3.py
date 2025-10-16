#!/usr/bin/python3
#Filter protein names starting with 'H' or has 'ase'

print("The name of the protein entered are:")
proteins=["Hexokinase", "Amylase","Hemoglobin", "Catalase", "Actin"]
print(proteins)

names_prot = [pro for pro in proteins if pro.startswith("H") or "ase" in pro]
print("Proteins staring with H or having ase in them :" , names_prot)