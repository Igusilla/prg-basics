import json
import os
# Read the contents of the json file
votes = {

}
if os.path.exists("voting.json"):
    with open('voting.json', 'r', encoding='utf-8') as file:
        votes = json.load(file)    

person_name = input('Name of the person you are voting for: ')
try: 
    votes[person_name]+=1
except:    
    votes[person_name]=1
with open('voting.json', 'w', encoding='utf-8') as file:
    json.dump(votes, file, ensure_ascii=False, indent=4)
