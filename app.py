
# Sample application for secure coding review

password = "admin123"  # Hardcoded password

def calculate(expression):
    return eval(expression)  # Unsafe evaluation of user input

def greet(username):
    print("Welcome, " + username)

if __name__ == "__main__":
    greet("Student")
    print(calculate("2 + 3"))
