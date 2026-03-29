# pango
A bioinformatic pipeline for constructing pan/core genome and phylogenetic tree using python.

### Description

Pango is a bioinformatics pipeline implemented in Python and orchestrated with Snakemake for the construction of pan-genomes and core genomes. It employs an all-vs-all reciprocal BLAST strategy to identify gene homologs across input genomes, providing a robust and sensitive approach to homology detection. As a result, runtime is primarily determined by BLAST computation, which scales with the number and size of input sequences. All auxiliary processing steps are implemented using vectorized pandas operations, ensuring efficient and scalable data handling throughout the pipeline.

Pango does not include proteins having multiple BLAST hits to avoid possible errors in the constructed pan/core genomes.

### Usage 

**Snakemake command:**
```bash
snakemake [options] run_pango
```

**Setting up snakemake config.yaml file**

```yaml
# Example config.yaml file
general:
  species_name: B_subtilis
  reference_genome: GCF_000009045.1_ASM904v1
  mol_type: nucl
  species_list: /home/pango/analysis/M_pneumoniae/B_subtilis.txt
blast:
  num_threads: 1
pango:
  pident: 75
  length_coverage: 75
  evalue: 1e-5
  relaxed_core: 100
```
**Config file options:**
| Variable | Type | Options | Description |
|-------|------|---------|-------------|
| `species_name`       |string||Species name|
| `reference_genome`   |string||Accession for reference genome used in the pipeline. (Does not affect the results)|
| `mol_type` |string|*nucl* or *prot*|Determines the fasta file to be used in pipeline. [nucl: nucleotide / fna, prot: protein / faa]|
| `species_list` |path||Path to the file containing accessions for genome files to be used|
| `num_threads `         |||Number of threads to be allocated for BLAST|
| `pident `         |float||percentage identity to determine homology after running BLAST|
| `length_coverage `         |float||Length overlap to determine homology after running BLAST|
| `evalue `         |float||evalue to determine homology after running BLAST|
| `relaxed_core `         |float||For generating relaxed core genome|

### Example run

blastresults no included

Bacterial lifestyle shapes pangenomes
The consequences of genetic drift for bacterial genome complexity
Factors driving effective population size and pan-genome evolution in bacteria