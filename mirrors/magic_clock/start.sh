#!/usr/bin/env bash

MM="$HOME/MM_magic_clock"

if [[ $# -eq 0 ]] ; then
    DISPLAY=:0 npm start --prefix ${MM}
else
    if [[ $1 = "--no-display" ]] ; then
        cd ${MM}
        node serveronly
        exit 1
    fi
fi