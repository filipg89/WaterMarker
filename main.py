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
        a.a = 0

    def report_callback_exception(self, *args):
        err = "One or both files aren't uploaded"
        tkinter.messagebox.showerror('Error', err)


def add_watermark(v, img1, img2):
    if v.get() == "topleft":
        img1.paste(img2, (0, 0), img2)
    elif v.get() == "topright":
        img1.paste(img2, (img1.size[0]-img2.size[0], 0), img2)
    elif v.get() == "center":
        img1.paste(img2, (int((img1.size[0] - img2.size[0]) / 2), int((img1.size[1] - img2.size[0]) / 2)), img2)
    elif v.get() == "bottomleft":
        img1.paste(img2, (0, int(img1.size[1] - img2.size[1])), img2)
    elif v.get() == "bottomright":
        img1.paste(img2, (img1.size[0]-img2.size[0], int(img1.size[1] - img2.size[1])), img2)
    progress_label = Label(mainframe, text='Complete!', fg='green', font=label_font, width=20, bg='white')
    progress_label.grid(row=11, sticky=S)
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
    run_button.config(text='Run!', command=lambda: add_watermark(position, img, watermark), bg='blue')
    return img


def upload_watermark():
    global watermark
    f_types = [('Png Files', '*.png')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    watermark = Image.open(filename)
    run_button.config(text='Run!', command=lambda: add_watermark(position, img, watermark), bg='blue')
    return watermark


tk = Tk()
app = App(tk)
tk.title("WaterMarker")
tk.config(background="#fff")
tk.geometry('360x550-800+90')

mainframe = Frame(tk, bg='white', padx=30)
mainframe.grid()

logo = ImageTk.PhotoImage(Image.open('watermarker.png'))
label_font = ('calibri', 14, 'normal')
button_font = ('calibri', 11, 'bold')
logo_label = Label(mainframe, image=logo, highlightthickness=0, borderwidth=0)
logo_label.grid(row=0, sticky=S)
image_label = Label(mainframe, text='Select an image to watermark:', width=30, font=label_font, bg='white')
image_label.grid(row=1, sticky=S)
image_button = Button(mainframe, text='Upload', width=20, command=lambda: upload_image(),
                      font=button_font, bg='blue', fg='white')
image_button.grid(row=2, sticky=S, pady=(0, 30))
watermark_label = Label(mainframe, text='Select watermark image:', width=30, font=label_font, bg='white')
watermark_label.grid(row=3, sticky=S)
watermark_button = Button(mainframe, text='Upload', width=20, command=lambda: upload_watermark(),
                          font=button_font, bg='blue', fg='white')
watermark_button.grid(row=4, sticky=S)
position = StringVar(tk, "center")


radioFrame = Frame(mainframe, bg='white')
radioFrame.grid(column=0, row=5, pady=(30, 0))

topleft_radio = Radiobutton(radioFrame, text="Top left", variable=position, value="topleft", bg="white", font=button_font)
topleft_radio.grid(column=0, row=0, sticky=W)
topright_radio = Radiobutton(radioFrame, text="Top right", variable=position, value="topright", bg="white", font=button_font)
topright_radio.grid(column=2, row=0, sticky=W)
center_radio = Radiobutton(radioFrame, text="Center", variable=position, value="center", bg="white", font=button_font)
center_radio.grid(column=1, row=1, sticky=W)
bottomleft_radio = Radiobutton(radioFrame, text="Bottom left", variable=position, value="bottomleft", bg="white", font=button_font)
bottomleft_radio.grid(column=0, row=2, sticky=W)
bottomright_radio = Radiobutton(radioFrame, text="Bottom right", variable=position, value="bottomright", bg="white", font=button_font)
bottomright_radio.grid(column=2, row=2, sticky=W)

run_button = Button(mainframe, text='Run!', width=20, font=button_font,
                    command=lambda: add_watermark(position, img, watermark), bg='blue', fg='white')
run_button.grid(row=10, sticky=S, pady=(50, 10))

tk.mainloop()
