#!/bin/sh
myFunction(){
    ls
    if ! test -d $1 ;then
        mkdir $1
    fi
    cd $1
    for i in 0 1 2 3 4
    do
        touch file$i.txt
    done
    ls
    tar -cvf $1.tar *
    mkdir $1
    mv $1.tar $1
    ls
    cd $1
    tar -xvf $1.tar
    }
read n
myFunction $n
exit 0
