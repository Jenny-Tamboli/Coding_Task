# Demultiplexing FASTQ files

### Usage
1. Clone a repository.
2. Navigate to the directory containing source file.
3. Ensure that the compressed FASTQ file 'demultiplex.fastq.gz' and sample file 'samples.csv' is in the same directory.
4. Run the script using command 'python demultiplex.py'.
5. The output files will be stored in a new directory called 'demultiplexed'.

### Input
The script requires two files 'demultiplex.fastq.gz' and 'samples.csv' as input.

### Output
The output generates one file for each sample in a new directory called 'demultiplexed'.

### Dependencies
Python 3 and Biopython 
