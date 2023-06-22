from tkinter import *
from PIL import Image, ImageTk
from tkinter.messagebox import *
# from tkinter.messagebox import showerror
from tkinter.ttk import Combobox
import googletrans
import speech_recognition as sp
import gtts
import playsound
root = Tk()
root.title('Speech To Text')
root.geometry('1080x600')
root.resizable(0,0)
root.configure(bg='#ccebff')


# icon
icon = Image.open('Logo.png')
logo = ImageTk.PhotoImage(icon)
root.iconphoto(False, logo)


def displayInstruction():
    showinfo("Instruction", "Noice adjuster takes 1 seconds to adjust the background noice after clicking on the speak button")
# After clicking on speak button noice adjuster takes few seconds, you need to wait for that after that you can record your voice for 4 seconds")
root.after(1000, displayInstruction)

def clearText():
    text_area.delete('1.0', 'end')
    text_area2.delete('1.0', 'end')

def checkforvoice():
    dynamicLabel.configure(text='Sorry, i cant able to speech this !', background='red')

def goBack():
    root.destroy()
    import temp

def copyText():
    text = text_area2.get('1.0', 'end-1c')
    root.clipboard_clear()
    root.clipboard_append(text)
    showinfo("Copy Text", "Text copied to clipboard")

def speechTest():
    try:
        selected_key = lang_box.get()
        selected_value = languages_support[selected_key]
        convertedText = text_area2.get('1.0', 'end-1c')
        print(convertedText)
        converted_aud = gtts.gTTS(convertedText, lang=selected_value)
        converted_aud.save("hehehe.mp3")
        playsound.playsound("hehehe.mp3")
    except Exception as ex:
        tempText = 'Select Language'
        getting_text_from_textarea1 = text_area.get('1.0', 'end-1c')
        if selected_key == tempText:
            showwarning("Warning", 'Langugage not selected, Please Choose a language first')
        elif selected_key != tempText and getting_text_from_textarea1 == '':
            showwarning("Warning", 'Text not found, Please speak text to translate')
        elif getting_text_from_textarea1 != '' and selected_key == tempText:
            showwarning("Warning", 'Langugage not selected, Please Choose a language first')
        else:
            # converted_aud = gtts.gTTS("Sorry i can't able to speech this ", lang="en")
            # converted_aud.save("hehehe.mp3")
            # playsound.playsound("hehehe.mp3")
            root.after(100, checkforvoice)



def speak_text():
    clearText()
    recognizer = sp.Recognizer()
    with sp.Microphone() as source:
        print("Adjusting noise ")        
        recognizer.adjust_for_ambient_noise(source, duration=1)        
        print("Recording for 4 seconds")
        recorded_audio = recognizer.listen(source, timeout=4)
        print("Done recording")

        try:
            text = recognizer.recognize_google(recorded_audio, language='en')
            print(text)
            text_area.insert(END, text)
        except Exception as e:
            showwarning("Warning", 'Recognizer failed to recognize your voice, please speak loudly !')
            return


# Select language to translate
        try:    
            selected_key = lang_box.get()
            selected_value = languages_support[selected_key]
            # print(f'Selected key: {selected_key}, Selected value: {selected_value}')

            translator = googletrans.Translator()
            translation = translator.translate(text,dest=selected_value)
            print(translation.text)
            text_area2.insert(END, translation.text)
        except Exception as e:
            showwarning("Warning", 'Langugage not selected, Please Choose a language first')
# Top frame
top_frame = Frame(root,bg='#33385c', width=330, height=30)
top_frame.place(x=750, y = 0)

# Back button
# back_button = Button(root,text ='Back', bg= 'red', fg='#fff', font='Arial 10 bold', padx=14, command=goBack)
back_button = Button(root,text ='Back', bg= 'red', fg='#fff', activebackground='#33385c',activeforeground='#fff', font='Arial 10 bold', padx=14, command=goBack)
back_button.place(x = 30, y = 1)

# Middle frame
middle_frame = Frame(root, highlightbackground='#33385c',highlightthickness=3,bg='#ccebff', width=1020, height=540)
middle2_frame = Frame(root, bg='#33385c', width=30, height=540)

middle_frame.place(x=30,y=30)
middle2_frame.place(x=1050, y = 30)

# Main Heading
heading_1 = Label(middle_frame, text='Speech To Text', bg = 'red', fg='#fff', font='Arial, 25 bold', padx=20)
heading_1.place(x = 350, y = 15)


# lang_box = Combobox(middle_frame, text='Select Language', values=['afrikaans','albanian','amharic','arabic','armenian','azerbaijani','basque','belarusian','bengali','bosnian','bulgarian','catalan','cebuano', 'chichewa','chinese (simplified)','chinese (traditional)','corsican', 'croatian', 'czech','danish',  'dutch', 'english', 'esperanto', 'estonian', 'filipino', 'finnish', 'french','frisian', 'galician', 'georgian',  'german',  'greek',  'gujarati',  'haitian creole',  'hausa', 'hawaiian', 'hebrew', 'hebrew','hindi', 'hmong', 'hungarian',  'icelandic',  'igbo',  'indonesian', 'irish', 'italian',  'japanese', 'javanese', 'kannada', 'kazakh',  'khmer',  'korean',  'kurdish (kurmanji)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy', 'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)', 'nepali', 'norwegian', 'odia', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala',  'slovak', 'slovenian', 'somali', 'spanish', 'sundanese',  'swahili', 'swedish',  'tajik',  'tamil',  'telugu',  'thai',  'turkish',  'ukrainian', 'urdu','uyghur',  'uzbek', 'vietnamese','welsh', 'xhosa','yiddish','yoruba','zulu'], font='Arial 14 bold', state='r', width=15, background='#8162e2')
languages_support = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zn-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'iw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}
lang_box = Combobox(middle_frame, font='Arial 14', state='r', width=15,values=list(languages_support.keys()))
lang_box.set('Select Language')
# lang_box.bind('<<ComboboxSelected>>', getComboVal)

# lang_box.place(x=500, y = 93)
lang_box.place(x=650, y = 93)


# Speak Area
sub_heading1 = Label(middle_frame, text='Select language to translate', bg = '#8162e2', fg='#fff', font='Arial 16 bold', padx=20)
sub_heading1.place(x = 30, y = 90)
# speak button
speak = Button(middle_frame, text='Speak', bg = 'red', fg='#fff',activebackground='#33385c',activeforeground='#fff', font='Arial 14 bold', padx=16, command=speak_text)
# speak = Button(middle_frame, text='Speak', bg = 'red', fg='#fff',font='Arial 14 bold', padx=16, command=speak_text)
speak.place(x = 155, y = 150)

# Instruction button
instructionIcon = Image.open('Pic5.png')
inst = instructionIcon.resize((40,40))
myimg4 = ImageTk.PhotoImage(inst)
instruction = Button(middle_frame, image=myimg4, bg='#ccebff',bd=0,activebackground='#ccebff',command=displayInstruction)

instruction.place(x = 950, y= 20)


# Play sound
# play = Button(middle_frame, text='Play', bg = 'red', fg='#fff', font='Arial, 14 bold', padx=16,command=speechTest)
play = Button(middle_frame, text='Play', bg = 'red',activebackground='#33385c',activeforeground='#fff', fg='#fff', font='Arial, 14 bold', padx=16,command=speechTest)

play.place(x = 745, y = 150)

# Clear Text
clear = Button(middle_frame,text ='Clear All', activebackground='#33385c',activeforeground='#fff', bg= 'red', fg='#fff', font='Arial 14 bold', padx=16, command=clearText)
# clear = Button(middle_frame,text ='Clear All',bg= 'red', fg='#fff', font='Arial 14 bold', padx=16, command=clearText)
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
# text_area = Text(middle_frame, font='Arial 12', relief=GROOVE, wrap=WORD)
text_area.place(x= 30, y = 230, width=400, height=180)

# Converted text
# Text Area
# text_area2 = Text(middle_frame, font='Arial 12', relief=GROOVE, wrap=WORD)
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


# Note 
note = Label(middle_frame, text='Note * Recording support for 4 seconds only', bg = 'red', fg='#fff', font='Arial 10', padx=20)
note.place(x=30,y=505)

# Bottom frame
bottom_frame = Frame(root,bg='#33385c', width=330, height=30)
bottom_frame.place(x=750, y = 570)
root.mainloop()


