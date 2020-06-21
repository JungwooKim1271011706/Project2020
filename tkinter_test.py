import tkinter
from tkinter import filedialog
import os

# def tkhandler():
#     window=tkinter.Tk()
#     window.title("문자 메시지 매니저")
#     window.geometry("640x400+100+100")
#     window.resizable(True, True)
#     label = tkinter.Label(window, text="안녕하세요")
#     label.pack()
#     window.mainloop()

filename = filedialog.askopenfilename()
print(filename)
