import json

def load_json_file(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
        return data

def main():
    file_path = "employees.csv"
    try:
        load_json_file(file_path)
    except FileNotFoundError:
        print(f"JSON loading failed: file not found. {file_path}")
    except json.JSONDecodeError:
        print(f"JSON loading failed: invalid JSON. {file_path}")
    else:
        print("JSON loaded successfully.")
if __name__ == "__main__":
    main()