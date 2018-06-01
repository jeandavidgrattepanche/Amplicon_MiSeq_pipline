# Amplicon_MiSeq_pipeline
This repository contains scripts and database to analyse MiSeq data for Amplicon generate with SAR primers.

# Amplicon_MiSeq_pipeline for other lineages
This set of scripts can be edited by building the database folder (see SSU_database_building repository) and replacing the database in the script MiSeq_pipeline_SAR_SWARM_part2.py and script 6 (look for SAR_db and replace by the corresponding files). Do not forget to update PEAR parameter in MiSeq_pipeline_SAR_SWARM_part1.py (see here for parameters https://sco.h-its.org/exelixis/web/software/pear/doc.html)

Place to update if you use another database:
- MiSeq_pipeline_SAR_SWARM_part2.py lines 61, 62, 66, 68, 69 and 73 

	*61 and 68: replace file after '--mapout' by your reference sequence alignment
	
	*62 and 69: replace the last argument by your list of column with missing data
	
	*66 and 73: replace the "-t" argument by your reference tree
	
- script 6: line 15 

	line 15: replace the SAR_db value by your BLAST db (do not forget to add the database folder)

# Pipeline Guide

A whole pipeline (scripts and folders structure) for MiSeq analysis.

Prepare your data and folders:

0- keep the same folders and files structure from the repository or the scripts will crash!

1- Create a folder named Rawdata with all your MiSeq sequence files (e.g. LAKM1_To.1.2_S1_L001_R1.fastq.gz, LAKM1_To.1.2_S1_L001_R2.fastq.gz)

	You can use the script movefile.py to create this folder

2- Create a file with your sample code and sample name (there should be a file named List_samples.txt containing: LKM## (tab) samplename ) \n '

	You can use excel to create this file and save as a Tab Delimited Text (.txt) file
	
	So far, the List_samples.txt file includes all the samples generated by the Katzlab. Delete the samples you are not interested in.
	
3- Copy the script folder, SAR_db folder and the 3 scripts named MiSeq_pipeline_SAR_SWARM_part(1,2 and 3).py from this repository and add all in the folder where you save the samplelist.txt and the rawdata folder (suggestion MiSeq_folder).

4- Open the script 6 (in Miseq_scripts folder, named 6_BLASTn_V2.py).

	Replace the XXX by the email address you are using for your NCBI account => Entrez.email = "XXX@xx.xx"
	
	If you don't an NCBI account, you should create one by going to this ncbi webpage (https://www.ncbi.nlm.nih.gov/account/register/?back_url=https%3A%2F%2Fwww.ncbi.nlm.nih.gov%2Fbioproject&partners-uri=cms:/account/partners)

More description available in Guide_MiSeqPipeline_2018.txt.

An undergraduate proofread guide can be shared on request.
