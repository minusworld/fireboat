#!/bin/bash

SERV=/dev/servoblaster
START=60
END=220

for (( c=$START; c<=$END; c++ ))
do
   echo $c > $SERV
done
