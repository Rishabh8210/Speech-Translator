from tkinter import *
from PIL import Image, ImageTk
from tkinter.messagebox import *
from tkinter.ttk import Combobox
import googletrans
import speech_recognition as sp
import gtts
import playsound
root = Tk()
root.title('Text To Speech')
root.geometry('1080x600')
root.resizable(0,0)
root.configure(bg='#ccebff')

# icon
icon = Image.open('Logo.png')
logo = ImageTk.PhotoImage(icon)
root.iconphoto(False, logo)

def clearText():
    text_area.delete('1.0', 'end')
    text_area2.delete('1.0', 'end')
    play.place(x = 745, y = 150)
    dynamicLabel.configure(text='', background='#ccebff')
    lang_box.set('Select Language')


def checkforvoice():
    dynamicLabel.configure(text='Sorry, i cant able to speech this !', background='red')
    play.place_forget()

def goBack():
    root.destroy()
    import temp

def speechTest():
    selected_key = lang_box.get()
    tempText = 'Select Language'
    getting_text_from_textarea1 = text_area.get('1.0', 'end-1c')
    if(selected_key != tempText and getting_text_from_textarea1 != ''):
        playsound.playsound("audio.mp3")
    else:
        showwarning("Warning", 'Langugage not selected, Please Choose a language first')


def copyText():
    text = text_area2.get('1.0', 'end-1c')
    root.clipboard_clear()
    root.clipboard_append(text)
    showinfo("Copy Text", "Text copied to clipboard")

def speak_text():
    text = text_area.get('1.0', 'end-1c')
    print(text)
# Select language to translate
    try:    
        selected_key = lang_box.get()
        selected_value = languages_support[selected_key]
        translator = googletrans.Translator()
        translation = translator.translate(text,dest=selected_value)
        print(translation.text)
        text_area2.insert(END, translation.text)
        converted_aud = gtts.gTTS(translation.text, lang=selected_value)
        converted_aud.save("audio.mp3")
    except Exception as e:
        tempText = 'Select Language'
        getting_text_from_textarea1 = text_area.get('1.0', 'end-1c')
        if selected_key == tempText:
            showwarning("Warning", 'Langugage not selected, Please Choose a language first')
        elif selected_key != tempText and getting_text_from_textarea1 == '':
            showwarning("Warning", 'Text not found, Please speak text to translate')
        elif getting_text_from_textarea1 != '' and selected_key == tempText:
            showwarning("Warning", 'Langugage not selected, Please Choose a language first')
        else:
            checkforvoice()
# Top frame
top_frame = Frame(root,bg='#33385c', width=330, height=30)
top_frame.place(x=750, y = 0)

# Back button
back_button = Button(root,text ='Back', bg= 'red', fg='#fff', activebackground='#33385c',activeforeground='#fff', font='Arial 10 bold', padx=14, command=goBack)
back_button.place(x = 30, y = 1)

# Middle frame
middle_frame = Frame(root, highlightbackground='#33385c',highlightthickness=3,bg='#ccebff', width=1020, height=540)
middle2_frame = Frame(root, bg='#33385c', width=30, height=540)

middle_frame.place(x=30,y=30)
middle2_frame.place(x=1050, y = 30)

# convert button
speak = Button(middle_frame, text='Convert', bg = 'red', fg='#fff',activebackground='#33385c',activeforeground='#fff', font='Arial 14 bold', padx=16, command=speak_text)
# speak = Button(middle_frame, text='Speak', bg = 'red', fg='#fff',font='Arial 14 bold', padx=16, command=speak_text)
speak.place(x = 155, y = 150)
# Main Heading
heading_1 = Label(middle_frame, text='Text To Speech', bg = 'red', fg='#fff', font='Arial, 25 bold', padx=20)
heading_1.place(x = 350, y = 15)


# lang_box 
languages_support = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zn-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'iw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}
lang_box = Combobox(middle_frame, font='Arial 14', state='r', width=15,values=list(languages_support.keys()))
lang_box.set('Select Language')
lang_box.place(x=650, y = 93)


# Speak Area
sub_heading1 = Label(middle_frame, text='Select language to translate', bg = '#8162e2', fg='#fff', font='Arial 16 bold', padx=20)
sub_heading1.place(x = 30, y = 90)


# Play sound
play = Button(middle_frame, text='Play', bg = 'red',activebackground='#33385c',activeforeground='#fff', fg='#fff', font='Arial, 14 bold', padx=16,command=speechTest)

play.place(x = 745, y = 150)

# Clear Text
clear = Button(middle_frame,text ='Clear All', activebackground='#33385c',activeforeground='#fff', bg= 'red', fg='#fff', font='Arial 14 bold', padx=16, command=clearText)
clear.place(x=440, y = 150)

# Secondary Poster
secPoster = Image.open('Pic3.png')
sec = secPoster.resize((135,100))
myimg2 = ImageTk.PhotoImage(sec)
Label(middle_frame, image=myimg2, bg='#ccebff').place(x = 440, y= 230)

thrdPoster = Image.open('Pic4.png')
thrd = thrdPoster.resize((135,100))
myimg3 = ImageTk.PhotoImage(thrd)
Label(middle_frame, image=myimg3, bg='#ccebff').place(x = 440, y= 310)


# Text Area
text_area = Text(middle_frame, font='Arial 12', relief=GROOVE, wrap=WORD,background='#33385c', foreground='#fff')
text_area.place(x= 30, y = 230, width=400, height=180)

# Converted text area
text_area2 = Text(middle_frame, font='Arial 12', relief=GROOVE, wrap=WORD,background='#33385c', foreground='#fff')
text_area2.place(x= 590, y = 230, width=400, height=180)

# Copy button
Copybutton = Image.open('Pic6.png')
copyBtn = Copybutton.resize((20,20))
myimg5 = ImageTk.PhotoImage(copyBtn)
coptText = Button(middle_frame,image=myimg5,bg='#33385c',activebackground='#33385c',command=copyText)

coptText.place(x = 963, y= 205)

# Dynamic Label (for voice)
dynamicLabel = Label(middle_frame, text='', bg = '#ccebff', fg='#fff', font='Arial 10')
dynamicLabel.place(x=590,y=430)

# Bottom frame
bottom_frame = Frame(root,bg='#33385c', width=330, height=30)
bottom_frame.place(x=750, y = 570)
root.mainloop()
