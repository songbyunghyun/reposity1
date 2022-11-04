#!/bin/sh

showinfo(){
        ls $1
}

echo "프로그램으로 들어왔습니다"

echo "함수 안으로 들어왔습니다"

read input

showinfo $input

echo "종료"

exit 0
