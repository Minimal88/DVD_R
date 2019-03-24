#cat top.dat | egrep '^[0-9]+' > cpu.txt | awk -v now=$(date +%s) '{print now,$6,$9}'

cat top.dat | egrep '^[0-9]+' | awk -v now=$(date +%s) '{print now,$6,$9}' > cpu.dat
#cat top.dat | egrep '^[0-9]+' > cpu.txt

#top -p 10506 -b -d 1 | egrep '^[0-9]+' > cpu.txt | awk -v now=$(date +%s) '{print now,$6,$9}'
