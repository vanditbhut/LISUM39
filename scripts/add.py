import json
import os

try:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
except NameError:

    pass

def load_json():
    try:
        with open('../response.json') as json_obj:
            response = json.load(json_obj)
    except FileNotFoundError:
        print("response.json not found, creating a new one.")
        response = {}
    except json.JSONDecodeError:
        print("Error reading JSON, creating a new response.")
        response = {}
    return response


def write_json(data, filename='../response.json'):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=0)
    except Exception as e:
        print(f"Failed to write to {filename}: {e}")


def call_sport():
    name = input("Please add your name: ").strip()
    sport = input("Please add your favorite sport: ").strip()


if __name__ == "__main__":
    response = load_json()  # Load once and reuse
    call_sport()
