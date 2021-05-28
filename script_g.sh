#!/bin/bash

dir_path=$(pwd)
:<<dencity
cd gauss/data_sort/
for i in $(ls)
do
sed 's!,!\t!g' $i > $i.txt
$dir_path/qcross_density_dr5 $i.txt 1 2 5 10 20 30 60 200000 8 | sed 's!\t!,!g' > $dir_path/gauss/data_dencity/$i.csv
rm $i.txt
done
cd -
dencity
#mkdir gauss/data_pic
cd gauss/data_dencity/
for i in $(ls)
do
#mkdir $dir_path/gauss/data_pic/$i
echo "$i"
$dir_path/main.py $i $dir_path/gauss/data_pic/$i/0_$i 0
$dir_path/main.py $i $dir_path/gauss/data_pic/$i/7_$i 7

done