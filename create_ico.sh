#!/bin/bash

#This script uses convert from ImageMagic and the nice bash expension

for letter in {A..Z}; 
  do
    convert -adjoin letter/eclipse_16_$letter.png letter/eclipse_32_$letter.png letter/eclipse_256_$letter.png letter/eclipse_48_$letter.png icos/eclipse_$letter.ico ;
done
