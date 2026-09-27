def greet():
    print("Hello from greet")

def goodbye():
    print("Goodbye from goodbye")

def execute(action):
    print("Starting execution")
    action()
    print("Execution completed")

execute(greet)
execute(goodbye)