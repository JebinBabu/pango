#!/usr/bin/env python3

import logging
import argparse
import glob
import os
from tqdm import tqdm
parser = argparse.ArgumentParser(description="A script that downloads genome files from NCBI using the assembly accession numbers")

parser.add_argument("-i","--inp", type=str, help="Input folder containing input fasta files", required=True)
parser.add_argument("-e","--ext", type=str, help="Input file extension", default=".fna")
parser.add_argument("-o","--out", type=str, help="Output folder", required=True)

args = parser.parse_args()

logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filemode='a')

fasta_files = glob.glob(f"{args.inp}*{args.ext}")

logging.info(f"Parsing {len(fasta_files)} {args.ext} files")

try:
    os.mkdir('../temp')
    logging.info(f"Making temp folder")
except:
    True

with open("../temp/all_proteins.txt",'w') as all_proteins, open("../temp/all_genomes.txt",'w') as all_genomes:

    # all_proteins.write(f'accession, protein_new_name, details\n')

    for file in tqdm(fasta_files):

        gcf = file.split('/')[-1].replace(args.ext,'')
        gcf_spliced = "_".join(gcf.split('_')[:2])

        all_genomes.write(f"{gcf_spliced}\n")

        with open(file,'r') as infile, open(f"{args.out}{gcf_spliced}{args.ext}",'w') as outfile:

            count = 0

            while True:

                line = infile.readline()

                if len(line) == 0:
                    break

                if ">" in line:

                    protein_name = f"{gcf_spliced};protein_{count}"

                    outfile.write(f">{protein_name}\n")
                    # all_proteins.write(f"{gcf_spliced}, {protein_name}, {line.split(' ')[0]}\n")
                    all_proteins.write(f"{protein_name}\n")
                    count += 1
                    continue

                outfile.write(line)
            

                
