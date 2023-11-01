#module
import base64
import pyperclip

#print
print("엔터 누를시 자동으로 클립보드 데이터 디코드후 복사")
print("인코드 데이터 복사후 엔터 누를시 자동으로 인코드 후 복사")
print("혹은 e 입력시 자동으로 클립보드 데이터 인코드후 복사")

#decode
while True :
    _encode_=input(">>>")

    #decode clipboard
    if _encode_=='' :
        str = pyperclip.paste()
        bytes = str.encode('ascii')
        result = base64.b64decode(bytes)
        result_str = result.decode('UTF-8')

    #encode
    elif _encode_=='e':
        str = pyperclip.paste()
        bytes = str.encode('UTF-8')
        result = base64.b64encode(bytes)
        result_str = result.decode('ascii')

    #encode_2
    else :
        str=_encode_
        bytes = str.encode('UTF-8')
        result = base64.b64encode(bytes)
        result_str = result.decode('ascii')

    #copy & print the result_str
    pyperclip.copy(result_str)
    print(result_str)
    print("is copied.")
