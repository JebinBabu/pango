#!/usr/bin/env python3

from tqdm import tqdm
import requests
import argparse
parser = argparse.ArgumentParser(description="A script that downloads genome files from NCBI using the assembly accession numbers")

parser.add_argument("-i","--inp", type=str, help="Input file containing all RefSeq assembly accessions", required=True)
parser.add_argument("-t","--type", type=str, choices=["nucl","prot"], help="Filetype to download from ncbi", default="nucl", required=True)
parser.add_argument("-o","--out", type=str, help="Output folder", required=True)

args = parser.parse_args()

accessions = []

with open(args.inp, "r") as infile:

    gcf_file = infile.readlines()

    for line in gcf_file:

        line = line.replace("\n","")

        accessions.append(line)

file_types = {"nucl":"_cds_from_genomic.fna.gz","prot":"_protein.faa.gz"}

print(f"Downloading {len(accessions)} {args.type} files!")

count_not_down = 0

for acc in tqdm(accessions):

    acc1 = acc[:3]
    acc2 = acc[4:7]
    acc3 = acc[7:10]
    acc4 = acc[10:13]

    new_filename = acc + file_types[args.type]

    url = f"https://ftp.ncbi.nlm.nih.gov/genomes/all/{acc1}/{acc2}/{acc3}/{acc4}/{acc}/{new_filename}"

    response = requests.get(url)

    if response.status_code == 200:

        with open(args.out + new_filename,"wb") as new_file:

            new_file.write(response.content)

    else:
        print(f"Couldn't download {acc}{file_types[args.type]}, please check the accession or download manually")

        count_not_down += 1

    if count_not_down > 0:

        print(f"{count_not_down} files not downloaded!") 

