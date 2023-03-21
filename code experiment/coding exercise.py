import function
import PySimpleGUI as sg

label1 = sg.Text("type a text:")
input1 = sg.Input(tooltip='enter text', key='text')
button1 = sg.Button('Add')
edit_button = sg.Button("Edit")
list_box = sg.Listbox(values=function.python_project(),key= 'texts',enable_events=True,
                      size=[55,12])
edit_button = sg.Button("Edit")

window = sg.Window("My Text App", layout=[[label1, input1, button1],
                   [list_box, edit_button]], font=(20))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['texts'])
    match event:
        case'Add':
            todo = function.python_project()
            new_todo = values['text'] + '\n'
            todo.append(new_todo)
            function.write_todos(todo)
            window['texts'].update(values['text'])
        case'Edit':
            todo_to_edit = values['texts'][0]
            new_todo = values['text']

            todo = function.python_project()
            index = todo.index(todo_to_edit)
            todo[index] = new_todo
            function.write_todos(todo)
            window['texts'].update(values= todo)
        case'texts':
            window['text'].update(value=values['texts'][0])
        case sg.WIN_CLOSED:
            break

window.close()