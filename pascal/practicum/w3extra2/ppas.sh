#!/bin/sh
DoExitAsm ()
{ echo "An error occurred while assembling $1"; exit 1; }
DoExitLink ()
{ echo "An error occurred while linking $1"; exit 1; }
echo Linking extra-2
OFS=$IFS
IFS="
"
/usr/bin/ld -b elf32-i386 -m elf_i386     -s  -L. -o extra-2 -T link13947.res -e _start
if [ $? != 0 ]; then DoExitLink extra-2; fi
IFS=$OFS
