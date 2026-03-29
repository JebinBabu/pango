# pango
A bioinformatic pipeline for constructing pan/core genome and phylogenetic tree using python.

### Description

Pango is a bioinformatics pipeline implemented in Python and orchestrated with Snakemake for the construction of pan-genomes and core genomes. It employs an all-vs-all reciprocal BLAST strategy to identify gene homologs across input genomes, providing a robust and sensitive approach to homology detection. As a result, runtime is primarily determined by BLAST computation, which scales with the number and size of input sequences. All auxiliary processing steps are implemented using vectorized pandas operations, ensuring efficient and scalable data handling throughout the pipeline.

Pango does not include proteins having multiple BLAST hits to avoid possible errors in the constructed pan/core genomes.

### Example run

blastresults no included

Bacterial lifestyle shapes pangenomes
The consequences of genetic drift for bacterial genome complexity
Factors driving effective population size and pan-genome evolution in bacteria