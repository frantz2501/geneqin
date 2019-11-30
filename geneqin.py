import PySimpleGUI as sg

layout=[[sg.Text('Générateur de personnage')],[sg.Text('Nom', size=(15,1)),sg.InputText('nom')],
   [sg.Text('Métal', size=(5,1)), (sg.InputCombo(('1', '2', '3', '4', '5'), size=(2,1)))],
   [sg.Text('Eau', size=(5,1)), (sg.InputCombo(('1', '2', '3', '4', '5'), size=(2,1)))],
   [sg.Text('Bois', size=(5,1)), (sg.InputCombo(('1', '2', '3', '4', '5'), size=(2,1)))],
   [sg.Text('Feu', size=(5,1)), (sg.InputCombo(('1', '2', '3', '4', '5'), size=(2,1)))],
   [sg.Text('Terre', size=(5,1)), (sg.InputCombo(('1', '2', '3', '4', '5'), size=(2,1)))],
   [sg.Submit(), sg.Cancel()]]

window=sg.Window('Générateur de perso de Qin').Layout(layout)

button, values=window.Read()

sg.Popup(values)