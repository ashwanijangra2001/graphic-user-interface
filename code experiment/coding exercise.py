import function
import PySimpleGUI as sg

label1 = sg.Text("type a text:")
input1 = sg.Input(tooltip='enter text', key='text')
button1 = sg.Button('add')

window = sg.Window("my text app", layout= [[label1,input1,button1]],font=15)

while True:
    item , value =  window.read()
    print(item)
    print(value)
    match item:
        case'add':
            todo = function.python_project()
            new_todo = value['text'] + '\n'
            todo.append(new_todo)
            function.write_todos(todo)
        case sg.WIN_CLOSED:
            break

window.close()