import json

with open('../data/schacon.repos.json', 'r') as file:
    data = json.load(file)

with open('chacon.csv', 'w') as csv_file:
    csv_file.write("name,html_url,updated_at,visibility\n")
    
    for entry in data[:5]:
        name = entry['name']
        html_url = entry['html_url']
        updated_at = entry['updated_at']
        visibility = entry['visibility']
        
        csv_file.write(f"{name},{html_url},{updated_at},{visibility}\n")