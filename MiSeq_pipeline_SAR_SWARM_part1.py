# python3 MiSeq_pipeline_SAR_SWARM_part1.py list_sample.txt
#!/usr/bin/python3

__author__ = "Jean-David Grattepanche"
__version__ = "5b, December 19, 2016"
__email__ = "jeandavid.grattepanche@gmail.com"


import string
import re
import sys
import os
from Bio import SeqIO
from sys import argv
seqlist = []
OTUlist = []
duplicatelist = []



def runPEAR(folder, file1, file2, path, outputpath):
	folderP = folder.split('/')[0]

	if not os.path.exists(outputpath +'PEAR/'):
		os.makedirs(outputpath+"PEAR/")
	try:
		os.system('pear -f ' +  path+file1 + ' -r ' + path+file2 + ' -o ' + outputpath + 'PEAR/'+ folder + ' -n 120 -m 300 -q 33 -v 100 -u 0 -j 2')
	except:
		os.system('pear -f ' +  path+file1 + ' -r ' +  path+file2 + ' -o ' + outputpath + 'PEAR/'+ folder  + ' -n 120 -m 300 -q 33 -v 100 -u 0 -j 2')
		print ("PEAR used the SAR parameters (120/300/33/100/0/2)!! check the parameters!")
	print ("Convert")
	if not os.path.exists(outputpath + 'convertPEARfiles/'): 
		os.makedirs(outputpath + 'convertPEARfiles/') 	
	os.system('python3 Miseq_scripts/0_convert_fastq_fasta.py ' + outputpath + 'PEAR/' + folderP + '.assembled.fastq') # -c fastq_to_fastaqual -o ' + outputpath + 'convertPEARfiles/')  #convert fastq file in fasta + qual files


def main():
	samplefile = sys.argv[1]
	pathA = os.getcwd()
	path = pathA + "/Rawdata/"
	listsamp = []
	try:
		listsample = samplefile
	except ValueError:
		samplefile = ""	
	if samplefile == "":
		print ('Your input samplefile is empty.  Try again. ')
	
	for samp in open(listsample,'r'):
		if samp.split('\t')[0] not in listsamp:
			listsamp.append(samp.split('\t')[0])
	print(len(listsamp), "samples")
	outputpath = pathA + '/outputs/'
	if not os.path.exists(outputpath): 
		os.makedirs(outputpath) 	
	temppath = pathA + '/temp/'
	if not os.path.exists(temppath): 
		os.makedirs(temppath) 	
	filnum = 0
	for file in os.listdir(path):
		if 'R1' in file and file.split('_')[0] in listsamp:
			print ("sample: ", file.split('_')[0])
			print ("file1: ",file, file.split('_')[0])
			file1 = file
			for filee in os.listdir(path):
				if 'R2' in filee and filee.split('_')[0] == file1.split('_')[0]:
					print ("file2: ",filee)
					file2 = filee
					folder = file1.split("_")[0]+"_"+file1.split("_")[1]
					filnum += 1
					runPEAR(folder, file1, file2, path, outputpath)
	if len(listsamp) != filnum:
		print( "ISSUE with sample list! PLEASE CHECK !")
	else:
		print("all Okay, go to the part2 !!")

main()
