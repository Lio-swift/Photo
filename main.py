import os
import tkinter as tk
import tkinter.filedialog
from PIL import Image, ImageTk
import process
import cv2 as cv


window = tk.Tk()
window.title('Processor')  # 窗口的标题
window.geometry('500x400')  # 窗口的大小
default_dir = r"文件路径"

file_path = tk.filedialog.askopenfilename(title=u'选择图片',
                                          initialdir=(os.path.expanduser(default_dir))
                                          )
imagepath = Image.open(file_path)  # 原生io函数对图像文件的支持并不完善，用PIL打开原始图像并显示
Way = process.Pro(file_path)
print(file_path)


def binaryzation():
    Way.custom_threshold()
    img2 = ImageTk.PhotoImage(file='./binary.png')
    imgn = tkinter.Label(window,
                         image=img2,
                         width=100,
                         )
    imgn.place(relx=0.1, rely=0.5)
    window.mainloop()


def grey():
    img_g = cv.cvtColor(Way.o, cv.COLOR_RGB2GRAY)
    cv.imwrite("./grey.png", img_g)
    img2 = ImageTk.PhotoImage(file='./grey.png')
    imgn = tkinter.Label(window,
                         image=img2,
                         )
    imgn.place(relx=0.1, rely=0.5)
    window.mainloop()


def ok():
    print('ok')


def dither():
    Way.dithering()
    img2 = ImageTk.PhotoImage(file='./dither.png')
    imgn = tkinter.Label(window,
                         image=img2,
                         )
    imgn.place(relx=0.1, rely=0.5)
    window.mainloop()


# 窗口布局
but1 = tk.Button(window, text='二值化', font='Helvetica -12 bold', width=6, height=1, command=binaryzation)
but1.place(relx=0.8, rely=25 / 400)  # place方法的相对位置，取值（0，1）
but2 = tk.Button(window, text='4级灰度图', font='Helvetica -12 bold', width=11, height=1, command=grey)
but2.place(relx=0.77, rely=(25 + 93) / 400)
but3 = tk.Button(window, text='随机抖动', font='Helvetica -12 bold', width=11, height=1, command=dither)
but3.place(relx=0.77, rely=(25 + 93 * 2) / 400)
but4 = tk.Button(window, text='ok', font='Helvetica -12 bold', width=11, height=1, command=ok)
but4.place(relx=0.77, rely=(25 + 93 * 3) / 400)

orgimg = ImageTk.PhotoImage(imagepath)
img = tkinter.Label(window,
                    image=orgimg,
                    )
img.place(relx=0.1, rely=25 / 400)

window.mainloop()

