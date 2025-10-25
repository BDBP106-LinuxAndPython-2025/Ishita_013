# (2) How does Python know where to search for modules and packages?
# Python searches the following locations in order:
# - The current directory (where the script runs)
# - Directories in the PYTHONPATH environment variable
# - Standard library directories (site-packages)
# - Built-in module locations
# The search path can be found in sys.path
import sys
print(sys.path)
