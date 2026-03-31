import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


my_type = 'core'

df = pd.read_csv('summary.csv')
df = df[df['type'] == f'{my_type}']
df = df[df['num_strains'] <= 75]
df['Species'] = df['species'].apply(lambda x: x.replace('_','. '))

plt.figure(figsize=(20,15))  

sns.lineplot(
    data=df,
    x="num_strains", y="size", hue="Species",
    err_style="bars", errorbar=("se", 2),linewidth=2.5,
)
plt.ylabel('Size of pan/core genome')
plt.xlabel('Number of strains')

plt.xlabel('Number of Strains', fontsize=40)
plt.ylabel(f'Size of {my_type} genome', fontsize=40)
plt.xticks(fontsize=35)
plt.yticks(fontsize=35)

plt.legend(fontsize=30) 

plt.savefig(f'{my_type}.png')

