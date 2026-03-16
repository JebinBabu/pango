# import pandas as pd

# df = pd.read_csv('B_subtilis.tsv', delimiter='\t')

# df = df[df['Assembly Level'] == 'Complete Genome']
# df = df.drop_duplicates('Organism Infraspecific Names Strain')

# df['new_name'] = df['Assembly Accession'] + "_" + df['Assembly Name']

# for name in df['new_name']:

#     print(name)



import glob
import os

files = glob.glob("../blastresults/*")


for file in files:  

    os.rename(file, file + ".out")