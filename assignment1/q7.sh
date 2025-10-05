#A script that prints the current disk usage, and if the usage is above 80% print a warning message
#!/bin/bash


usage=$(df / | tail -1 | awk '{print $5}' | tr -d '%')
echo "Disk usage: $usage%"
if [ "$usage" -gt 80 ]; then
  echo "Warning: Disk usage above 80%"
fi
