#!/usr/bin/python3

__author__ = "Jean-David Grattepanche"
__version__ = "5, March 16, 2017"
__email__ = "jeandavid.grattepanche@gmail.com"


import sys
import os
import re
from Bio import SeqIO
from sys import argv

seqlist = {}

## missing the otufile need to be create in script 3

def countread(seqfile,otufile,samplelist): #,dataname):	
	for Seq in SeqIO.parse(open(seqfile),'fasta'):
		seqlist[Seq.id] = str(Seq.seq)

	outfile = open('outputs/OTUs/OTUtable_temp.txt','w')
	outfile.write('OTU\toccurrence\treadnumber\t' + str(samplelist).replace("', '",'\t').replace("[",'').replace("]",'').replace("'","") + '\n') #add the heading row with samples name
	outfile.close()

	for line in open(otufile,'r'):
		OTUID = line.split('\t')[0]
		allread = []
		occlist = []
		abundance = []
		readnumber= 0
		for read in line.split('\t'  )[1:]:
			samplename = read.split('_')[0].replace(" ","")
			if samplename in samplelist:
				allread.append(samplename)
				if samplename not in occlist:
					occlist.append(samplename)
			else:
				print("ERROR in list")
		occurrence = len(occlist)
		totalread = len(allread)
		print(OTUID, " has occurred in ", occurrence, " samples and is represented by ", totalread, " reads.") 
		if totalread > 1:
			if occurrence > 0:
		
				for R in samplelist:
					readnumber = allread.count(R)
					abundance.append(readnumber)
		
		
#				print(OTUID, " represents", totalread , " for ", occurrence, "samples")
				outfile = open('outputs/OTUs/OTUtable_temp.txt','a')
				outfile.write( OTUID +'\t' + str(occurrence) + '\t' + str(totalread)  + '\t'+ str(abundance).replace(',','\t').replace('[','').replace(']','') +  '\n')
				outfile.close()
				outseq = open(seqfile.split(".")[0]+ "_nosingleton.fas",'a')
				outseq.write(">" + OTUID + '\n' + seqlist[OTUID] + '\n')
				outseq.close()
	
	
				
		
	
def main():
	script, seqfile, otufile, listofsample = argv #, dataname = argv
	samplefile = open(listofsample,'r')
	samplelist= []
	for sample in samplefile:
		if sample.split('\n')[0] != "":
			samplelist.append(sample.split('\n')[0].split('\t')[1].replace('_','.'))
	print(samplelist)
	countread(seqfile,otufile,samplelist) #,dataname)
main()