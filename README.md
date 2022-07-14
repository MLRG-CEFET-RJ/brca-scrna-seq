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

* `geo/sklearn.py` contains the pipelines built on top of [GSE75688](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE75688), a dataset with 549 cells of 11 breast cancer patients.

## Next Steps

* Find larger dataset (a potential candidate is [GSE161529](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE161529), which contains about 430,000 cells).
* Implement Differential Cluster Analysis.
* Verify the need of a QC step prior to the data pipelines execution.