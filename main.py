while True:
    useraction = input("type add, show, edit, complete or exit:")
    useraction = useraction.strip()

    match useraction:
        case 'add':
            test = input("what happend :") + '\n'

            with open("D:\python file\members.txt",'r') as file:
                text = file.readlines()

            text.append(test)

            with open("D:\python file\members.txt",'w') as file:
                file.writelines(text)


        case 'show' | "display":
            with open("D:\python file\members.txt",'r') as file:
                text = file.readlines()

            # new_text = [item.strip('\n') for item in text]  (known as list comphrension.)
            for index, item in enumerate(text):
                item = item.strip("\n")
                row = f"{index+1}-:){item}"
                print(row)
        case 'edit':
            number = int(input("no of replacing item:"))
            number = number - 1

            with open("D:\python file\members.txt",'r')as file:
                file.readlines()

            new_text = input("replacing item:")
            text[number] = new_text + '\n'

            with open("D:\python file\members.txt",'w')as file:
                file.writelines(text)

        case "complete":
            number = int(input("no. of the text to complete"))

            with open("D:\python file\members.txt",'r')as file:
                file.readlines()

            index = number - 1
            text_was_removed = text[index].strip('\n')
            text.pop(index)

            with open("D:\python file\members.txt",'w')as file:
                file.writelines(text)

            message = (f"{text_was_removed}was removed from list.")
            print(message)
        case 'exit':
            break
print("Bye!")



