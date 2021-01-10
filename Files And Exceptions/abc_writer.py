import json

abc = ['a','b','c']   
file = "file.json"
with open(file,'w') as f:
    json.dump(abc,f)