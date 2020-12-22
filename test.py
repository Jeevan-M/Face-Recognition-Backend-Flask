import json
import urllib.request
url = 'http://sietface.000webhostapp.com/Face_Encoding_Data.json'
fileName = 'Face_Encoding_Data.json'
data = json.loads(urllib.request.urlopen(url).read().decode())
print(type(data))
