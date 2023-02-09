import PySimpleGUI as sg

level1 = sg.Text("Select File to Compress: ")
input1 = sg.Input(tooltip="Select File to Compress")
btn1 = sg.FilesBrowse("Choose")

level2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
btn2 = sg.FolderBrowse("Choose")

compress_btn = sg.Button("Compress")

window = sg.Window("File Compresser",layout = [[level1,input1,btn1],[level2,input2,btn2],[compress_btn]])
window.read()
window.close()