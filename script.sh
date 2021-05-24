#!/bin/bash

a1=300
a2=310
b1=40
b2=50

dir_path=$(pwd)
:<<comment
start=`date +%s.%N`
psql -h 192.168.225.193 astrocat -U user -c "copy (SELECT ra, dec, w1, w2 FROM allwise WHERE q3c_poly_query(ra,dec,'(($a1,$b1), ($a1,$b2), ($a2,$b2), ($a2,$b1))'::polygon)) to stdout with csv header delimiter E'\t'" > allwise.$a1.$b1.$a2.$b2.1.csv
cat allwise.$a1.$b1.$a2.$b2.1.csv | tail -n +2 | LC_ALL=en_US.utf8   sort +1 -2 -g > allwise.$a1.$b1.$a2.$b2.csv

awk '{ 
    file="allwise_slice/allwise_"
    for(i=0;i<16;i+=1)
    {
        d1=i
        d2=i+3
        filename=file d1 "_" d2
        if($3<d2 && $3>d1) 
            {print $0 > filename}
    }
    }' allwise.$a1.$b1.$a2.$b2.csv 

cd allwise_slice
for i in $(ls)
do
../qcross_density_dr5 $i 1 2 5 10 20 30 60 2000000 8 | sed 's!\t!,!g' > $i.csv
rm $i
done
load=`date +%s.%N`
echo "load"
echo "$load - $start" | bc -l
comment
cd allwise_slice
iteration=1
#dir_path=$(pwd)
for i in $(ls)
do
load=`date +%s.%N`
mkdir $dir_path/allwise_slice_pic/$iteration
echo "$i"
../main.py $i $dir_path/allwise_slice_pic/$iteration/0_$i 0
end1=`date +%s.%N`
echo "col 0"
echo "$end1 - $load" | bc -l
../main.py $i $dir_path/allwise_slice_pic/$iteration/7_$i 7
end2=`date +%s.%N`
echo "col 7"
echo "$end2 - $end1" | bc -l
iteration=$[iteration+1]
done

cd ..







#filename=$1
#a1=$2
#b1=$3
#a2=$4
#b2=$5
#d1=$6
#d2=$7
#awk '{if('$a1'<$1 && '$a2'>$1 && '$b1'<$2 && '$b2'>$2) {print $0}}' filename > filename_$a1_$a2.csv
#./qcross_big_data flag=1 filename_$a1_$a2.csv > filename_$b1_$b2.csv
#awk '{ if($?<'$d2' && $?>'$d1') {print $0}}' filename_$b1_$b2.csv > filename_$d1_$d2.csv
#./qcross_dencity filename_$d1_$d2.csv
