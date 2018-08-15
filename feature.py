#!/usr/bin/env python3

import json

python_obj={}
python_obj['name']='francis'
python_obj["age"]=18

json_obj='{"name":"evan", "age":20}'

dumps=json.dumps(python_obj)
loads=json.loads(json_obj)
print(type(dumps))
print(dumps)

print(type(loads))
print(loads)



