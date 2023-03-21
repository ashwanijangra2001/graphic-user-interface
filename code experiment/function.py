def python_project(filepath= "D:\python file\members.txt"):
    """read the file and return the list of present data """
    with open(filepath, 'r')as file:
        text = file.readlines()
    return text


def write_todos(text, filepath= "D:\python file\members.txt"):
    with open(filepath, "w") as file:
        file.writelines(text)


if __name__ == "__name__":
    print("hello")
    print(python_project())
