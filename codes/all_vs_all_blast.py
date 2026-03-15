#!/usr/bin/env python3

import logging
import argparse
import subprocess
import glob
from tqdm import tqdm
parser = argparse.ArgumentParser(description="A script that downloads genome files from NCBI using the assembly accession numbers")

parser.add_argument("-i","--inp", type=str, help="Input folder containing input fasta files", required=True)
parser.add_argument("-e","--ext", type=str, help="Input file extension", default=".fna")
parser.add_argument("-b","--blast_type", type=str, choices=["nucl","prot"], help="Filetype to download from ncbi", default="nucl")
parser.add_argument("-t","--threads", type=int, help="Number of threads", default=8)
parser.add_argument("-o","--out", type=str, help="Output folder", required=True)

args = parser.parse_args()

logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filemode='a')

if args.blast_type == "nucl":    
    blast_type = "blastn"
else:
    blast_type = "blastp"


def run_blast(query, subject, out_file, threads=args.threads):

    cmb_makeblast_db = ["makeblastdb", "-in", subject, "-dbtype", args.blast_type]

    result_makeblast_db = subprocess.run(cmb_makeblast_db, capture_output=True, text=True)

    if result_makeblast_db.returncode != 0:
        logging.error(f"Makeblastdb returned an error!! {result_makeblast_db.stderr}")

    cmd_blast = [
        blast_type, "-query", str(query),
        "-db", subject, "-out", str(out_file),
        "-outfmt", "6", "-num_threads", str(threads)
    ]
    result = subprocess.run(cmd_blast, capture_output=True, text=True)
    return query, result.returncode, result.stderr


fasta_files = glob.glob(args.inp + f"*{args.ext}")[:2]

total_blast_count = len(fasta_files)*(len(fasta_files) - 1)

logging.info(f"Running {total_blast_count} BLASTs")

for file1 in tqdm(fasta_files):

    for file2 in fasta_files:

        if file1 == file2:
            continue
        
        gcf1 = file1.split('/')[-1].replace(args.ext,"")
        gcf2 = file2.split('/')[-1].replace(args.ext,"")
        blast_out_name = args.out + gcf1 + "_vs_" + gcf2

        blast_status = run_blast(file1, file2, blast_out_name)

        if blast_status[1] == 0:
            logging.info(f"Ran BLAST on {gcf1} vs {gcf2} successfully")
        else:
            logging.error(f"Couldn't run BLAST on {gcf1} vs {gcf2}")
            logging.error(f"{blast_status[2]}")
