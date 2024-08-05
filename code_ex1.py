

## Coding EX1
# while True:
#     enter_user = input("Would you like to enter a new member? ")
#     enter_user.lower().strip()

#     match enter_user:
#         case "true"| "yes" | "y":
#             member = input("Enter new member: ") + "\n"
#             member.title()
#             file = open("text_files/members.txt", "r")
#             members = file.readlines()

#             members.append(member)

#             file = open("text_files/members.txt", "w")
#             file.writelines(members)
#             file.close()
#         case _:
#             break


## transforming strings
# filenames = ["1.doc", "1.report","1.presentation"]
# filenames = [filename.replace('.','-') + '.txt' for filename in filenames]
# print(filenames)

## Coding EX2
# password = input("Enter new password: ")
# result = {}

# if len(password) >= 8:
#     result["length"] = True
# else:
#     result["length"] = False

# digit = False
# for i in password:
#     if i.isdigit():
#         digit = True
# result["digits"] = digit

# uppercase = False
# for i in password:
#     if i.isupper():
#         uppercase = True
# result["upper-case"] = uppercase

# if all(result.values()):
#     print("Strong Password")
# else:
#     print("Weak Password")

# print(result)

## Coding EX3
# try:
#     width = float(input("Enter rectangle width: "))
#     length = float(input("Enter rectangle length: "))

#     if width == length:
#         exit("That looks like a square")
#     area = width + length
#     print(area)
# except ValueError:
#     print("Please enter a number in digit form.")


## Coding EX4
def get_average():
    total = 0
    with open('text_files/data.txt', "r") as file:
        data = file.readlines()
    temps = data[1:]
    temps = [float(temp) for temp in temps]
    
average = get_average()
print(average)