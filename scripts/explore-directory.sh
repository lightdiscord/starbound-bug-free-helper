#!/usr/bin/env bash

if [ $# -ne 1 ]; then
    echo "$0: <directory>"
    exit 1
fi


find "$1" -name "*.world" -exec ./bugfree.py "{}" \; 2>/dev/null
