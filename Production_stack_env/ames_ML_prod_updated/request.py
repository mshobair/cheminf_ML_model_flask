
import request

url = 'http://localhost:5000/results'
r = request.post(url,json={'Smiles':'CCC'})

print(r.json())