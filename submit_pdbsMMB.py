import requests
import json

pdbids_jobs=[]
with open('list.txt', 'r') as pdbids_file:
  for line in pdbids_file:
		pdbids_jobs.append(line[0:4])

with open('jobids.txt', 'w') as jobids_file:
  for pdbid in pdbids_jobs:
    url='http://biocomp.chem.uw.edu.pl/A3D2/RESTful/submit/{}/'.format(pdbid)
    req = requests.post(url)
    print(req.status_code, req.text)
    try:
      jobid=(req.json()['jobid'])
    except:
      jobid= ‘Error found. Check pdb code is correct.’
    jobids_file.write('{}\t{}\n'.format(pdbid, jobid))
