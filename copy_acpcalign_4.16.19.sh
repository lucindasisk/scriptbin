#! /bin/bash

home=/Volumes/iang/ELS_data/ELS-T1
dest=/Volumes/iang/ELS_data/ELS_DTI_Analysis/ELS_T1/matproc
list=/Volumes/iang/ELS_data/ELS_DTI_Analysis/ELS_T1/config/txtfiles/NewT1subs_4.16.19.txt

cd $home
subs=$(ls)

for sub in $subs ; do
  subname=els${sub}
  if [ -e $home/$sub/T1w_9mm_sag_raw_acpc.nii.gz ] ; then
    if [ -e $dest/els${sub}/${subname}_t1_acpc.nii.gz ] ; then
      :
    else
      echo 'Copying ACPC file for' $sub
      cp $home/$sub/T1w_9mm_sag_raw_acpc.nii.gz $dest/els${sub}/${subname}_t1_acpc.nii.gz
      #echo $subname >> $list
    fi
  else
    :
  fi
done
