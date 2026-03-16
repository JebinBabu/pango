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

args = parser.parse_args()

logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filemode='a')