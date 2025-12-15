#!/usr/bin/env bash
read ch
ch=${ch:0:1}

if [[ "$ch" == [Yy] ]]; then
    echo "YES"
else
    echo "NO"
fi
