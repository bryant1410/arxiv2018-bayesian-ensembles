#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -J pico_al_gpu
#SBATCH --mail-user=
#SBATCH --mail-type=FAIL
#SBATCH -e ./pico_al_gpu.err.%j
#SBATCH -o ./pico_al_gpu.out.%j
#SBATCH -n 1
#SBATCH -c 16
#SBATCH --mem-per-cpu=8182
#SBATCH --exclusive

# ----------------------------------


module load intel cuda gcc python/3.5.2 blas OpenBLAS/gcc/avx OpenBLAS/gcc/sse OpenBLAS/intel/avx/0.2.2

cudaDir="/home/ih68sexe/cudnn/cuda"
export LD_LIBRARY_PATH=${cudaDir}/lib64:${LD_LIBRARY_PATH}
export CPATH=${cudaDir}/include:${CPATH}
export LIBRARY_PATH=${cudaDir}/lib64:${LD_LIBRARY_PATH}

THEANO_FLAGS=mode=FAST_RUN,device=cuda*,floatX=float32,optimizer_including=cudnn python3 run_pico_active_learning.py
