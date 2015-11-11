#!/bin/bash

SERV=/dev/servoblaster
START=60
END=220

for (( c=$START; c<=$END; c++ ))
do
	echo 0=$c > $SERV
	echo 1=$c > $SERV
done

# Aaaand back

for (( i=$END; i <=$START; i-- ))
do
        echo 0=$c > $SERV
        echo 1=$c > $SERV
done
