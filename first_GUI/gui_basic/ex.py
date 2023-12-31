"""
tkinter를 이용한 메모장 프로그램을 만드시오

[GUI 조건]
title : 제목 없음 - windows 메모장 x 
메뉴 : 파일, 편집, 서식, 보기 도움말 
실제 메뉴 구현 : 파일 메뉴 내에서 열어서 보여주기
열기 : mynote.txt 파일 내용 열어서 보여주기
저장 : mynote.txt. 파일에 현재 내용 저장하기
끝내기 : 프로그램 종료
프로그램 시작 시 본문은 비어 있는 상태
하단 status 바는 필요 없음
프로그램 크기, 위치는 자유롭게 하되 크기 조정 가능해야 함 x 
본문 우측에 상하 스크롤 바 넣기
"""
import os
from tkinter import *

root = Tk()
root.title("제목 없음 - windows 메모장")
root.geometry("640x480")

# 열기, 저장 파일 이름
filename = "mynote.txt"

def open_file():
    if os.path.isfile(filename):    # 파일 있으면 True, 없으면 False
        with open(filename, 'r', encoding="utf-8") as file:
            txt.delete("1.0", END)          # 텍스트 위젯 본문 삭제
            txt.insert(END, file.read())    # 파일 내용을 본문에 입력

def  save_file():
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(txt.get("1.0", END))     # 모든 내용을 가져와서 사용

menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command = open_file)
menu_file.add_command(label="저장", command = save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)

# 편집, 서식, 보기 도움말 
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

# 스크롤 바
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# 본문 영역
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)


scrollbar.config(command=txt.yview)
root.config(menu=menu)
root.mainloop()
