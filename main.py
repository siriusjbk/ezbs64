import base64
import pyperclip

#decode
print("엔터 누를시 자동으로 클립보드 데이터 디코드후 복사")
print("인코드 데이터 복사후 엔터 누를시 자동으로 인코드 후 복사")
print("혹은 e 입력시 자동으로 클리보드 데이터 인코드후 복사")
_encode_=input(">>>")

#decode clipboard
if _encode_=='' :
    code = pyperclip.paste()
    code_bytes = code.encode('ascii')

    decoded = base64.b64decode(code_bytes)
    str = decoded.decode('UTF-8')
    pyperclip.copy(str)
    print(str)
    print("가 복사 되었습니다.")
    input("아무키나 누르면 종료")

#encode
elif _encode_=='e':
    str = pyperclip.paste()
    bytes = str.encode('UTF-8')
    result = base64.b64encode(bytes)
    result_str = result.decode('ascii')
    pyperclip.copy(result_str)
    print(result_str)
    print("가 복사 되었습니다.")
    input("아무키나 누르면 종료")

else :
    str=_encode_
    bytes = str.encode('UTF-8')
    result = base64.b64encode(bytes)
    result_str = result.decode('ascii')
    pyperclip.copy(result_str)
    print(result_str)
    print("가 복사 되었습니다.")
    input("아무키나 누르면 종료")