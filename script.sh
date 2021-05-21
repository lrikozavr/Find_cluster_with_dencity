#!/bin/bash

a1=310
a2=320
b1=40
b2=50



d1=14
d2=16
start=`date +%s.%N`
#psql -h 192.168.225.193 astrocat -U user -c "copy (SELECT ra, dec, w1, w2 FROM allwise WHERE q3c_poly_query(ra,dec,'(($a1,$b1), ($a1,$b2), ($a2,$b2), ($a2,$b1))'::polygon)) to stdout with csv header delimiter E'\t'" > allwise.$a1.$b1.$a2.$b2.1.csv
#cat allwise.$a1.$b1.$a2.$b2.1.csv | tail -n +2 | LC_ALL=en_US.utf8   sort +1 -2 -g > allwise.$a1.$b1.$a2.$b2.csv
#awk '{ if($3<'$d2' && $3>'$d1') {print $0}}' allwise.$a1.$b1.$a2.$b2.csv > allwise.csv
#./qcross_density_dr5 allwise.csv 1 2 5 10 20 30 60 2000000 8 | sed 's!\t!,!g' > allwise_den.csv
load=`date +%s.%N`
./main.py allwise_den.csv /home/kiril/github/Find_cluster_with_dencity/allwise_0/ 0
end1=`date +%s.%N`
./main.py allwise_den.csv /home/kiril/github/Find_cluster_with_dencity/allwise_60/ 7
end2=`date +%s.%N`


echo "load"
echo "$load - $start" | bc -l
echo "col 0"
echo "$end1 - $load" | bc -l
echo "col 7"
echo "$end2 - $end1" | bc -l








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
