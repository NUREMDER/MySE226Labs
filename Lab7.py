
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except:
        return "Cannot divide by zero"

def power(x, y):
    return x ** y

def mod(x, y):
    return x % y

# Calculator
def calculator():
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    op = input("Enter operator (+, -, *, /, **, %): ")
    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        operations = {
            '+': add,
            '-': subtract,
            '*': multiply,
            '/': divide,
            '**': power,
            '%': mod
        }
        if op in operations:
            print("Result:", operations[op](a, b))
        else:
            print("Invalid operator")
    else:
        print("Invalid input")


def reverse_string(s):
    return s[::-1]

def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

def remove_punctuation(s):
    result = ""
    for char in s:
        if char.isalpha() or char.isspace():
            result += char
    return result

def count_characters(s):
    return len(s.replace(" ", ""))

def count_words(s):
    return len(s.split())

def average_word_length(s):
    words = s.split()
    total = 0
    for word in words:
        total += len(word)
    if len(words) == 0:
        return 0
    return total / len(words)

def string_analyzer():
    text = input("Enter a sentence: ")
    reversed_text = reverse_string(text)
    capitalized_text = capitalize_words(text)
    print("Reversed:", reversed_text)
    print("Capitalized:", capitalized_text)

    no_punc = remove_punctuation(text)
    print("Without punctuation:", no_punc)
    print("Character count:", count_characters(no_punc))
    print("Word count:", count_words(no_punc))
    print("Average word length:", average_word_length(no_punc))


if __name__ == "__main__":
    print("1 - Calculator")
    print("2 - String Analyzer")
    choice = input("Choose 1 or 2: ")
    if choice == "1":
        calculator()
    elif choice == "2":
        string_analyzer()
    else:
        print("Wrong choice")
