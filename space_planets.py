from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import ttk
import pickle
import cv2


root = Tk()
root.title("Space")
root.geometry("1300x900")

#preprocessing image
def preprocess(img):
    img = cv2.imread(str(img))
    img = cv2.resize(img, (85,85))
    img = img/255
    img = img.flatten()
    return img

#model prediction
def predict_img(img):
    planets = {
        0 : 'Earth',
        1 : 'Jupiter',
        2 : 'MakeMake',
        3 : 'Mars',
        4 : 'Mercury',
        5 : 'Moon',
        6 : 'Neptune',
        7 : 'Pluto',
        8 : 'Saturn',
        9 : 'Uranus',
        10 : 'Venus'
    }
    model_name = "trained_model.sav"
    loaded_model = pickle.load(open(model_name, 'rb'))
    predicted_label= loaded_model.predict([img])
    print(planets[predicted_label[0]])
    return planets[predicted_label[0]]

#defining opening function
def openimg():
    root.filename = filedialog.askopenfilename(initialdir="/This PC",
    title="Select a Photo", filetypes=(("png files", "*.png"), ("all files", "*.*")))
    img = root.filename

    # placce photo
    my_image = ImageTk.PhotoImage(Image.open((img)))
    my_lab = Label(image=my_image).place(x="500", y="100px")

    img = preprocess(img)
    pre_label = predict_img(img)
    print(root.filename)


    #place label
    my_canvas.create_text(650,90,text=pre_label,font=("Impact",25), fill="white")
    my_lab.pack()

#Image create
image = Image.open("back.jpg")
photo = ImageTk.PhotoImage(image)

#create canvas
my_canvas = Canvas(root, width=1300, height=900)
my_canvas.pack(fill="both", expand=True)

#set image to canvas
my_canvas.create_image(0,0,image=photo,anchor = "nw")

#create main generate button
button1 = Button(root,text="Upload Image to Classify", font=("Goudy old style", 15), command=openimg)
button1_window = my_canvas.create_window(550,30,anchor="nw",window=button1)

root.mainloop()