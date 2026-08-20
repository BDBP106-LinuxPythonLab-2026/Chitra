#!/bin/bash
ls
ls > listoffiles
ls 1> listoffiles
ls -l . newdir
ls -l . newdir 1>presentfiles 2>filesnotpresent
ls -l . newdir >listoffiles
