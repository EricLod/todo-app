import PySimpleGUI as sg

feet_label = sg.Text("Enter feet:")
feet_input = sg.InputText(tooltip="feet", key="feet")

inches_label = sg.Text("Enter inches:")
inches_input = sg.InputText(tooltip="inches", key="inches")

convert_button = sg.Button("Convert")
convert_label = sg.Text("", key="convert")

window = sg.Window("Convertor",
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [convert_button, convert_label]])

while True:
    event, values = window.read()

    feet = values["feet"]
    if feet == "":
        feet = 0
    else:
        feet = int(feet)

    inches = values["inches"]
    if inches == "":
        inches = 0
    else:
        inches = int(inches)

    output = feet*0.3048+inches*0.0254
    window["convert"].update(str(output) + "m")

window.close()