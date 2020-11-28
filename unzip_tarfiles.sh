#!/bin/bash

#SBATCH --job-name=unzip_imputed
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --cpus-per-task=10
#SBATCH --mem-per-cpu=10G
#SBATCH --time=80:00:00
#SBATCH --partition=verylong
#SBATCH --mail-type=ALL
#SBATCH --mail-user=lucinda.sisk@yale.edu

path='/gpfs/milgram/scratch60/gee_dylan/lms233/imputed'

cd $path
gzip -d *.gz
