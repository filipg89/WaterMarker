import tkinter.messagebox
import traceback
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


class App:
    def __init__(self, master):
        master.report_callback_exception = self.report_callback_exception
        self.frame = Frame(master)
        self.frame.grid()

    def cause_exception(self):
        a = []
        a.a = 0 #A traceback makes this easy to catch and fix

    def report_callback_exception(self, *args):
        err = "One or both files aren't uploaded"
        tkinter.messagebox.showerror('Exception', err)


def add_watermark(img1, img2):
    img1.paste(img2, (int((img1.size[0]-img2.size[0])/2), int((img1.size[1]-img2.size[0])/2)), img2)
    progress_label = Label(mainframe, text='Complete!', fg='green', font=label_font, width=20, bg='white')
    progress_label.grid(row=8)
    run_button.config(text='Save image', command=lambda: img1.save(save_file()), bg='green')


def save_file():
    files = [('Jpg Files', '*.jpg'), ('PNG Files', '*.png')]
    filename = filedialog.asksaveasfile(defaultextension=".*", filetypes=files)
    return filename.name


def upload_image():
    global img
    f_types = [('All files', '*.*'), ('Jpg Files', '*.jpg'), ('Png Files', '*.png')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = Image.open(filename)
    return img


def upload_watermark():
    global watermark
    f_types = [('Png Files', '*.png')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    watermark = Image.open(filename)
    return watermark


tk = Tk()
app = App(tk)
tk.title("WaterMarker")
tk.config(background="#fff")
tk.geometry('300x400-800+90')

mainframe = Frame(tk, bg='white')
mainframe.grid()

logo = ImageTk.PhotoImage(Image.open('watermarker.png'))
label_font = ('calibri', 14, 'normal')
button_font = ('calibri', 11, 'bold')
logo_label = Label(mainframe, image=logo, highlightthickness=0, borderwidth=0)
logo_label.grid(row=1)
image_label = Label(mainframe, text='Select an image to watermark:', width=30, font=label_font, bg='white')
image_label.grid(row=2)
image_button = Button(mainframe, text='Upload', width=20, command=lambda: upload_image(),
                      font=button_font, bg='blue', fg='white')
image_button.grid(row=3, pady=(0, 30))
watermark_label = Label(mainframe, text='Select watermark image:', width=30, font=label_font, bg='white')
watermark_label.grid(row=4)
watermark_button = Button(mainframe, text='Upload', width=20, command=lambda: upload_watermark(),
                          font=button_font, bg='blue', fg='white')
watermark_button.grid(row=5)
run_button = Button(mainframe, text='Run!', width=20, font=button_font,
                    command=lambda: add_watermark(img, watermark), bg='blue', fg='white')
run_button.grid(row=7, pady=(50, 10))

tk.mainloop()
