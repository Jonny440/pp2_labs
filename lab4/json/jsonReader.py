import pandas as pd
import json

data = pd.read_json('/Users/Z1/Desktop/pp2_labs/lab4/sample-data.json')
rows = []
for item in data['imdata']:
    attributes = item['l1PhysIf']['attributes']
    rows.append({
        'dn': attributes['dn'],
        'description': attributes['descr'],
        'speed': attributes['speed'],
        'mtu': attributes['mtu']
    })

df = pd.DataFrame(rows)

print(df.to_string(index=False))