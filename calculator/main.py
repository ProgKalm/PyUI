"""
@name: PyCalculator
@author: Suponev Ilia
@about: This demonstrates simple calculator by python3.tkinter
@realise-version: 1.0
@build-version: 0.5
"""
from tkinter import *
import math
import keyboard

root = Tk()

size = (536, 493)
operation: str = None
buffer: str = None
DEBUG: bool = True

""" Main Window settings [added at version 0.1]"""
root.geometry(f"{size[0]}x{size[1]}+100+150")  # set window size as 300 by X, 500 by Y
root.resizable(False, False)  # removing the ability to change the size of the window by X and Y
root.title("PyCalculator")  # set window title name as 'PyCalculator'
root.iconbitmap('calculator.ico')  # set window icon as file 'calculator.ico'

"""Creating all containers for all objects on window [added at version 0.2, set version 0.3]"""
top_frame = Frame(root, bg="#ac045a")  # frame for contains main label
top_frame.pack(fill=X)  # frame filling window by X( or WIDTH)
btn_frame = Frame(root, bg="#c78deb")  # frame for contains all label
btn_frame.pack(fill=X)

""" Creating all buttons and labels for app [added at version 0.3, set version 0.4]"""
# 1) creating main label, it will contain the value of the expression calculation
label = Label(top_frame, text='0', bg="#faeba7", fg="#050505",
              anchor=E, relief=RAISED, font=('Arial', 30, 'bold'), bd=5)
label.pack(side=TOP, fill=X)


# functions to working with label for all buttons at next.
def add_symbol(text: str) -> None:
    """
    Add to end of text value of text
    :param text: str type, contain value of clicked btn.
    :return: None
    """
    global buffer
    if label['text'] == 'Ошибка!':
        label['text'] = '0'

    if buffer is None and operation is not None:
        buffer = label['text']
        label['text'] = '0'
    if text in '1234567890':
        if label['text'] == '0':
            label['text'] = text
        else:
            label['text'] = label['text'] + text
    elif text == '.':
        if not ('.' in label['text']):
            print(label['text'])
            label['text'] = label['text'] + text
    else:
        exception()


def clear(text: str) -> None:
    """
    Clear label or all params of calculator
    :param text: str type, contain value of clicked btn.
    :return: None
    """
    global buffer, operation
    if text == 'cls':
        text = label['text'][:-1]
        if text == '':
            label['text'] = '0'
    elif text == 'del':
        label['text'] = '0'
        buffer = None
        operation = None
    else:
        exception()


def exception(msg: str = "Ошибка!") -> None:
    """
    Sending message about some exception for user, and clearing all
    :param msg: message about exception when app is working
    :return:
    """
    global buffer, operation
    label['text'] = msg
    buffer = None
    operation = None


def set_operation(text: str) -> None:
    global operation, buffer
    if text == '=':
        if buffer is None and operation is None:
            # Not doing anything
            pass
        elif buffer is None and operation is not None:
            # Invalid pushing, we will think that as also
            pass
        elif buffer is not None and operation is None:
            # Something not work, we set buffer, but not set operation
            exception()
        else:
            # buffer is not None and operation is not None
            try:
                if operation == 'sqrt' or operation == 'pow':
                    if operation == 'sqrt':
                        value = eval(f"math.pow({buffer}, 1 / {label['text']})")
                    else:
                        value = eval(f"math.pow({buffer}, {label['text']})")
                else:
                    value = eval(f"{buffer}{operation}{label['text']}")
                label['text'] = str(value)
            except Exception as ignored:
                exception()
            buffer = None
            operation = None
    else:
        operation = text


def program(text: str) -> None:
    text = text.lower()

    if DEBUG:
        print(f"buffer={buffer}\noperation={operation}\nlabel['text']={label['text']}\nenter={text}")
    if text in '1234567890.':
        add_symbol(text)
    elif text in ['+', '-', '/', '*', '=', 'sqrt', 'pow']:
        set_operation(text)
    elif text in ('cls', 'del'):
        clear(text)
    else:
        exception()
    print(f"result={label['text']}")
    print("\n=============\n")


def log(text: str):
    print(f"[LOG]: User click on button {text}.")


def set_btn_function(button: Button, message: str):
    message = message.lower()
    lmb = lambda x: eval(f'program("{message}")')
    button['command'] = lambda: eval(f'program("{message}")')

    if message in ['del', 'cls']:
        if message == 'del':
            keyboard.on_press_key('delete', lmb)
        else:
            keyboard.on_press_key('backspace', lmb)
    elif message == '=':
        keyboard.on_press_key('enter', lmb)
        keyboard.on_press_key('=', lmb)
    elif not (message in ['pow', 'sqrt']):
        keyboard.on_press_key(message, lmb)


# add buttons on 'btn_frame'
btns_names = ['1', '2', '3', '+',
              '4', '5', '6', '-',
              '7', '8', '9', '*',
              '.', '0', '=', '/',
              'del', 'cls', 'pow', 'sqrt']
for i in range(5):
    for j in range(0, 4):
        btn = Button(btn_frame, text=btns_names[i * 4 + j].upper(), bg='orange', fg='darkgrey',
                     relief=RAISED, font=('Arial', 30, 'bold'), bd=5)
        set_btn_function(btn, btns_names[i * 4 + j].upper())
        btn.grid(column=j, row=i, stick='wens')
        """ Add special functions for work by keyboard: User can writing numbers from keyboard 
                                    [added at version 0.4, set version 0.5]
        """

""" Running app [added at version 0.1, set version 0.2]"""
root.mainloop()
