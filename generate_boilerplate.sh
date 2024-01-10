#!/bin/bash
if ! mkdir day${1}; then
    exit 1
fi
cd day${1}
touch input.txt
touch testinput.txt
touch output.txt
cp ../boilerplate.py ./part1.py
cp ../boilerplate.py ./part2.py