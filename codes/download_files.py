#!/usr/bin/env python3

import subprocess
import pandas as pd
import argparse
parser = argparse.ArgumentParser(description="A script that downloads genome files from NCBI using the assembly accession numbers")

parser.add_argument("--inp", type=str, help="NCBI assembly summary file")
parser.add_argument("--out", type=str, help="Output folder")

args = parser.parse_args()


df = pd.read_csv(args.inp, sep='\t')

df = df[df['Assembly Level'] == 'Complete Genome']
df = df.drop_duplicates('Organism Infraspecific Names Strain')

print(df.shape)


cmd = "curl https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/009/045/GCF_000009045.1_ASM904v1/GCF_000009045.1_ASM904v1_protein.faa.gz -o GCF_000009045.1_ASM904v1_protein.faa.gz"