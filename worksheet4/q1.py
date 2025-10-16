#!/usr/bin/python3
#a list comprehension to extract all even gene lengths from a list of genes.
#For example, gene_lengths=[450,300,725,1024,512,815].

print("All the gene lengths entered are: ")
gene_lengths = [450, 300, 725, 1024, 512, 815]
print(gene_lengths)

#list comprehension for even gene lengths
even_gene = [len for len in gene_lengths if len % 2 == 0]
print("All gene lengths wiht even value are:" , even_gene)
