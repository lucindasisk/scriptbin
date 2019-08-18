#! /bin/bash

fp=/Volumes/group/active/ELS/ELS-T3
log=~/Desktop/ELST3_DTIcount.txt

cd $fp
subs=$(ls)

for sub in $subs ; do
  if [ -e $fp/${sub}/DTI_2mm_b2000_60dir_raw.nii.gz ] ; then
    echo $sub 'has DTI' >> $log
  elif [ -e $fp/${sub}/DTI_2mm_b2000_60dir_raw.nii ] ; then
      echo $sub 'has DTI' >> $log
  else
    echo $sub 'missing DTI'
  fi
done
