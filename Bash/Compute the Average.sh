read n
sum=0
i=0

while [ "$i" -lt "$n" ]; do
    read x
    sum=$((sum + x))
    i=$((i + 1))
done

printf "%.3f\n" "$(echo "$sum / $n" | bc -l)"
