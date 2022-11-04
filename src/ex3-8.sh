#!/bin/sh
if ! test -d DB.txt ;then
    touch DB.txt
fi
read string
echo $string >> DB.txt
exit 0
