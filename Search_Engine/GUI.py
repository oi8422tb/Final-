import PySimpleGUI as sg


class window():

    def __init__(self,w,h):
#This is the layout of the window
        self.layout = [ [sg.Text('Enter Some Text Here')],
                                [sg.InputText()], 
                                [sg.Button('Search'), sg.Button('Random Search')] ]
                
        self.window = sg.Window('Easy Search Bar', self.layout)
                
        self.width = w
        self.height = h
      
