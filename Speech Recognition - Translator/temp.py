from tkinter import *
from PIL import Image, ImageTk
from tkinter.messagebox import showinfo
root = Tk()
root.title('Language Translator')
root.geometry('1080x600')
root.resizable(0,0)
root.configure(bg='#ccebff')
def speechToText():
    root.destroy()
    import SpeechToText

def textToSpeech():
    root.destroy()
    import TextToSpeech

#icon
icon = Image.open('Logo.png')
logo = ImageTk.PhotoImage(icon)
root.iconphoto(False, logo)

# Top frame
top_frame = Frame(root,bg='#33385c', width=330, height=30)
top_frame.place(x=750, y = 0)
# Middle frame
middle_frame = Frame(root, highlightbackground='#33385c',highlightthickness=3,bg='#ccebff', width=1020, height=540)
middle2_frame = Frame(root, bg='#33385c', width=30, height=540)

middle_frame.place(x=30,y=30)
middle2_frame.place(x=1050, y = 30)

# Main Poster
mainPoster = Image.open('Pic1.png')
main = mainPoster.resize((500,500))
myimg = ImageTk.PhotoImage(main)
Label(middle_frame, image=myimg, bg='#ccebff').place(x = 20, y= 0)

# Main Heading
heading_1 = Label(middle_frame, text='Language Translator', bg = 'red', fg='#fff', font='Arial, 25 bold', padx=20)
heading_1.place(x = 530, y = 50)
heading_2 = Label(middle_frame, text='Translate', bg = '#ccebff', fg='#33385c', font='Arial, 30 bold', padx=20)
heading_2.place(x=610, y=150)
heading_3 = Button(middle_frame, text='Speech To Text', bg = '#8162e2', fg='#fff', font='Arial, 18 bold', padx=30, activebackground='#33385c', activeforeground='#fff', command=speechToText)
heading_3.place(x=590, y=218)
heading_4 = Label(middle_frame, text='&', bg = '#ccebff', fg='#33385c', font='Arial, 30 bold')
heading_4.place(x=720, y=280)
heading_5 = Button(middle_frame, text='Text To Speech', bg = '#8162e2', fg='#fff', font='Arial, 18 bold', padx=30, activebackground='#33385c', activeforeground='#fff',command=textToSpeech)
heading_5.place(x=590, y=340)
# Bottom frame
bottom_frame = Frame(root,bg='#33385c', width=330, height=30)
bottom_frame.place(x=750, y = 570)
root.mainloop()

