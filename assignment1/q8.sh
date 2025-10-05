# script that prints a mini-system report that includes a) current date and time, b)logged-in users, c) system uptime and d) top 5 processes by memory usage
#!/bin/bash


echo "Date and time: $(date)"
echo "Logged in users:"
who
echo "System uptime: $(uptime -p)"
echo "Top 5 memory usage processes:"
top -o %MEM | head -n 6
