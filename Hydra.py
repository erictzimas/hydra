from tkinter import *
import librosa
import pyrubberband
import soundfile as sf
from PIL import ImageTk,Image  




def clicked():
   
    path1 = te.get()
    path2 = te2.get()
    incr = float(te3.get())
    
    rubberband(incr,path1,path2)




def rubberband(incr, path1, path2):
    label1 = Label(w,text = "Loading..")
    label1.pack()
    y, sr = librosa.load(path1, sr=None)
    y_stretched = pyrubberband.time_stretch(y, sr, incr)
    sf.write(path2, y_stretched, sr, format='wav')
    label1.config(text = 'Done !')
root = Tk()
root.title('Hydra')
w = Frame(root)


# Make the root window always on top
root.attributes("-topmost", True)
# Turn off the window shadow
root.attributes("-transparent", True)



w.pack()
img = ImageTk.PhotoImage(Image.open("scroll2.png"))

button1 = Button(w,command = clicked,text = "Develop")
button1.config(width = 40, height = 5)
canvas = Canvas(w, width = 700, height = 300)
canvas.pack()  
canvas.create_image(240, 100, anchor=NW, image=img) 
te = Entry(w,text = "Enter .wav path", fg = "black")
te.insert(0,'Enter .wav path')
button1.config(bg='systemTransparent')
te2 = Entry(w,text = "Enter destination-path/name of new .wav")
te2.insert(0,'Enter destination of new wav')
te3 = Entry(w,text = "Enter new speed")
te3.insert(0,"Enter new speed")


button1.pack()
te.pack()
te2.pack()
te3.pack()
root.geometry("700x700")
root.resizable(False,False)

mainloop()