

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
password = input("Enter new password: ")
result = []

if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

print(result)

