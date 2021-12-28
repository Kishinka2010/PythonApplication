import PySimpleGUI as sg
sg.theme('LightGrey2')
layout = [
 [sg.Text('Создать новый аккаунт',size=(30,1),font=("Helvetica", 20),justification='center'),
],
[sg.Text('Это бесплатно - и всегда так будет.',size=(30,1),font=("Helvetica", 20),justification='center'),
],
[sg.Text('Имя'), sg.InputText(size=(12,1)), sg.Text('Фамилия '), sg.InputText(size=(12,1))
],
[sg.Text('Номер телефона'), sg.InputText(),
],
[sg.Text('Новый пароль '), sg.InputText(),
],
[sg.Text('Дата рождения',size=(60,1),justification='center'),
],
[sg.Text('День'),sg.Combo([1,2,3,4,5,6,7,8], size=(12,1)),sg.Text('Месяц'),sg.Combo(['январь','февраль','март','апрель','май'],
size=(12,1)),sg.Text('Год'),sg.Combo([2000,2001,2002,2003,2004], size=(12,1)),
],
[sg.Radio('мужчина', "RADIO1", default=False),sg.Radio('женщина', "RADIO1", default=True)],
[sg.Submit(), sg.Cancel()]
]
window = sg.Window('Авторизация', layout)
event, values = window.read()
window.close()

text_input =[ values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7]]
sg.popup('Ваши данные', text_input)
with open('data.txt', 'w') as f:
 for listitem in text_input:
  f.writelines('%s\n' % listitem)

