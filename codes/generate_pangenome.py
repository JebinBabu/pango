#!/usr/bin/env python3

import logging
import argparse
import pandas as pd
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

all_genomes_list = pd.read_csv('../temp/all_genomes.txt', header=None)[0].values.tolist()[:10]
all_proteins_list = pd.read_csv('../temp/all_proteins.txt', header=None)[0]


for gcf1 in tqdm(all_genomes_list):

    pre_pangenome = pd.DataFrame()

    for gcf2 in all_genomes_list:

        if gcf1 == gcf2: 
            continue

        df_blast1 = pd.read_csv(f'{args.inp}{gcf1}_vs_{gcf2}_filtered.csv')[['qseqid','sseqid']]
        df_blast1.columns = [gcf1, gcf2]
        df_blast2 = pd.read_csv(f'{args.inp}{gcf2}_vs_{gcf1}_filtered.csv')[['qseqid','sseqid']]
        df_blast2.columns = [gcf2, gcf1]

        df_overlap = pd.merge(df_blast1, df_blast2, on=[gcf1, gcf2], how='inner')

        df_duplicated = df_overlap[df_overlap[gcf1].duplicated()]

        df_final = df_overlap[~df_overlap[gcf1].isin(df_duplicated[gcf1])]
        
        if pre_pangenome.shape[1] == 0:

            pre_pangenome = df_final.copy()

        else:

            pre_pangenome = pd.merge(pre_pangenome, df_final, on=gcf1, how="left")

    pre_pangenome = pre_pangenome[all_genomes_list]
    pre_pangenome.to_csv(f'../temp/pre_pangenomes/{gcf1}.csv', index=None)



# Compiling pre-pangenomes

df_pre_pangenome_final = pd.DataFrame()

for gcf in tqdm(all_genomes_list):

    df_pre_pangenome = pd.read_csv(f"../temp/pre_pangenomes/{gcf}.csv",dtype=str)

    if df_pre_pangenome_final.shape[0] == 0:

        df_pre_pangenome_final = df_pre_pangenome.copy()

    else:

        df_pre_pangenome_final = pd.merge(df_pre_pangenome_final, df_pre_pangenome, on=all_genomes_list, how='outer', validate='1:1')




df_pre_pangenome_final.to_csv('../pangenome.csv',index=None)