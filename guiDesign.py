import tkinter as tk
from tkinter import ttk, RIGHT, Y, END, LEFT, BOTH
from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *
import pdfplumber
from extractionMethod import key_phrase_extraction

window = tk.Tk()
window.state("zoomed")

# the window fits the screen of the user window
width, height = window.winfo_screenwidth(), window.winfo_screenheight()
# window.geometry('%dx%d+0+0' % (width, height))
# window.geometry("200x150")
# window.attributes("-fullscreen", True)
# window.geometry('1010x1090+200+200')
# window.resizable(True, True)
# making background transparent
# window.attributes('-alpha', 0.94)

window_width = 900
window_height = 1000

# find the center point
center_x = int(width / 2 - window_width / 2)
center_y = int(height / 2 - window_height / 2)

# set the position of the window to the center of the screen
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# changing the icon by putting the path to the new icon
# window.iconbitmap(......)
window.title("Key phrase Extractor Glossary")
# window.rowconfigure(0, weight=2)
# window.columnconfigure(0, weight=2)
# window.columnconfigure(1, weight=1)


# window.columnconfigure(2, minsize=50, weight=1)

txt_edit = tk.Text(window, bd=8, width=100, height=150, wrap=WORD, relief="ridge")
txt_edit.pack()
txt_edit.grid(row=0, column=1, sticky=tk.NS, pady=0, padx=0)


# function to open and upload the pdf file soon after creating the app window
def upload_file():
    # capture the file path to use for key phrase extraction after its uploaded using a variable
    filetypes = [('Pdf files', '*.pdf'), ("All Files", "*.*")]
    filename = filedialog.askopenfilename(filetypes=filetypes)
    # ttk.Button(frm, text="Upload Pdf File", command=f).grid(column=1, row=0)
    # print(filename.title())  # printing file path required for extraction

    # extracting/mining all text information in the pdf to text
    all_text = ''
    with pdfplumber.open(filename.title()) as pdf:
        for pdf_page in pdf.pages:
            pdf_page_text = pdf_page.extract_text()
            # print(text)
            # case normalisation of text
            all_text += '\n' + pdf_page_text.lower()
    return all_text


# get text from the uploaded pdf doc
doc_text = upload_file()
print(doc_text)


# getting the extraction method from the gui input


# getting the number of key phrases from the gui input


# the get function for getting values/strings from gui input
def get(input_variable):
    print(input_variable.get())
    return input_variable.get()


# styling the frame
ttk.Style().configure('tab1.TFrame', background='black', foreground='blue')

# left hand side button frame
fr_buttons = ttk.Frame(window, style='tab1.TFrame', width=100, height=150, relief=tk.RIDGE, padding="0.5i")
# fr_buttons['padding'] = (55, 55, 55, 55)
fr_buttons.pack(expand=True, fill=BOTH)
fr_buttons.grid(row=0, column=0, sticky=tk.NS)

# styling all buttons
ttk.Style().configure("TButton", width=20, height=20, padding=6, relief="flat", background="#ccc")

# styling labels
label_style = ttk.Style()
label_style.configure('TLabel', relief="ridge", padx=5, pady=5)

#  styling option menu
menu_style = ttk.Style()
menu_style.configure('TMenubutton')

# styling the slider
slider_style = ttk.Style()
slider_style.configure('Horizontal.TScale')

# styling window

# styling text box
textbox_style = ttk.Style()
textbox_style.configure('TPanedwindow ', padding=0)

# left hand buttons and grid pos

paddings = {'padx': 5, 'pady': 5}

btn_upload = ttk.Button(fr_buttons, text="Upload file:", style='TButton', command=lambda: upload_file())
btn_upload.pack()
btn_upload.grid(row=0, column=0, sticky=tk.W, **paddings)

extraction_method_list = ["Algorithm1", "Algorithm2"]
var = StringVar(fr_buttons)
var.set(extraction_method_list[0])
option = ttk.OptionMenu(fr_buttons, var, *extraction_method_list)
# # # option.config(width=25)
option.pack()
var.trace("w", var.get())
ttk.Label(fr_buttons, text='Extraction method:').grid(row=3, column=0, sticky=tk.W)
option.grid(row=3, column=1, sticky=tk.E, padx=0, pady=50)

slider_label = ttk.Label(fr_buttons, text='key phrases number:')
slider_label.pack()
slider = ttk.Scale(fr_buttons, from_=0, to=20, orient='horizontal')
# slider.config(width=15,)
slider.set(10)
slider.pack()
slider_label.grid(row=6, column=0, sticky=tk.W, **paddings)
slider.grid(row=6, column=1, sticky=tk.E, **paddings)

#
btn_extract = ttk.Button(fr_buttons, text="Extract",
                         command=lambda: txt_edit.insert(tk.END, key_phrase_extraction(doc_text, get(var), get(slider)))
                         )
# btn_phrases = ttk.Button(window, text="Key Phrases")
btn_concurrence = ttk.Button(fr_buttons, text="Concurrence")
btn_concurrence.pack()
btn_concurrence.grid(row=9, column=0, sticky=tk.W, **paddings)

btn_extract.grid(row=12, column=0, sticky=tk.W, **paddings)
btn_extract.pack()
btn_extract.grid(row=12, column=0, sticky=tk.W, **paddings)

btn_exit = ttk.Button(fr_buttons, text="Exit", command=window.quit)
btn_exit.pack()
btn_exit.grid(row=15, column=0, sticky=tk.W, **paddings)

# grid
# btn_upload.grid(row=0, column=0, sticky=tk.W, **paddings)

# menu_label.grid(row=0, column=0, sticky="we", ipadx=0, ipady=0)
# ttk.Label(fr_buttons, text='Select key phrases number').grid(row=1, column=0)
# option.grid(row=3, column=0, sticky=tk.NSEW, padx=0, pady=50)

# slider_label.grid(row=3, column=0, sticky=tk.W, **paddings)
# slider.grid(row=3, column=1, sticky=tk.E, **paddings)

# btn_phrases.grid(row=1, column=0, sticky="we", padx=0, pady=50)
# btn_concurrence.grid(row=6, column=0, sticky=tk.W, **paddings)
# btn_extract.grid(row=9, column=0, sticky=tk.W, **paddings)
# #
# btn_exit.grid(row=12, column=0, sticky=tk.W, **paddings)
#
# fr_buttons.grid(row=0, column=0, sticky=tk.NS)

# txt_edit['state'] = 'disabled'

# text box grid pos in the window
# txt_edit.grid(row=0, column=3, sticky=tk.NS)

# # textbox scrollbar
# scrollbar = ttk.Scrollbar(window, orient='vertical', command=txt_edit.yview)
# scrollbar.grid(row=0, column=1, sticky='ns')
#
# # communicate back to the scrollbar
# txt_edit['yscrollcommand'] = scrollbar.set
# maybe change order of buttons, home, upload/open, extract, show extracted phrases, save the phrases as pdf, exit

# scroll = tk.Scrollbar(window, command=txt_edit.yview)
# txt_edit.configure(yscrollcommand=scroll.set)
# scroll.pack(side=tk.RIGHT, fill=tk.Y)

window.mainloop()

# TO DO:
# tkinter gui tutorials
# try display pdf text in the window just for checking
# sorting out the buttons upload/open button  and extrac button  on the bottom horizontally showing the file browse path
# adding scroll bar to the gui
# LC lectures, NLP lectures and labs
# CV - ip video
# NLE lab 1 and 2 and seminar paper
# class design for python coding


# must do today
# NLE seminar paper and the for-loop
# tk inter videos - at least 2 or 3


# training course prep before monday
# start text pre-processing and finish User interface interactive buttons
# key phrase number button and extraction choice algorithm
# ANLE labs 1 ,2,3
# watch buttons tutorials, -styling buttons , position as well
# rearrange buttons style- but do this later
# make the text box read only and non-editable


# frame arrangements
#  https://stackoverflow.com/questions/45122244/having-frames-next-to-each-other-in-tkinter
# try this as an experiment in extraction process
# https://www.pythontutorial.net/tkinter/ttk-style/
# use disabled buttons lables to make it same as other buttons
