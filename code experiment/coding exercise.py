import function
import PySimpleGUI as sg
import time

sg.theme("black")
clock = sg.Text(" ", key='clock')
label1 = sg.Text("type a text:")
input1 = sg.Input(tooltip='enter text', key='text')
button1 = sg.Button('Add', font=10)
edit_button = sg.Button("Edit")
list_box = sg.Listbox(values=function.python_project(),key= 'texts',enable_events=True,
                      size=[55,12])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button('Exit')

window = sg.Window("My Text App", layout=[[clock], [label1, input1, button1],
                   [list_box, edit_button, complete_button],
                    [exit_button]], font=(20))

while True:
    event, values = window.read(timeout=100)
    window['clock'].update(value= time.strftime("%b %d ,%Y   %H:%M:%S"))
    match event:
        case'Add':
            try:
                todo = function.python_project()
                new_todo = values['text'] + '\n'
                todo.append(new_todo)
                function.write_todos(todo)
                window['texts'].update(values=todo)
            except TypeError:
                sg.popup("please select the item first.", font=('classic',20))
        case'Edit':
            try:
                todo_to_edit = values['texts'][0]
                new_todo = values['text']

                todo = function.python_project()
                index = todo.index(todo_to_edit)
                todo[index] = new_todo
                function.write_todos(todo)
                window['texts'].update(values=todo)
            except IndexError:
                sg.popup("please select the item first.", font=('classic', 10))
        case 'Complete':
            try:
                remove_to_todo = values['texts'][0]
                todo = function.python_project()
                todo.remove(remove_to_todo)
                function.write_todos(todo)
                window['texts'].update(values=todo)
                window['text'].update(value='')
            except IndexError:
                sg.popup("please select the item first.", font=('classic', 12))

        case 'texts':
            window['text'].update(value=values['texts'][0])
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break

window.close()