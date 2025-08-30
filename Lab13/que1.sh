#!/bin/bash


sed -n '/and/p' Lab13pract.txt
#This command prints only those lines in Lab13pract.txt that contain the word 'and'. The -n suppresses default output, while /and/p matches lines with 'and' and prints them.


sed 's/language/lang/g' Lab13pract.txt
#This substitutes every occurrence of the word 'language' with 'lang'. The -g means "global" throughout each line.

sed '/is/d' Lab13pract.txt
#This removes from all lines containing 'is' from the output.

nl Lab13pract.txt
#The nl command ("number lines") adds line numbers to every line, separated by tabs by default.


sed '=' Lab13pract.txt | sed 'N;s/\n/ /'
#This prints a line number, then the line, for each line.


sed '1,2d' Lab13pract.txt
#This deletes lines 1 and 2 from the output.

sed -n 'p;n' Lab13pract.txt
#This prints every alternate line.

sed 's/Python/python/;s/language/lang/' Lab13pract.txt
#Both substitutions are done on each line that is only the first occurrence per line
