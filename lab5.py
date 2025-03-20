import random
import string
#I want to make lots of function and while loop practise.
def get_replacements():
    replacements = {}
    count = 0
    while count < 5:
        char = input("Enter a lowercase character: ").strip()
        if char in string.ascii_lowercase and char not in replacements:
            options = []
            option_count = 0
            while option_count < 3:
                rep = input(f"Enter a replacement for '{char}': ").strip()
                if len(rep) == 1 and rep not in options:
                    options.append(rep)
                    option_count += 1
                else:
                    print("Invalid input. Please try again.")
            replacements[char] = options
            count += 1
        else:
            print("Invalid input. Please try again.")
    return replacements

def generate_passwords(count):
    passwords = []
    i = 0
    while i < count:
        password = ''.join(random.choices(string.ascii_lowercase, k=15))
        passwords.append(password)
        i += 1
    return passwords


def modify_and_classify(passwords, replacements):
    strong_passwords = []
    weak_passwords = []
    index = 0
    while index < len(passwords):
        password = passwords[index]
        new_password = ""
        replaced_count = 0
        char_index = 0
        while char_index < len(password):
            char = password[char_index]

            if char in replacements:
                new_password += random.choice(replacements[char])
                replaced_count += 1
            else:
                new_password += char
            char_index += 1
        if replaced_count >= 4:
            strong_passwords.append(new_password)
        else:
            weak_passwords.append(new_password)
        index += 1
    return {"Strong": strong_passwords, "Weak": weak_passwords}

def main():
    replacements = get_replacements()
    passwords = generate_passwords(5)
    classified_passwords = modify_and_classify(passwords, replacements)

    print("\nGenerated Passwords:")
    print("Strong Passwords:")
    i = 0
    while i < len(classified_passwords["Strong"]):
        print(classified_passwords["Strong"][i])
        i += 1
    print("Weak Passwords:")
    j = 0
    while j < len(classified_passwords["Weak"]):
        print(classified_passwords["Weak"][j])
        j += 1

if __name__ == "__main__":
    main()
