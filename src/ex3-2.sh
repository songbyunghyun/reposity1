#!/bin/sh
read num1 i num2 
case "$i" in
	+)
		expr $num1 + $num2;; 
	-)
		expr $num1 - $num2;;
esac
exit 0
