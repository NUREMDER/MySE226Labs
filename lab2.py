
print('Scenario 3')
num = int(input("Please enter a number between [3-9]: "))

if num < 3 or num > 9:
    print("Wrong input!")
else:
    i = 1
    for star in " " * num:
        if i <= num:
            stars = ""
            for star in " " * i:
                stars += "*"
            print(stars)
            i += 1

    i = num - 1
    for star in " " * (num - 1):
        if i > 0:
            stars = ""
            for star in " " * i:
                stars += "*"
            print(stars)
            i -= 1
