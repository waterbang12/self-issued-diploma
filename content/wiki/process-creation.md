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





## Threads

- [[Why fork/exec felt unintuitive]]
- [[What survives across exec]]

## Still open

- How does Windows `CreateProcess` differ from Linux `fork` + `exec`?
- What is the parent process when Explorer starts Python?
