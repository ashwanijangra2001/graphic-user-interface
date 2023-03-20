import PySimpleGUI as sg

label1 = sg.Text("select the compressed file:")
input1 = sg.Input(tooltip='choose file')
button1 = sg.FileBrowse("choose")

label2 = sg.Text("select the destination file:")
input2 = sg.Input(tooltip='destination file')
button2 = sg.FolderBrowse("choose")

compressor_button = sg.Button("compressor")

window = sg.Window('compressor',[[label1,input1,button1],
                                 [label2,input2,button2],
                                 [compressor_button]])

window.read()
window.close()