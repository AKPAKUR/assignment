#!/bin/bash

# Install Miniconda (change the URL if needed)
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
bash miniconda.sh -b -p $HOME/miniconda
rm miniconda.sh

# Initialize Conda
eval "$($HOME/miniconda/bin/conda shell.bash hook)"
conda init

# Create a new Conda environment
conda create --name assignment python=3.9

# Activate the environment
conda activate assignment

# Install required packages
conda install ./requirement.txt

## To deactivate - This is not needed when you kill the shell, the Conda env with be deactivated
#conda deactivate

echo "Setup complete. Activate the environment with 'conda activate assignment'."
