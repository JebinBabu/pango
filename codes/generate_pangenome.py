#!/usr/bin/env python3

import logging
import argparse
import pandas as pd
import glob
from tqdm import tqdm
import os
parser = argparse.ArgumentParser(description="A script that downloads genome files from NCBI using the assembly accession numbers")

parser.add_argument("-i","--inp", type=str, help="Input folder containing input fasta files", required=True)
parser.add_argument("-c","--core_perc", type=float, help="Relaxed cutoff for core genome", default = 100)
parser.add_argument("-o","--out", type=str, help="Output folder", required=True)

args = parser.parse_args()

logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filemode='a')


# Generating pre-pan genomes

files = glob.glob(args.inp + "*_filtered.csv")

# try:
#     os.remove('../temp/all_paralogs.txt')
# except:
#     True
    
# for file in tqdm(files):

#     gcf1, gcf2 = file.split("/")[-1].replace('_filtered.csv',"").split("_vs_")

#     df = pd.read_csv(file)

#     df['paralog'] = df.duplicated('qseqid')

#     df_paralogs = df[df['paralog'] == True][['qseqid','sseqid']]

#     df_paralogs[['qseqid']].to_csv('../temp/all_paralogs.txt', header=False, mode='a', index=None)
#     df_paralogs[['qseqid']].to_csv('../temp/all_paralogs.txt', header=False, mode='a', index=None)


all_paralogs = pd.read_csv('../temp/all_paralogs.txt',header=None)
all_paralogs.drop_duplicates(inplace=True)

all_paralogs.to_csv('../temp/all_paralogs.txt', header=False, index=None)




