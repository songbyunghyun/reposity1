#!/bin/sh
echo "리눅스가 재밌습니까?(yes/no)"
read answer
case $answer in
	yes|y|Y|YES)
		echo "yes";;
	NO|n|N|no)
		echo "no";;
	*)
		echo "yes or no로 입력";; 
esac
exit 0
