#! /bin/bash

fp=/Users/myelin/Desktop/Box_Sync/Manpreet_MRS

cd $fp
subs=$(ls)

for sub in $subs ; do
	fldr=$fp/$sub
	cd $fldr
	if [ -e $fldr/SPGR ] ; then
		if [ -e $fldr/t1w.nii ] ; then
			if [ -e $fldr/t1w_reorient.nii.gz ] ; then
				if [ -e $fldr/t1w_reorient_bet_seg.nii.gz ] ; then
					echo 'Segmentation done for' $sub
				else
					echo 'Working on' $sub
					bet t1w_reorient.nii.gz t1w_reorient_bet.nii.gz -m
					fast -s 2 t1w_reorient_bet.nii.gz
					echo 'Finished' $sub
				fi
			else
				fslreorient2std t1w.nii t1w_reorient.nii
			fi
		else
			cd $fldr/SPGR
			to3d -prefix t1w *.dcm
			3dAFNItoNIFTI t1w+*
			fslreorient2std t1w.nii t1w_reorient.nii
			mv *.nii *BRIK *.HEAD *nii.gz $fldr
			cd $fldr
			tar -cvzf SPGR_dcm.tgz SPGR/
		fi
	else
		echo 'Could not find SPGR'
	fi
done
