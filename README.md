# pango
A bioinformatic pipeline for constructing pan/core genome using python.

### Description

Pango is a bioinformatics pipeline implemented in Python and orchestrated with Snakemake for the construction of pan-genomes and core genomes. It employs an all-vs-all reciprocal BLAST strategy to identify gene homologs across input genomes, providing a robust and sensitive approach to homology detection. As a result, runtime is primarily determined by BLAST computation, which scales with the number and size of input sequences. All auxiliary processing steps are implemented using vectorized pandas operations, ensuring efficient and scalable data handling throughout the pipeline.

### Benchmarking

The pan-genome of a species provides critical insights into its biology and evolutionary history. The environment a species inhabits shapes its population dynamics, which in turn drives modifications to its gene pool. Species occupying a broad range of habitats tend to accumulate a larger repertoire of genes, whereas obligate parasites undergo genome reduction as an adaptation to their specific host niche. Additional factors influencing gene pool composition include effective population size and genetic drift. Consequently, characterising the pan-genome and core genome has become an integral component of population genetics and evolutionary studies.

To benchmark Pango, I selected four well-characterised bacterial species, each represented by more than 90 complete genomes annotated in the NCBI RefSeq database. Two facultative pathogens (Escherichia coli and Bacillus subtilis) and two obligate pathogens (Mycoplasmoides pneumoniae and Helicobacter pylori) were chosen to capture the contrasting trends expected in pan-genome and core genome architecture. Pan-genomes and core genomes were constructed by incrementally sampling from 10 to 90 strains, with five independent random samplings performed at each interval. In a complementary analysis, gene frequency distributions were examined at a fixed strain count. Together, these analyses provide a framework for interpreting the distinct evolutionary trajectories and gene pool dynamics characteristic of each bacterial lifestyle.

### Usage 

**Steps to run the pipeline:** 

1. copy the `codes` folder to the working directory (Ideally a directory for a species). 
2. Make a list of genome accessions to be used.
3. Give necessary permissions to the shell scripts for creating necessary folders.
4. Set up the `config.yaml` file.
5. Set up the conda environment using the `environment.yml` file.
5. Run `make_folders.sh`
6. Run the pipeline using snakemake.

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
  species_list: /home/pango/analysis/B_subtilis/B_subtilis.txt
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

### The pipeline
Pango does not include proteins having multiple BLAST hits to avoid possible errors in the constructed pan/core genomes.
### Example run

blastresults not included

1. Bacterial lifestyle shapes pangenomes
2. Factors driving effective population size and pan-genome evolution in bacteria
3. The consequences of genetic drift for bacterial genome complexity
4. Producing polished prokaryotic pangenomes with the Panaroo pipeline
5. Roary: rapid large-scale prokaryote pan genome analysis

How to read outfiles, pan and core genomes
Correct pan output file name snakemake errors
Integrate makefolder to pipeline
change snaketemp naming

**Claude.ai used for paraphrasing this README*