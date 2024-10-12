#!/bin/sh

size=$1
color=$2
file_type=$3
output=$4

for file in *.svg; do
    rsvg-convert -a -w "$size" -f "$file_type" -o "$output/$file" $file
    sed -i "s/rgb(100%, 100%, 100%)/$color/g" "$output/$file"
    echo "Converted $file"
done
