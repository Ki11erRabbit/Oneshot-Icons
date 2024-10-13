#!/bin/sh

size=$1
output=$2


for file in *.svg; do
    rsvg-convert -a -w "$size" -f svg -o "$output/$file" $file
    rsvg-convert -a -w "$size" -h "$size" -f png -o "$output/${file%.*}.png" "$output/$file"
    rm "$output/$file"
    echo "Converted $file"
    echo "$size 0 0 $output/${file%.*}.png 1000" > "$output/${file%.*}.in"
done

