from random import random, choice
import string
import PySimpleGUI as sg
import os

class PasswordGenerator:
    def __init__(self):
        #creating the layout
        sg.theme("Reddit")
        layout  = [
            [sg.Text('User', size=(10,1)), sg.Input(key='site', size= (20,1))],
            [sg.Text('Site/Software', size=(10,1)), sg.Input(key='user', size=(20,1))],
            [sg.Text('Characters', size=(10,1)), sg.Combo(values=list(range(16)), key='total_chars', default_value=1, size=(3,1))],
            [sg.Output(size=(33,5),)],
            [sg.Button('GENERATE')]
        ]
        #declaring window
        self.window = sg.Window('Password Generator', layout)
    
    def start(self):
        while True:
            event, values = self.window.read()
            if event == 'GENERATE':
                new_pass = self.generate_password(values)
                print(self.actual_password)

            if event == sg.WINDOW_CLOSED:
                break

    def generate_password(self, values):
        characters = string.ascii_letters + string.digits + string.punctuation
        self.actual_password = ''
        for i in range(values['total_chars']):
            self.actual_password += choice(characters)

    def save_password(self):
        pass
