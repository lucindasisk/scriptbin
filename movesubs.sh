#! /bin/bash

fp=/Users/lucindasisk/Dropbox/Projects/MS_Hippocampal_MRS/HippoMRSProject
gopath=/Users/lucindasisk/Box_Sync/Manpreet_MRS
ss=/Users/lucindasisk/Dropbox/Projects/MS_Hippocampal_MRS/LS_MRS_Hipp_Processing/Subj_MRSHipp_Coords

cd $gopath
subs=$(ls)

for sub in $subs; do
  if [ -e $gopath/$sub ] ; then
    cp $fp/RO1-Segmentation/$sub/*nii $gopath/$sub/.
    cp -vr $fp/RO1-Segmentation/$sub/*3T $gopath/$sub/.
    cp $ss/$sub/*tiff $gopath/$sub/.
  else
    echo 'folder not found for' $sub
  fi
done
