loops=0

while :; do
  ls -R /
  loops+=1
  echo $loops >>~/Documents/rootListLoops.txt
done
