#Display a menu with options: 1) Show date, 2) Show calendar, 3) show logged-in users,4) Exit. The script should display these options, execute the appropriate command according to the option.


#!/bin/bash
while true; do
    echo "1) Show date"
    echo "2) Show calendar"
    echo "3) Show logged-in users"
    echo "4) Exit"
    read -p "Choose an option: " choice
    case $choice in
        1) date ;; 
        2) cal ;; 
        3) who ;; 
        4) break ;; 
        *) echo "Invalid option";;
    esac
done

