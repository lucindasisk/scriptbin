#! /bin/bash

sub=$1

datadir=/Volumes/iang/active/BABIES/BABIES_qT1/newproc
pe1=$datadir/$sub/${sub}_qt1_raw_pe1.nii.gz
pe0=$datadir/$sub/${sub}_qt1_raw_pe0.nii.gz
mask=$datadir/$sub/${sub}-binarized_mask.nii

pipenv run python t1fit_unwarp.py --tr 3000 --ti 50 --pe1 $pe1 $pe0 $datadir/$sub/

cd $datadir/$sub
if [ -e *t1fit_t1.nii.gz ] ; then
  echo 'T1fitter output exists, tarring extra files'
  mv *t1fit_t1.nii.gz ${sub}_qt1_T1fit_final.nii.gz
  tar -cvzf t1fit_other.tgz _*
  mkdir $datadir/delete
  mkdir $datadir/$sub/${sub}_delete
  mv _* $datadir/$sub/${sub}_delete
  mv $datadir/$sub/${sub}_delete $datadir/delete/
  echo 'Successfully completed' $sub
else
  echo 'Could not find T1fitter output for' $sub
fi
