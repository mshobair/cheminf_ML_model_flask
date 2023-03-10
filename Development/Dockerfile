#FROM python:3.6.7
# Define base image
FROM continuumio/miniconda3
 
# Set working directory for the project
WORKDIR usr/src/flask_app

 
# Create Conda environment from the YAML file
COPY rdkit_ml.yml .

RUN conda env create -f rdkit_ml.yml
 # Override default shell and use bash
SHELL ["conda", "run", "-n", "rdkit_ml", "/bin/bash", "-c"]
# Activate Conda environment and check if it is working properly
SHELL ["conda", "activate", "rdkit_ml", "/bin/bash", "-c"]

#RUN conda activate my-rdkit-env
COPY . .
# PATH
ENV PATH /opt/conda/envs/rdkit_ml/bin:$PATH