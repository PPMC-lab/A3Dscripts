import requests
import json

mutation_table = [{'idx': 5, 'chain': 'A', 'oldres': 'G', 'newres': 'A'},
				  {'idx': 27, 'chain': 'A', 'oldres': 'G', 'newres': 'A'}]

options = {'dynamic':True,
            'distance':10,
            'email':'user@domain.com',
            'name':'MMB_2',
            'hide':False,
            'mutate':mutation_table,
            'foldx':True,
            'auto_mutation':None}

url='http://biocomp.chem.uw.edu.pl/A3D2/RESTful/submit/1PHT/'

req = requests.post(url,
					data=json.dumps(options),
					headers={'content-type': 'application/json'})
print(req.status_code, req.text)

