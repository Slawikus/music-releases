#!/usr/bin/env bash

touch dublicate_files.txt
find -type f -name example_*.jpg > dublicate_files.txt
find -type f -name dummy_*.jpg > dublicate_files.txt

xargs rm < dublicate_files.txt
rm dublicate_files.txt
