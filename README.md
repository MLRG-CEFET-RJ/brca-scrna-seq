# SCRNA-Seq Analysis of BRCA patients

This repository hosts the code for an ongoing research on scRNA-seq analysis of BRCA patients.

## Setup

This project is built on Python 3.10.4. Having it installed, the commands below can be run on the root project folder (the one containing this README) on a Linux machine to create a virtual environment with the required packages.

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Important Files

* `geo/read_matrices.py` reads all matrices of [GSE161529](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE161529) and save it in a single gene expression matrix. For a successful execution, files must be downloaded from [GSE161529](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE161529) and extracted to the `geo/data/GSE161529/RAW` folder.
* `geo/sparse-full.ipynb` contains the experiment described on the paper [GSE161529](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE161529).