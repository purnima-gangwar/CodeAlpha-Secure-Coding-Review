
import os

password = os.getenv("APP_PASSWORD")

def calculate(operation):
    allowed_operations = {
        "add": lambda: 2 + 3,
        "subtract": lambda: 5 - 3,
    }

    if operation not in allowed_operations:
        raise ValueError("Unsupported operation")

    return allowed_operations[operation]()

def greet(username):
    print(f"Thank you!, {username}")

if __name__ == "__main__":
    greet("Code Alpha")
    print(calculate("add"))
