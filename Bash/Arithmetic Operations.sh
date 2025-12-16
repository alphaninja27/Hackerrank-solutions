read expr
printf "%.3f\n" "$(echo "$expr" | bc -l)"
