text = []

while True:
    user_action = input("type add, show or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            test = input("what happend")
            text.append(test)
        case "show":
            for item in text:
                item = item.title()
                print(item)
        case "exit":
            break
        case _:
            print("hey this command not find in this code ")

print("Bye!")

