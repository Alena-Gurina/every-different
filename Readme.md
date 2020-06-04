# Repetitive DNA comparison of different primitive cultivated potato species. 
### Gurina A., Divashuk M.

Big part of plant genome refers to repetitive genome fraction, include tandem repeats (satellites), LTR-elements and transposones. <br>
These part generally difficult in assambly and analysing. To identify these elements specific tools, such RepeatExplorer, could be used.
__So aim of these work is to compare repetitive DNA fraction of primitive potato species__
<br> <br>
To perform it, the following tasks were set:
- select samples with SRA data available in NCBI
- find repetitive elements using TAREAN
- compare repetitive DNA fraction of different primitive cultured potato species




#### __Requirements__
*Tested on UBUNTU 19.10*
<ol>
    <li> RepeatExplorer [1] with TAndem REpeats ANaliser (Tarean) tool[2]
    <li> Python3.6 or higher with packages:</li>
    - pandas 0.25.3<br>
    - numpy 1.18.1<br>
    - scikitlearn 0.23.0 <br>
    - matplotlib 3.2.0<br>
    - seaborn 0.10.0<br>
    - folium 0.11.0<br>
    - os <br>
    - argparse 1.1<br>
    <li> FastQC v0.11.8 [3] </li>
    <li> Preprocession of FASTQ paired-end reads on Galaxy 19.09 [4] </li>
    <li> NCBI SRA toolkit 2.9.3 [4] </li>
    <li> BLAST Command line Applications </li>
</ol>

#### __Pipeline__
<ol>
    <li> Collecting SRA data from NCBI using SRA toolkit [4] </li>
    <li> Checking reads quality using FastQC [3] </li>
    <li> Preprocessing data on Galaxy server using specific tools (Preprocessing of paired-end reads in FASTQ format including trimming, quality filtering, cutadapt filtering and interlacing. Broken pairs are discarded).
</ol>


```python

```


```python

```

#### Liturature
<ol>
    <li>Novák, P., Neumann, P., Pech, J., Steinhaisl, J. & Macas, J. RepeatExplorer: a Galaxy-based web server for genome-wide characterization of eukaryotic repetitive elements from next-generation sequence reads. Bioinformatics 29, 792–793 (2013).</li>
    <li>Novak, P., Avila Robledillo, L., Koblizkova, A., Vrbova, I., Neumann, P., Macas, J. (2017) – TAREAN: a computational tool for identification and characterization of satellite DNA from unassembled short reads. Nucleic Acids Res., doi:10.1093/nar/gkx257</li>
    <li> FastQC: A Quality Control Tool for High Throughput Sequence Data [Online]. Available online at: http://www.bioinformatics.babraham.ac.uk/projects/fastqc/ (2015), "FastQC," https://qubeshub.org/resources/fastqc.</li>
    <li> [Galaxy] (http://repeatexplorer-elixir.cerit-sc.cz/galaxy) </li>
    <li> Sequence Read Archive Submissions Staff. Using the SRA Toolkit to convert .sra files into other formats. In: SRA Knowledge Base [Internet]. Bethesda (MD): National Center for Biotechnology Information (US); 2011-. Available from: https://www.ncbi.nlm.nih.gov/books/NBK158900/ </li>
    <li> BLAST® Command Line Applications User Manual [Internet]. Bethesda (MD): National Center for Biotechnology Information (US); 2008-. Available from: https://www.ncbi.nlm.nih.gov/books/NBK279690/ </li>
    
</ol>

- pretraining include: filtering low-quality, unpaired and short reads (processing in Galaxy)
- from sample for each programm launch we randomly selected fraction about 400000 each forward and reverse reads (totally about 800000). It was done by script *rand_for_fasta.py*
- for each sample 5 times launched Repeat Explorer with Tarean add-in to find repetitive fraction (example of tarean report ....)
- data preprocessing include collecting data from all Tarean reports, creating local blast database based on all sequences, get into with investigetion
- to compare repatitive fraction we have done local blast all repeats againsr itself and then we analyses matches
