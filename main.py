import os
import tkinter as tk
import tkinter.filedialog
from PIL import Image, ImageTk

global on_hit  # 声明全局变量

window = tk.Tk()
window.title('Processor')  # 窗口的标题
window.geometry('500x400')  # 窗口的大小
default_dir = r"文件路径"

but1 = tk.Button(window, text='二值化', font='Helvetica -12 bold', width=6, height=1)
but1.place(relx=0.8, rely=25 / 400)
but2 = tk.Button(window, text='椒盐滤波器', font='Helvetica -12 bold', width=10, height=1)
but2.place(relx=0.8, rely=(25 + 93) / 400)
but3 = tk.Button(window, text='二值化', font='Helvetica -12 bold', width=6, height=1)
but3.place(relx=0.8, rely=(25 + 93 * 2) / 400)
but4 = tk.Button(window, text='二值化', font='Helvetica -12 bold', width=6, height=1)
but4.place(relx=0.8, rely=(25 + 93 * 3) / 400)

file_path = tk.filedialog.askopenfilename(title=u'选择图片',
                                          initialdir=(os.path.expanduser(default_dir))
                                          )
imagepath = Image.open(file_path)
img = ImageTk.PhotoImage(imagepath)
orgimg = tkinter.Label(window,
                       image=img
                       )
orgimg.place(relx=0.1, rely=25 / 400)

window.mainloop()
