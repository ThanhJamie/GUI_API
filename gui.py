from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog,Text

ws = Tk()
ws.title('Age PreDiction')
ws.geometry('700x700')
ws.config(bg='#4a7a8c')
# canvas = Canvas(ws)
# Resize image
def resize_func():
    fileName = openFile()
    image = Image.open(fileName)
    w = int(width.get())
    h = int(height.get())
    resize_img = image.resize((w, h))
    img = ImageTk.PhotoImage(resize_img)
    disp_img.config(image=img)
    disp_img.image = img

# Read Image
def openFile():
    fileName = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    return fileName

# fileName2 = openFile()
def predictAge():
    # mess = Message(text= "2333", bg="#263D42", fill = 'red')
    # mess.pack(side = BOTTOM)
    my_label_example = Label(ws, text=Predict(), foreground='RED')
    my_label_example.pack()

def Predict():
    ret


frame = Frame(ws)
frame.pack()

OpenFile = Button(
    frame,
    text='Open File',
    command=resize_func
)
OpenFile.pack(side=RIGHT,padx=10,pady=10)

Label(
    frame,
    text='Width'
    ).pack(side=LEFT)
width = Entry(frame, width=10)
width.insert(END, 300)
width.pack(side=LEFT)

Label(
    frame,
    text='Height'
    ).pack(side=LEFT)
height = Entry(frame, width=10)
height.insert(END, 350)
height.pack(side=LEFT)

# resize_btn = Button(
#     frame,
#     text='Resize',
#     command=resize_func
# )
# resize_btn.pack(side=LEFT)

disp_img = Label()
disp_img.pack(pady=20)

predictAge = Button(ws, text = "Predict Age", padx= 10,pady= 5,fg="white", bg="#263D42",command = predictAge)
predictAge.pack(side = BOTTOM)


ws.mainloop()