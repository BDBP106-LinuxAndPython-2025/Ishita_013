#!/bin/bash

gawk '!/^>/' fasta.txt
#!/^>/ matches lines that do not start with >.This command prints only sequence lines.

sed 's/T/U/g' fasta.txt
#This converts the DNA sequences to RNA by converting all the T to U 

sed 's/seq1/human_gene/g' fasta.txt
#Replaces every instance of seq1 with human_gene, including in headers.


