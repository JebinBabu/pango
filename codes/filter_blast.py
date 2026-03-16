#!/usr/bin/env python3

import logging
import argparse
import pandas as pd
import glob
from tqdm import tqdm
parser = argparse.ArgumentParser(description="A script that downloads genome files from NCBI using the assembly accession numbers")

parser.add_argument("-i","--inp", type=str, help="Input folder containing input fasta files", required=True)
parser.add_argument("-e","--evalue", type=float, help="E-value cutoff", default=1e-5)
parser.add_argument("-p","--pident", type=float, help="Percentage identity cutoff", default=75)
parser.add_argument("-l","--len", type=float, help="Percentage length overlap cutoff", default=80)

args = parser.parse_args()

logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filemode='a')


files = glob.glob(args.inp + "*.out")

for file in tqdm(files):

    df = pd.read_csv(file, delimiter='\t',header=None)
    df.columns = ['qseqid', 'sseqid', 'pident', 'length', 'qlen', 'evalue']

    df1 = df[df['pident'] >= args.pident]
    df1 = df1[df1['evalue'] <= args.evalue]
    df1["len_cov"] = df1['length']/ df1['qlen']
    df1 = df1[df1['len_cov'] >= args.len/100]


    df1.to_csv(file.replace(".out","_filtered.csv"), index=None)

logging.info(f"Filtered {len(files)} blastresults")

