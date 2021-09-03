import requests
import json
url='http://biocomp.chem.uw.edu.pl/A3D2/RESTful/submit/1PHT/'

req=requests.post(url)
print(req.status_code, req.text)
