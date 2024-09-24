import tkinter as tk
from tkinter import *
import sys
import os

# Получить доступ к папке, где находятся файлы
if getattr(sys, 'frozen', False):
    # Если запущена как .exe
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(__file__)

# Это base_path для доступа к изображениям
image_path = os.path.join(base_path, 'image')

# Основное окно
root = Tk()
root.title("ToDo 4U")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("tasklist.txt", 'a') as taskfile:
            taskfile.write(f"{task}\n")
        task_list.append(task)
        listbox.insert(END, task)

def deleteTask():
    global task_list
    try:
        task = str(listbox.get(ANCHOR))
        if task in task_list:
            task_list.remove(task)
            with open("tasklist.txt", 'w') as taskfile:
                for task in task_list:
                    taskfile.write(task + "\n")

            listbox.delete(ANCHOR)
    except IndexError:
        # Если ничего не выбрано, можно игнорировать
        pass

def openTaskFile():
    global task_list

    try:
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task.strip():  # Убираем пустые строки
                task_list.append(task.strip())
                listbox.insert(END, task.strip())
    except FileNotFoundError:
        # Создаем файл, если он не существует
        with open('tasklist.txt', 'w'):
            pass

# Функция для загрузки изображения
def load_image(filename):
    return PhotoImage(file=os.path.join(image_path, filename))

# Иконка
Image_icon = load_image('scrr.png')
root.iconphoto(False, Image_icon)

# Верхняя панель
TopImage = load_image('top.png')
Label(root, image=TopImage).pack()

dockImage = load_image('doc.png')
Label(root, image=dockImage, bg="#32405b").place(x=15, y=20)

noteImage = load_image('task.png')
Label(root, image=noteImage, bg="#32405b").place(x=320, y=20)

heading = Label(root, text="ALL TASK", font="arial 20 bold", fg="black", bg="white")
heading.place(x=130, y=35)

# Основной фрейм
frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=140)

task = StringVar()
task_entry = Entry(frame, width=18, font="arial 20", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

button = Button(frame, text="ADD", font="arial 20 bold", width=6, bg="grey", fg="#fff", bd=0, command=addTask)
button.place(x=300, y=0)

# Listbox
frame1 = Frame(root, bd=3, width=700, height=280, bg="grey")
frame1.pack(pady=(100, 0))

listbox = Listbox(frame1, font=('arial', 12), width=40, height=16, bg="white", fg="black", cursor="hand2", selectbackground="grey")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

# Удалить задачу
Delete_icon = load_image('trash.png')
Button(root, image=Delete_icon, bd=0, command=deleteTask).pack(side=BOTTOM, pady=13)

root.mainloop()