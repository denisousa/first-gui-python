import PySimpleGUI as sg


class Window():
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('Name', size=(5,0)), sg.Input(size=(15,0), key='name')],
            [sg.Text('Age', size=(5,0)), sg.Input(size=(15,0), key='age')],
            [sg.Text('Emails providers accept:')],
            [
                sg.Checkbox('Gmail', key='gmail'),
                sg.Checkbox('Hotmail', key='hotmail'),
                sg.Checkbox('Yahoo', key='yahoo'),
            ],
            [
                sg.Radio('Yes', 'cards', key='accept_card'),
                sg.Radio('no', 'cards', key='no_accept_card'),
            ],
            [
                sg.Slider(range=(0,200),
                          default_value=0,
                          orientation='h',
                          size=(15,20),
                          key='speed'),
        ],
            [sg.Button('Data Send')],
            [sg.Output(size=(30,20), key='output')],
        ]
        # Janela
        self.janela = sg.Window('User Data').layout(layout)

    def iniciar(self):
        while True:
            # Extrair dados da tela
            self.button, self.values = self.janela.Read()
            name = self.values['name']
            age = self.values['age']
            gmail = self.values['gmail']
            hotmail = self.values['hotmail']
            yahoo = self.values['yahoo']
            accept_card = self.values['accept_card']
            no_accept_card = self.values['no_accept_card']
            velocidade = self.values['speed']
            print(f'name: {name}')
            print(f'age: {age}')
            print(f'gmail: {gmail}')
            print(f'hotmail: {hotmail}')
            print(f'yahoo: {yahoo}')
            print(f'accept_card: {accept_card}')
            print(f'no_accept_card: {no_accept_card}')
            print(f'velocidade: {velocidade}')

tela = Window()
tela.iniciar()