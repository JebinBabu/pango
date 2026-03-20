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

with open('../temp/all_duplicates.csv','w') as dup_file:
    dup_file.write('')    

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

        df_duplicated.columns = ['x','y']
        df_duplicated.to_csv('../temp/all_duplicates.csv',header=None, index=None,mode='a')

        
        if pre_pangenome.shape[1] == 0:

            pre_pangenome = df_final.copy()

        else:

            pre_pangenome = pd.merge(pre_pangenome, df_final, on=gcf1, how="left")

    pre_pangenome = pre_pangenome[all_genomes_list]
    pre_pangenome.to_csv(f'../temp/pre_pangenomes/{gcf1}.csv', index=None)


# arranging protein families

# protein_families = []

# for gcf in tqdm(all_genomes_list):

#     df_pre_pan = pd.read_csv(f'../temp/pre_pangenomes/{gcf}.csv',header=None)
#     df_pre_pan = df_pre_pan.iloc[1:]

#     if len(protein_families) == 0:

#         protein_families = df_pre_pan.values.tolist()

#     else:

#         for new_protein_family in df_pre_pan.values.tolist():

#             for protein_family_id, existing_protein_families in enumerate(protein_families):

#                 new_fam_set = set(new_protein_family)
#                 existing_fam_set = set(existing_protein_families)

#                 if len(new_fam_set.intersection(existing_fam_set)) >= 2:

#                     protein_families[protein_family_id] = list(new_fam_set.union(existing_fam_set))

#                     break

            
#             protein_families.append(new_protein_family)

df_pangenome = pd.DataFrame()

for gcf in all_genomes_list:

    df_pre_pan = pd.read_csv(f'../temp/pre_pangenomes/{gcf}.csv')

    if df_pangenome.shape[0] == 0:

        df_pangenome = df_pre_pan.copy()
        

    else:

        df_pangenome = pd.merge(df_pangenome, df_pre_pan, on=all_genomes_list, how='outer')


df_pangenome.to_csv(f'{args.out}pan.csv',index=None)




