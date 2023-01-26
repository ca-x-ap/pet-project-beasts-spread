#!/bin/bash

# echo 'using\n> rs_build_bin.sh file_name'
rustc src/$@.rs
# echo 'enter file_name for run'
# read file_name;
./$@

echo ''
echo 'Done rs_build_bin.sh'