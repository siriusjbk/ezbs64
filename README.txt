
     _/\/\/\/\/\/\_     _/\/\/\/\/\/\_     _/\/\/\/\/\___     ___/\/\/\/\/\_     ___/\/\/\/\___     _____/\/\/\___
    _/\___________     _______/\/\___     _/\/\____/\/\_     _/\/\_________     _/\/\_________     ___/\/\/\/\___ 
   _/\/\/\/\/\___     _____/\/\_____     _/\/\/\/\/\___     ___/\/\/\/\___     _/\/\/\/\/\___     _/\/\__/\/\___  
  _/\/\_________     ___/\/\_______     _/\/\____/\/\_     _________/\/\_     _/\/\____/\/\_     _/\/\/\/\/\/\_   
 _/\/\/\/\/\/\_     _/\/\/\/\/\/\_     _/\/\/\/\/\___     _/\/\/\/\/\___     ___/\/\/\/\___     _______/\/\___    
______________     ______________     ______________     ______________     ______________     ______________     

# ezbs64
github
https://github.com/siriusjbk/ezbs64

version pack (버젼 업데이트 내용도 들어있음)
https://drive.google.com/drive/folders/1Y7gvNdpNJl7LIRB-Axb01sKaPcsviXl6?usp=drive_link

email:siriusjbk@gmail.com
version:1.2.231107

bs64 사용을 사이트에서 인코딩 디코딩 하는것 보다 빠르게 하기 위해 제작했음
귀찮아서 개빠르게 코딩한거라 문제 많음

#UI
윈도우창 하단의 인풋창에 문자열 입력가능
윈도우창 오른쪽 상단의 닫기버튼을 누를경우 자동으로 아이콘 숨기기 표시됨
끄는 방법은 숨겨진 아이콘 표시 아이콘을 누른 후 ezbs64.exe 를 우클릭 후 Quit 을 누르면됨
만약 다시 ezbs64창을 키고싶은 경우엔 숨겨진 아이콘 표시 아이콘 클릭후 ezbs64.exe를 우클릭, Show 버튼 혹은
숨겨진 아이콘 표시 아이콘 클릭후 ezbs64.exe를 더블클릭
#############################
버그 안내
ezbs64.exe를 우클릭후 Quit을 누르면 아이콘이 사라지지만 프로그램이 늦게 꺼지는
버그가 있음 이때 꺼진 상태에서 작업관리자를 통해 강제 작업 종료를 바람
#############################

#auto
ctrl + c 를 할경우 자동으로 클립보드의 데이터를 디코딩 한후 클립보드에 저장합니다.
#clipboard : dGVzdA==
#pause ctrl + c
test
is copied.
#clipboard : test

ctrl + alt 를 입력 할경우 자동 디코딩을 해제합니다 다시 ctrl + alt 를 입력할 경우 자동 디코딩을 작동시킵니다
#clipboard : test
#pasue ctrl + alt
auto copy is off
#pause ctrl + c : dGVzdA==
#clipboard : dGVzdA==


#manual
엔터만 누를시 클립보드 내용이 자동으로 디코딩 된후 결과값이 복사됩니다.
ex)
#clipboard : dGVzdA==
#pause enter
test
is copied.
#clipboard : test

인코딩할 데이터를 입력후 엔터를 누를경우 데이터를 인코딩 한후 
ex)
test
dGVzdA==
is copied.
#clipboard : dGVzdA==

'//e' 을 입력시에는 클립보드에 있는 데이터를 자동으로 인코딩 한후 결과값이 복사됩니다.
ex)
#clipboard : test
//e
dGVzdA==
is copied.
#clipboard : dGVzdA==
