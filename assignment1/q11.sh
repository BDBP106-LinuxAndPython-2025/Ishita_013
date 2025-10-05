#n a directory, rename all files with extension .txt to have a prefix old_

#!/bin/bash
for f in *.txt;
do
    mv "$f" "old_$f"
done
