---
title: "Process creation"
question: "프로은 어떻게 만들어지는가?"
status: hub
tags: ["os","process"]
updated: "2026-05-19"
published: false
publishedExcerpt: ""
---

개요: k8s를 공부하다가 kubectl도 프로그램이고, [[ls]]도 프로그램인걸 알았다(*Q:ls가 프로그램이면, ls또한 메모리 영역과 스택 큐를 가지는데 각각의 영역에 무엇이 들어갈까?*). 그래서 ls을 직접 만들면 어떻게 만들까를 고민하다가 C 컴파일이 안되는걸 발견했다. 원인은 PATH 관련 문제였다. 그럼 PATH는 왜 필요할까? [[프로세스]]가 메모리 스택 힙 만 필요하다면 그냥 윈도우(또는 리눅스)가 알아서 다 실행시켜주면 안되나? 그러면 지금까지 cmd에 python hello_world.py가 다른 의미가 있던 건가? 에서 나온 궁금증


일단 그러면 command란 무엇일까?
명령어다. 그러면 명령어라고 다 같은 명령어인가? 
CASE 1. A program
EX: git, python, gcc, ls
프로그램이기에 디스크에서 페이지들로 쪼개져서 존재한다.(플래시는 아닐수도) 그리고 이것이 프로세스로 바뀌려면 OS가 이걸 디스크에서 찾아와서 메모리 위에 얹어야 한다.

CASE 2. Shell built in commands
EX: cd, alias
shell 내부에 있다. (내부에 있다가 뭔지는 잘 모른다)

CASE 3. Shell functions
EX: alias k=kubectl
이것도 뭔지 모른다.

## CASE 1. 프로그램
python hello world을 cmd에 치면 어떻게 되는가? 
(이미지 넣기)
키보드에 치면 하드웨어 과정을 통해(*기억 안남, 추가 예정*)shell에 글자가 적히고, shell이 python.exe를 찾고 새로운 프로세스(run python.exe on memory with argument main.py)(*이때 parsing이 shell에서 일어나나?*)를 만든다. 그리고 이 프로세스는 argument hello_world.py로 동작한다. 그럼 shell이 어떻게 python.exe를 찾는가? 그건 환경변수에 path이 있어서 그렇다. 프언 과목에서 env variable들은 shadowing도 되고 update도 되던  key value 값들- line by line 실행할 때 그저 값들을 참고해오려고 만든 딕셔너리였다. 이것도 비슷한 것 같다.

그러면 마찬가지, ls은 아무렇지도 않게 궁금하면 ls을 치면 된다. 하지만 ls 또한 프로그램, 그렇다면 ls의 PATH 또한 저장되어 있는가? (*또 윈도우랑 ubuntu랑 ls는 차이가 있으며 윈도우는 컴파일된 .NET 코드로 되어있으며 어쩌고 저쩌고라는데 이건 범위 밖이니 생략*) 
그림 넣기

그렇다! exe 로 존재한다.

그러면 항상 겪는 command not found는 왜 일어나는가? 환경변수 딕셔너리에서 못찾았기 때문이다. 
(참고: 왜 항상 ./main으로 실행을 할까? ./는 현재 디렉토리를 뜻한다. 근데 사람이라면 당연히 여기서 작업하고 여기서 만들고 여기서 실행하지 않을까? 하지만 shell은 PATH 에서만 파일들을 검색하고 현재 디렉토리에서는 검색하지 않는다. 이러한 이유는 보안상 어떤 악의적인 사람이 현재 디렉토리에 컴퓨터를 없애는 main 프로그램을 넣었을 수 있는 가능성 때문이라는데, 그럴듯하지 않은가?) 






## Threads

- [[Why fork/exec felt unintuitive]]
- [[What survives across exec]]

## Still open

- How does Windows `CreateProcess` differ from Linux `fork` + `exec`?
- What is the parent process when Explorer starts Python?
