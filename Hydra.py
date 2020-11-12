from tkinter import *
import librosa
import pyrubberband
import soundfile as sf
from PIL import ImageTk,Image  



counter = 0
def clicked():

   try: 
    path1 = te.get()
    

    path2 = te2.get()

    incr = float(te3.get())

    rubberband(incr,path1,path2)
   except FileNotFoundError:
       s.config(text = "Enter .wav path, destination path and time scale 0.0 - 2.0.", fg= "red")
       
   except RuntimeError:
       s.config(text = "Enter .wav path, destination path and time scale 0.0 - 2.0.", fg= "red")
   except ValueError:
       s.config(text = "Enter .wav path, destination path and time scale 0.0 - 2.0.", fg= "red")

   
    
        
def rubberband(incr, path1, path2):
    
    y, sr = librosa.load(path1, sr=None)
    
    y_stretched = pyrubberband.time_stretch(y, sr, incr)
    sf.write(path2, y_stretched, sr, format='wav')
    label1 = Label(w,text = "Done !") 
    label1.pack()    
root = Tk()
root.title('Hydra')
root.geometry("700x700")
root.resizable(False,False)
w = Frame(root)
w.pack()
img = ImageTk.PhotoImage(Image.open("scroll2.png"))
photo=PhotoImage(file= r"download.png")
photoimage = photo.subsample(3,3)


button1 = Button(w,command = clicked,text = "Develop",image = photoimage, compound = CENTER)
button1.config(width = 240, height = 50)
canvas = Canvas(w, width = 600, height = 300)
canvas.pack()  
canvas.create_image(70, 100, anchor=NW, image=img) 
te = Entry(w,text = "Enter .wav path", fg = "black")
te.insert(0,'Enter .wav path')
te2 = Entry(w,text = "Enter destination-path/name of new .wav")
te2.insert(0,'Enter destination of new wav')
te3 = Entry(w,text = "Enter new speed")
te3.insert(0,"Enter new speed")
pp = Label(w,text = "")
s = Label(w, text = "")
s.pack()

button1.pack()
pp.pack()
te.pack()
te2.pack()
te3.pack()


mainloop()