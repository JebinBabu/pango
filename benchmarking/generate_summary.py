import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


folders = ['E_coli','B_subtilis','H_pylori','M_pneumoniae']
# folders = ['E_coli','H_pylori','M_pneumoniae']

new_data = {'species':[],'num_strains':[],'iteration':[],"type":[], 'size':[]}

for folder in folders:
    new_data['num_strains'].append(0)
    new_data['iteration'].append(0)
    new_data['type'].append('pan')
    new_data['species'].append(folder)
    new_data['size'].append(0)

    new_data['num_strains'].append(0)
    new_data['iteration'].append(0)
    new_data['type'].append('core')
    new_data['species'].append(folder)
    new_data['size'].append(0)

    for i in range(5,91,5):

        for j in range(5):

            df_pan = pd.read_csv(f'./{folder}/out_{j}/pangenome_g{i}.csv',header=None,dtype=str)

            df_core = pd.read_csv(f'./{folder}/out_{j}/coregenome_g{i}_100%.csv')

            print(df_pan.shape)


            new_data['num_strains'].append(i)
            new_data['iteration'].append(j)
            new_data['type'].append('pan')
            new_data['size'].append(df_pan.shape[0])
            new_data['species'].append(folder)

            new_data['num_strains'].append(i)
            new_data['iteration'].append(j)
            new_data['type'].append('core')
            new_data['size'].append(df_core.shape[0])
            new_data['species'].append(folder)


df_new = pd.DataFrame(new_data)

df_new.to_csv('summary.csv',index=None)