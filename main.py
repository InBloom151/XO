from tkinter import *
import random

root = Tk()
root.title('Criss-cross')
game_run = True
field = []
cross_count = 0
score_x = 0
score_o = 0


def new_game():
    for row in range(2, 5):
        for col in range(2, 5):
            field[row - 2][col - 2]['text'] = ' '
            field[row - 2][col - 2]['background'] = 'lavender'
    global game_run
    game_run = True
    global cross_count
    cross_count = 0


def click(row, col):
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        check_win('X')
        if game_run and cross_count < 5:
            computer_move()
            check_win('O')


def check_win(smb):
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2], smb)
        check_line(field[0][n], field[1][n], field[2][n], smb)
    check_line(field[0][0], field[1][1], field[2][2], smb)
    check_line(field[2][0], field[1][1], field[0][2], smb)


def check_line(a1, a2, a3, smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = 'pink'
        global game_run
        game_run = False
        if smb == 'O':
            global score_o
            score_o += 1
            global label_o
            label_o.config(text=f'O: {score_o}')
        elif smb == 'X':
            global score_x
            score_x += 1
            global label_x
            label_x.config(text=f'X: {score_x}')


def can_win(a1, a2, a3, smb):
    res = False
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
        a3['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
        a2['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
        a1['text'] = 'O'
        res = True
    return res


def computer_move():
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'O'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'O'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'O'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'O'):
        return
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'X'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'X'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'X'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'X'):
        return
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break


for row in range(2, 5):
    line = []
    for col in range(2, 5):
        button = Button(root, text=' ', width=4, height=2,
                        font=('Verdana', 20, 'bold'),
                        background='lavender',
                        command=lambda row=row, col=col: click(row - 2, col - 2))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
score_label = Label(text='СЧЕТ')
score_label.grid(row=0, column=0, columnspan=5, sticky='nsew')
label_x = Label(text=f'X: {score_x}', font='bold')
label_x.grid(row=1, column=2, sticky='nsew')
label_o = Label(text=f'O: {score_o}', font='bold')
label_o.grid(row=1, column=4, sticky='nsew')
new_button = Button(root, text='Начать заново', command=new_game)
new_button.grid(row=5, column=0, columnspan=5, sticky='nsew')
root.mainloop()
