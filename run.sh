#!/bin/bash
module load anaconda/2021.05

source activate mmcls2

export PYTHONUNBUFFERED=1

# run
python tools/train.py \
    configs/resnet/resnet18_b16_garbage.py \
    --work-dir work_dirs/garbage