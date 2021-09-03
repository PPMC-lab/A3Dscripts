import time
import csv
with open('A3D_results.txt', 'w') as outfile:
	outfile.write('PDB\tA3D Average Score\n')
	with open('jobids.txt', 'w') as jobids_file:
		lines = infile.readlines()
		csvlines=csv.reader(lines, delimiter='\t')
		for line in csvlines:
			pdbid=line[0]
			jobid=line[1]
		url2='http://biocomp.chem.uw.edu.pl/A3D2/RESTful/job/{}/'.format(jobid)
		req = requests.get(url2)
		data = req.json() 
		a3d_av_score = data['A3Dscore']['avg']
		outfile.write('{}\t{}\n'.format(pdbid ,a3d_av_score))
		time.sleep(1)
