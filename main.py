from customtkinter import *
import requests

root = CTk()
root.geometry('572x230')
root.resizable(False, False)
root.title('Clima')
root.iconbitmap('icone.ico')
root.configure(fg_color='#469899')


def pesquisar():
    cidade = str(entry_espaco.get())

    # Dados da API
    chave_api = '9f4e96f3c9540132014661a98fd6b21e'
    idioma_portugues = '&lang=pt_br'
    link_api = f'https://api.openweathermap.org/data/2.5/weather?' \
               f'q={cidade}&appid={chave_api}{idioma_portugues}'

    # Acessando a API
    clima_online = requests.get(f'{link_api}')
    clima_online.raise_for_status()

    # Convertendo a API em formato Python
    clima_online_dic = clima_online.json()

    temp = clima_online_dic['main']['temp'] - 273.15
    descricao = clima_online_dic['weather'][0]['description'].title()
    sensacao = clima_online_dic['main']['feels_like'] - 273.15
    temp_minima = clima_online_dic['main']['temp_min'] - 273.15
    temp_maxima = clima_online_dic['main']['temp_max'] - 273.15

    labeltemp = CTkLabel(root, text=f'{temp:.0f} °C', text_color='#105223',
                         font=('Arial', 18, 'bold'))
    labeltemp.place(x=60, y=120)

    label_descricao = CTkLabel(root, text=f'{descricao}', width=125,
                               text_color='#105223',
                               font=('Arial', 13, 'bold'))
    label_descricao.place(x=25, y=150)

    label_sens = CTkLabel(root, text=f'{sensacao:.0f} °C',
                          text_color='#105223',
                          font=('Arial', 18, 'bold'))
    label_sens.place(x=220, y=120)

    label_temp_minima = CTkLabel(root, text=f'{temp_minima:.0f} °C',
                                 font=('Arial', 18, 'bold'),
                                 text_color='#105223')
    label_temp_minima.place(x=360, y=120)

    label_temp_maxima = CTkLabel(root, text=f'{temp_maxima:.0f} °C',
                                 font=('Arial', 18, 'bold'),
                                 text_color='#105223')
    label_temp_maxima.place(x=484, y=120)


label_cidade = CTkLabel(root, text='Cidade', font=('Arial', 18, 'bold'))
label_cidade.place(x=30, y=20)

entry_espaco = CTkEntry(root, width=270, font=('Arial', 18, 'bold'),
                        text_color='#105223',
                        fg_color='#469899', corner_radius=10,
                        border_color='white', border_width=1,
                        justify='center')
entry_espaco.place(x=110, y=20)

button_pesquisar = CTkButton(root, text='Pesquisar', fg_color='#397C7D',
                             hover_color='#429191', border_color='white',
                             font=('Arial', 18, 'bold'), corner_radius=10,
                             border_width=1,
                             command=pesquisar)
button_pesquisar.place(x=402, y=20)

label_temperatura = CTkLabel(root, text='Temperatura',
                             font=('Arial', 18, 'bold'))
label_temperatura.place(x=30, y=80)

label_sensacao = CTkLabel(root, text='Sensação', font=('Arial', 18, 'bold'))
label_sensacao.place(x=200, y=80)

label_minima = CTkLabel(root, text='Mínima', font=('Arial', 18, 'bold'))
label_minima.place(x=350, y=80)

label_maxima = CTkLabel(root, text='Máxima', font=('Arial', 18, 'bold'))
label_maxima.place(x=470, y=80)

root.mainloop()
