import tkinter as tk
from tkinter import ttk, RIGHT, Y, END, LEFT, BOTH
from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *
import pdfplumber
from extractionMethod import key_phrase_extraction
import tkinter.scrolledtext as scrolledtext

window = tk.Tk()
# the window fits the screen of the user window
width, height = window.winfo_screenwidth(), window.winfo_screenheight()
window_width = 900
window_height = 900

# find the center point
center_x = int(width / 2 - window_width / 2)
center_y = int(height / 2 - window_height / 2)

# set the position of the window to the center of the screen
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
window.title("Key phrase Extractor Glossary")
window.resizable(1, 1)
window.geometry('%dx%d+0+0' % (width, height))
window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.configure(background='grey')


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

# creating text box for text display
txt_edit = scrolledtext.ScrolledText(window, undo=True, bd=5, width=130, height=150, relief="flat")
txt_edit['font'] = ('consolas', '14')
# txt_edit.config(state='disabled')
txt_edit.pack(expand=True, fill='both')
txt_edit.grid(row=0, column=1, sticky=tk.NS, pady=0, padx=0)

# styles
# styling the frame
# ttk.Style().configure('TFrame', background='grey')

# styling all buttons includes 2 buttons used as labels
ttk.Style().configure("TButton", width=20, height=20, padding=5, relief="flat", background="#ccc")

#  styling option menu
menu_style = ttk.Style()
menu_style.configure('TMenubutton', width=10, height=10, padding=0, background="#ccc")

# styling the slider
slider_style = ttk.Style()
slider_style.configure('Horizontal.TScale', width=10, height=10, padding=0, background="#ccc")

# left hand side button frame
# padding="0.5i"
fr_buttons = ttk.Frame(window, width=100, height=150, relief=tk.RIDGE)
# fr_buttons['padding'] = (55, 55, 55, 55)
fr_buttons.columnconfigure(0, weight=3)
fr_buttons.columnconfigure(1, weight=1)
fr_buttons.pack(expand=True, fill=BOTH)
fr_buttons.grid(row=0, column=0, sticky=tk.NS)


# tkk inter message box for errors e.g insufficient key phrase number


# the get function for getting values/strings from gui input- slider and option buttons
def get(input_variable):
    print(input_variable.get())
    return input_variable.get()


# left hand buttons and grid pos and their padding in the frame
paddings = {'padx': 20, 'pady': 50}

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
btn_opt_label = ttk.Button(fr_buttons, text='Extraction method:', style='TButton')
btn_opt_label['state'] = 'disabled'
btn_opt_label.pack()
btn_opt_label.grid(row=6, column=0, sticky=tk.W, **paddings)
btn_opt_label.grid(row=3, column=0, sticky=tk.W, **paddings)
option.grid(row=3, column=1, sticky=tk.E, **paddings)

btn_slider_label = ttk.Button(fr_buttons, text='key phrases number:', style='TButton')
btn_slider_label['state'] = 'disabled'
btn_slider_label.pack()
btn_slider_label.grid(row=6, column=0, sticky=tk.W, **paddings)
slider = tk.Scale(fr_buttons, from_=1, to=20, orient='horizontal')
# slider.config(width=15,)
slider.set(10)
slider.pack()
slider.grid(row=6, column=1, sticky=tk.E, **paddings)


v = get(var)
s = get(slider)
kp = key_phrase_extraction(doc_text, v, s)

# create a function insert to the require

btn_extract = ttk.Button(fr_buttons, text="Extract", command=lambda: txt_edit.insert(tk.END, kp)

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

# txt_edit.insert(tk.END, "Welcome Floyd")
# txt_edit.config(state='disabled')
# txt_edit.pack(expand=True, fill='both')
# txt_edit.grid(row=0, column=1, sticky=tk.NS, pady=0, padx=0)


window.mainloop()

# message box for errors with any of button functions eg, problem with file upload, empty file for key phrase extraction

# frame arrangements
#  https://stackoverflow.com/questions/45122244/having-frames-next-to-each-other-in-tkinter
# try this as an experiment in extraction process
# https://www.pythontutorial.net/tkinter/ttk-style/
# use disabled buttons lables to make it same as other buttons
