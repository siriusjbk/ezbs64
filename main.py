'''
     _/\/\/\/\/\/\_     _/\/\/\/\/\/\_     _/\/\/\/\/\___     ___/\/\/\/\/\_     ___/\/\/\/\___     _____/\/\/\___
    _/\___________     _______/\/\___     _/\/\____/\/\_     _/\/\_________     _/\/\_________     ___/\/\/\/\___ 
   _/\/\/\/\/\___     _____/\/\_____     _/\/\/\/\/\___     ___/\/\/\/\___     _/\/\/\/\/\___     _/\/\__/\/\___  
  _/\/\_________     ___/\/\_______     _/\/\____/\/\_     _________/\/\_     _/\/\____/\/\_     _/\/\/\/\/\/\_   
 _/\/\/\/\/\/\_     _/\/\/\/\/\/\_     _/\/\/\/\/\___     _/\/\/\/\/\___     ___/\/\/\/\___     _______/\/\___    
______________     ______________     ______________     ______________     ______________     ______________     
ezbs64 v.1.1
'''


#module
import base64
import pyperclip
import binascii
import keyboard
from time import *

#variable
sendc=0
sendbreak=0
autocopy=1
hook_n=1
_input_=''

#function

#en & de code
def __encodef__(): #encode
    global sendc,result_str
    try :
        bytes = str.encode('UTF-8')
        result = base64.b64encode(bytes)
        result_str = result.decode('ascii')
    except binascii.Error: sendc=1
    except UnicodeDecodeError:sendc = 1
        
def __decodef__(): #decode
    global sendc,result_str
    try :
        bytes = str.encode('UTF-8')
        result = base64.b64decode(bytes)
        result_str = result.decode('ascii')
    except binascii.Error : sendc=1
    except UnicodeDecodeError: sendc=1
        
def __keydecodef__(): #auto decode
    sleep(0.1)
    global sendc,result_str
    try :
        str = pyperclip.paste()
        bytes = str.encode('UTF-8')
        result = base64.b64decode(bytes)
        result_str = result.decode('ascii')
        pyperclip.copy(result_str)
        print(result_str)
        print("is copied.")
    except binascii.Error : pass
    except UnicodeDecodeError : pass


#add & del key
def __delkey__():
    keyboard.remove_hotkey('ctrl + c')
    
def __addkey__():
    keyboard.add_hotkey('ctrl + c', __keydecodef__)


#detect
def __decodedetect__():
    global sendc,hook_n
    hook_n+=1
    #off
    if hook_n%2==0:
        keyboard.remove_hotkey('ctrl + c')
        print("auto copy is off")
        sendc=1
    # on
    elif hook_n%2==1:
        keyboard.add_hotkey('ctrl + c', __keydecodef__)
        print("auto copy is on")
        sendc=1

#copy
def __copyf__():
    pyperclip.copy(result_str)
    print(result_str)
    print("is copied.")

#key
keyboard.add_hotkey('ctrl + c', __keydecodef__)
keyboard.add_hotkey('ctrl + alt',__decodedetect__)

#print
print("엔터 누를시 자동으로 클립보드 데이터 디코드후 복사")
print("인코드 데이터 복사후 엔터 누를시 자동으로 인코드 후 복사")
print("혹은 e 입력시 자동으로 클립보드 데이터 인코드후 복사")
print("auto copy is on")

#main
while True :
    if sendc==1: #send continue
        sendc=0
        continue
        
    _input_=input("") #input data

    #main
    if _input_=='//e':
        str = pyperclip.paste()
        __encodef__()
        __copyf__()
        if sendc==1:
            sendc=0
            continue

    #decode clipboard
    if _input_=='' :
        str = pyperclip.paste()
        __decodef__()
        __copyf__()
        if sendc==1:
            sendc = 0
            continue

    #encode_2
    else :
        str=_input_
        __encodef__()
        __copyf__()
        if sendc==1:
            sendc = 0
            continue
