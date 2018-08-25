#! /bin/bash

base=/Volumes/iang/active/BABIES
chome=$base/BABIES_Crossectional/BABIES_Crossectional-T1
l2home=$base/BABIES_Longitudinal/BABIES_Longitudinal-T2
l3home=$base/BABIES_Longitudinal/BABIES_Longitudinal-T3
mama=$base/BABIES_MAMA

home=$mama

cd $home
subs=$(ls)

for sub in $subs ; do
  if [ -e $home/$sub.tgz ] ; then
    echo 'Tgz already exists for '$sub
  else
    tar -cvzf $home/$sub.tgz $home/$sub
  fi
done
