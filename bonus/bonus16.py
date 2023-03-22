import PySimpleGUI as sg
from zipcreator import make_archive

label1 = sg.Text("select files to compress:")
input_box1 = sg.Input()
add_button1 = sg.FilesBrowse("choose", key='files')

label2 = sg.Text("select destination file :")
input_box2 = sg.Input()
add_button2 = sg.FolderBrowse("choose", key='folder')

compress_button = sg.Button("Compressor")
output_label = sg.Text(key='message')

window = sg.Window("Compressor App", layout=[[label1,input_box1, add_button1],
                                             [label2,input_box2,add_button2],
                                             [compress_button,output_label]],
                                              font=[45,10])

window.read()
while True:
    event , value = window.read()
    print(event, value)
    filepaths = value['files'].split(';')
    folder = value['folder']
    make_archive(filepaths, folder)
    window['message'].update(value= "compression is completed.")



window.close()

