import json

# Read the JSON  from the file
with open('data.json', 'r') as file:
    data = json.load(file)

# Find the donut with name "Old Fashioned"
for ex5 in data:
    if ex5['name'] == 'Old Fashioned':
        # Add a new batter named "Coffee"
        last_id=str(int(ex5['batters']['batter'][-1]['id']) + 1)
        ex5['batters']['batter'].append({'id': last_id, 'type': 'Coffee'})
        break  
    # Stop iterating since we found the donut

# Write the updated data back to the file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)