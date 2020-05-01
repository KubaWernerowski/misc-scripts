#!/bin/bash

# variables
DATE=$(date +%F)
IN_DIR='/Users/kuba/Downloads/'
BASE_DIR='/Users/kuba/Documents/photos/HEIC-originals/'
OUT_DIR=$BASE_DIR$DATE

mkdir -p $OUT_DIR

cd $IN_DIR

list=$(ls *.HEIC)
for img in $list
do 
    mogrify -format png -resize 75% $img
    mv $img $OUT_DIR
done

