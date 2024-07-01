


while True:
    enter_user = input("Would you like to enter a new member? ")
    enter_user.lower().strip()

    match enter_user:
        case "true"| "yes" | "y":
            member = input("Enter new member: ") + "\n"
            member.title()
            file = open("text_files/members.txt", "r")
            members = file.readlines()

            members.append(member)

            file = open("text_files/members.txt", "w")
            file.writelines(members)
            file.close()
        case _:
            break