#https: // github.com / DataGlacier / VC.git
import json
import os

# Set the current working directory to the directory of this script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Function to load JSON data from response.json
def load_json(filename='../response.json'):
    if os.path.exists(filename):
        with open(filename) as json_file:
            return json.load(json_file)
    else:
        return {}

# Function to write JSON data to response.json
def write_json(data, filename='../response.json'):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=2)

# Function to prompt user for name and favorite sport
def call_sport():
    response = load_json()
    name = input("Please add your name: ")
    sport = input("Please add your favourite sports name: ")
    
    if not sport:
        sport = 'Cricket'
    
    if name:
        response[name] = sport
        write_json(response)
        print(f"Data added successfully for {name}")

if __name__ == "__main__":
    call_sport()
