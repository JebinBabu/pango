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

try:
    os.mkdir('../temp/pre_pangenomes/')
except:
    True

# Generating pre-pan genomes

all_genomes_list = pd.read_csv('../temp/all_genomes.txt', header=None)[0].values.tolist()
all_proteins_list = pd.read_csv('../temp/all_proteins.txt', header=None)[0]

df_all_duplicates = pd.DataFrame()

for gcf1 in all_genomes_list:

    pre_pangenome = pd.DataFrame()

    for gcf2 in all_genomes_list:

        if gcf1 == gcf2: 
            continue

        df_blast1 = pd.read_csv(f'{args.inp}{gcf1}_vs_{gcf2}_filtered.csv')[['qseqid','sseqid']]
        df_blast1.columns = [gcf1, gcf2]
        df_blast2 = pd.read_csv(f'{args.inp}{gcf2}_vs_{gcf1}_filtered.csv')[['qseqid','sseqid']]
        df_blast2.columns = [gcf2, gcf1]

        df_overlap = pd.merge(df_blast1, df_blast2, on=[gcf1, gcf2], how='inner')

        # print(df_overlap.shape)


        df_duplicated = df_overlap[df_overlap[gcf1].duplicated()]

        # print(df_duplicated.shape)

        df_final = df_overlap[~df_overlap[gcf1].isin(df_duplicated[gcf1])]


        # print(df_final.shape)
        if pre_pangenome.shape[1] == 0:

            pre_pangenome = df_final.copy()

        else:

            pre_pangenome = pd.merge(pre_pangenome, df_final, on=gcf1, how="left")


    pre_pangenome.to_csv(f'../temp/pre_pangenomes/{gcf1}.csv', index=None)



    
