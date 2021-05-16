#!/bin/bash

lex icg_quad.l
yacc mychange.y
gcc y.tab.c -ll -w
./a.out
