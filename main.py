'''
     _/\/\/\/\/\/\_     _/\/\/\/\/\/\_     _/\/\/\/\/\___     ___/\/\/\/\/\_     ___/\/\/\/\___     _____/\/\/\___
    _/\___________     _______/\/\___     _/\/\____/\/\_     _/\/\_________     _/\/\_________     ___/\/\/\/\___
   _/\/\/\/\/\___     _____/\/\_____     _/\/\/\/\/\___     ___/\/\/\/\___     _/\/\/\/\/\___     _/\/\__/\/\___
  _/\/\_________     ___/\/\_______     _/\/\____/\/\_     _________/\/\_     _/\/\____/\/\_     _/\/\/\/\/\/\_
 _/\/\/\/\/\/\_     _/\/\/\/\/\/\_     _/\/\/\/\/\___     _/\/\/\/\/\___     ___/\/\/\/\___     _______/\/\___
______________     ______________     ______________     ______________     ______________     ______________
ezbs64 v1.2.231107
'''

# module
import base64
import pyperclip
import binascii
import keyboard
from time import *
import tkinter as tk
from infi.systray import SysTrayIcon

# variable
sendc = 0
sendbreak = 0
autocopy = 1
hook_n = 1
_input_ = ''


# function

#tkinter UI function
def execute_command():
    global str
    command = input_entry.get()
    input_entry.delete(0, tk.END)  #reset input
    output.see(tk.END)

    if command == '':
        str = pyperclip.paste()
        __decodef__()
        __copyf__()
    elif command =='//e':
        str = pyperclip.paste()
        __encodef__()
        __copyf__()
    else:
        str = command
        __encodef__()
        __copyf__()

#kill key
def disable_input(event):
    return "break"

#infi.systray
def on_quit_callback(systray):
    root.quit()

def on_show(systray):
    root.deiconify()

def on_close():
    root.withdraw()
    systray.update(icon="ezbs64.ico", hover_text="ezbs64.exe")

# en & de code
def __encodef__():  # encode
    global result_str
    try:
        bytes = str.encode('UTF-8')
        result = base64.b64encode(bytes)
        result_str = result.decode('ascii')
    except binascii.Error:
        pass
    except UnicodeDecodeError:
        pass

def __decodef__():  # decode
    global sendc, result_str
    try:
        bytes = str.encode('UTF-8')
        result = base64.b64decode(bytes)
        result_str = result.decode('ascii')
    except binascii.Error:
        pass
    except UnicodeDecodeError:
        pass

def __keydecodef__():  # auto decode
    sleep(0.1)
    global sendc, result_str
    try:
        str = pyperclip.paste()
        bytes = str.encode('UTF-8')
        result = base64.b64decode(bytes)
        result_str = result.decode('ascii')
        pyperclip.copy(result_str)

        output.insert(tk.END,result_str+"\n")
        output.see(tk.END)

        output.insert(tk.END,"is copied.\n")
        output.see(tk.END)

    except binascii.Error:
        pass
    except UnicodeDecodeError:
        pass

# add & del key
def __delkey__():
    keyboard.remove_hotkey('ctrl + c')

def __addkey__():
    keyboard.add_hotkey('ctrl + c', __keydecodef__)

# detect
def __decodedetect__():
    global sendc, hook_n
    hook_n += 1
    # off
    if hook_n % 2 == 0:
        keyboard.remove_hotkey('ctrl + c')
        output.insert(tk.END,"auto decode copy is off\n")
        output.see(tk.END)

    # on
    elif hook_n % 2 == 1:
        keyboard.add_hotkey('ctrl + c', __keydecodef__)
        output.insert(tk.END,"auto decode copy is on\n")
        output.see(tk.END)

# copy
def __copyf__():
    pyperclip.copy(result_str)

    output.insert(tk.END,result_str+"\n")
    output.see(tk.END)
    output.insert(tk.END,f"is copied.\n")
    output.see(tk.END)



#set UI
root = tk.Tk()
root.title("ezbs64.exe")
root.geometry("700x400")
root.resizable(False, False)
root.protocol('WM_DELETE_WINDOW', on_close)
menu_options = (("Show", None, on_show),)
systray = SysTrayIcon("ezbs64.ico", "ezbs64.exe", menu_options, on_quit=on_quit_callback)

#make output
output = tk.Text(root, width=100, height=29, wrap=tk.WORD,bg='black',fg='green')
output.pack()
output.bind('<Key>', disable_input)  #key binding

#make input
input_entry = tk.Entry(root, width=100,bg='black',fg='white',font=12)
input_entry.pack()
input_entry.bind('<Return>', lambda event: execute_command())  #key binding

# key
keyboard.add_hotkey('ctrl + c', __keydecodef__)
keyboard.add_hotkey('ctrl + alt', __decodedetect__)

# print
output.insert(tk.END,f"엔터 누를시 자동으로 클립보드 데이터 디코드후 복사\n")
output.insert(tk.END,f"인코드 데이터 복사후 엔터 누를시 자동으로 인코드 후 복사\n")
output.insert(tk.END,f"혹은 e 입력시 자동으로 클립보드 데이터 인코드후 복사\n")
output.insert(tk.END,f"auto decode copy is on\n")

#root
systray.start()
root.mainloop()