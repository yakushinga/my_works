#!/bin/sh
DoExitAsm ()
{ echo "An error occurred while assembling $1"; exit 1; }
DoExitLink ()
{ echo "An error occurred while linking $1"; exit 1; }
echo Linking z8_32
OFS=$IFS
IFS="
"
/usr/bin/ld -b elf32-i386 -m elf_i386     -s  -L. -o z8_32 -T link181909.res -e _start
if [ $? != 0 ]; then DoExitLink z8_32; fi
IFS=$OFS
