#!/bin/sh

size=$1
color=$2
file_type=$3
output=$4


for file in *.svg; do
    case "$file_type" in
        png)
            rsvg-convert -a -w "$size" -f svg -o "$output/$file" $file
            sed -i "s/rgb(100%, 100%, 100%)/$color/g" "$output/$file"
            rsvg-convert -a -w "$size" -h "$size" -f png -o "$output/${file%.*}.png" "$output/$file"
            rm "$output/$file"
            echo "Converted $file"
            continue
            ;;
        *)
            ;;
    esac
    rsvg-convert -a -w "$size" -f svg -o "$output/$file" $file
    sed -i "s/rgb(100%, 100%, 100%)/$color/g" "$output/$file"
    echo "Converted $file"
done
mkdir -p "$output/symbolic"
for file in symbolic/*.svg; do
    case "$file_type" in
        png)
            rsvg-convert -a -w "$size" -h "$size" -f png -o "$output/${file%.*}.png" "$output/$file"
            rm "$output/$file"
            echo "Converted $file"
            continue
            ;;
        *)
            ;;
    esac
    rsvg-convert -a -w "$size" -f svg -o "$output/$file" $file
    echo "Converted $file"
done
