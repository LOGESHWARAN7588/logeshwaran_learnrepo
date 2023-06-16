import json


with open('data.json', 'r') as file:
    data = json.load(file)


for ex5 in data:
    if ex5['name'] == 'Old Fashioned':
       
        last_id=str(int(ex5['batters']['batter'][-1]['id']) + 1)
        ex5['batters']['batter'].append({'id': last_id, 'type': 'Coffee'})
        break  
   
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)