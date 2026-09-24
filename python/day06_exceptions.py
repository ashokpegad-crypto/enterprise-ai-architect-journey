def get_value():
    return "123"


def main():
    try:
        result = int(get_value())
    except ValueError as error:
        print(f"Conversion failed: {error}")
    else:
        print(f"Success: {result}")
    finally:
        print("Conversation attempt completed")

if __name__ == "__main__":
    main()