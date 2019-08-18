#! /bin/bash

home=/Volumes/group/active/ELS/ELS-T1
dest=/Volumes/iang/ELS_data/ELS_DTI_Analysis/ELS_T1/matproc
list=/Volumes/iang/ELS_data/ELS_DTI_Analysis/ELS_T1/config/txtfiles/NewT1subs_4.16.19.txt

cd $home
subs=$(ls)

for sub in $subs ; do
  subname=els${sub}
  if [ -e $home/$sub/DTI_2mm_b2000_60dir_raw.ni* ] ; then
    if [ -e $dest/els${sub}/${subname}_t1.nii.gz ] ; then
      :
    else
      echo 'Making a folder for' $sub
      mkdir $dest/${subname}
      mkdir $dest/${subname}/raw
      cp $home/${sub}/*.bval $dest/${subname}/raw/$subname'.bval'
      cp $home/${sub}/*.bvec $dest/${subname}/raw/$subname'.bvec'
      cp $home/${sub}/DTI_2mm_b2000_60dir_raw.ni* $dest/${subname}/raw/$subname'.nii.gz'
      cp $home/${sub}/T1w_9mm_sag_raw.nii.gz $dest/${subname}/$subname'_t1.nii.gz'
      #echo $subname >> $list
    fi
  else
    :
  fi
done
