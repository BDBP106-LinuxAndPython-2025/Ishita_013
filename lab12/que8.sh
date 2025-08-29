#!/bin/bash
# ls 1>listoffiles- Redirects STDOUT (normal output) to listoffiles. Errors (if any) show on terminal.

#ls 1>presentfiles 2>filesnotpresent   Redirects STDOUT (present files) to presentfiles, and STDERR (errors/missing files) to filesnotpresent.


ls -l newdir          # Lists newdir or errors if missing
ls -l newdir 1>presentfiles 2>filesnotpresent


