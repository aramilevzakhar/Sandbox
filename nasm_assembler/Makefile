#!/bin/bash
all:
		nasm –f elf $(source)
		ld –m elf_i386 –s –o build $(source).o
# 		rm $(source).o 
