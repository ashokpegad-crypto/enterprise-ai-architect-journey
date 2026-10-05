import json
try:
    with open("custo_summary.json", "r") as file:
        summary = json.load(file)
        
    print("Summary Loaded Successfully")
    print("Total Cumstomers:", summary["total_customers"])

except FileNotFoundError:
    print("Error: JSON file was not found")
except json.JSONDecodeError:
    print("Error: JSON file contails invalid JSON")
except KeyError as error:
    print("Error: Missing key ",error)
except Exception as error:
    print("Unexpected error occurred: ", error)
