#!/bin/bash/rs

if [[ $@ ]];
then
  cd ./rs/
  rustc src/$@.rs
  # echo 'enter file_name for run'
  # read file_name;
  ./$@
  echo ''
  echo 'Done rs_build_bin.sh'
else
  echo 'run - rs_build_bin.sh file_name'
fi