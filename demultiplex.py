import gzip
from Bio import SeqIO
import os

# create a dictionary to sample indices
indices = {"CCGCGGTT": "Sample1", 
           "CAAGCTAG": "Sample2", 
           "AGCCTCAT": "Sample3",
           "TGGATCGA": "Sample4"}

# create a new directory to store demultiplexed output files
if not os.path.exists('demultiplexed'):
    os.mkdir('demultiplexed')

# open a fastq file as a input 
with gzip.open("demultiplex.fastq.gz", "rt") as input_file:
    
    # parse each record of a fastq file with SeqIO module
    for record in SeqIO.parse(input_file, 'fastq'):
        index = record.description.split(':')[-1]
        #print(f'Found index sequence: {index}')

        # check for sampleID based on index
        if index in indices:
            sample_id = indices[index]  
        else:
            sample_id = 'unknown'

        # create and write the records in appropriate sample file
        with open(os.path.join('demultiplexed', f'{sample_id}.fastq'), 'a') as outfile:
            SeqIO.write(record, outfile, 'fastq')
        
