#!/bin/sh
myFunction(){
    ls
    if ! test -d $1 ;then
        mkdir $1
    fi
    cd $1
    for i in 0 1 2 3 4
    do
        mkdir file$i
        touch file$i.txt
    done
for i in 0 1 2 3 4
do
  location="file$i.txt"
  todir="file$i/$location"
  ln -Tfs $location $todir
done
}
read name
myFunction $name
