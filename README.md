Instructions for convert from .py to .exe

pyinstaller --onefile --noconsole --add-data "image/scrr.png;img" --add-data "image/top.png;img" --add-data "image/doc.png;img" --add-data "image/task.png;img" --add-data "image/trash.png;img" --add-data "image;image" --hidden-import=tkinter --hidden-import=os --hidden-import=sys todo.py
