#!/usr/bin/env bash

find -type f -name 00*.py > badmigs.txt
xargs rm < badmigs.txt
rm badmigs.txt
