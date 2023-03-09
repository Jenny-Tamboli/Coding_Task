import csv
import gzip
from Bio import SeqIO
import os

# read a csv file and create a dictionary of each index and sampleID
indices = {}
with open ('samples.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)

    for row in reader:
        indices[row[1]] = row[0]
    #print(indices)

# create a new directory to store demultiplexed output files
if not os.path.exists('demultiplexed'):
   os.mkdir('demultiplexed')

# open a fastq file as a input and parse each record with SeqIO module
with gzip.open("demultiplex.fastq.gz", "rt") as input_file:
    
    for record in SeqIO.parse(input_file, 'fastq'):
        index = record.description.split(':')[-1]
        #print(f'Found index sequence: {index}')

        # check for the presence of sample_id based on index
        if index in indices:
            sample_id = indices[index]  
        else:
            sample_id = 'unknown'

        # create and write the records in appropriate sample file
        with open(os.path.join('demultiplexed', f'{sample_id}.fastq'), 'a') as output_file:
            SeqIO.write(record, output_file, 'fastq')
        
