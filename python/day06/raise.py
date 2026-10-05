def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

def main():
    try:
        validate_age(5)
    except ValueError as error:
        print(f"Validation failed: {error}")

if __name__ == "__main__":
    main()
    