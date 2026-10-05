def load_file(file_path):
    with open(file_path, "r") as file:
        data = file.read()


def main():
    try:
        load_file("missing_employee.json")
    except FileNotFoundError:
        print("File loading failed: input file was not found.")
    else:
        print("File loaded successfully.")
if __name__ == "__main__":
    main()