import os
import tkinter as tk
from tkinter import ttk, RIGHT, Y, END, LEFT, BOTH, messagebox
from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *
from turtledemo.penrose import f

import pdfplumber
from extractionMethod import key_phrase_extraction
import tkinter.scrolledtext as scrolledtext
from nltk.tokenize import word_tokenize
from stopwords import get_stopwords

import yake
import nltk

window = tk.Tk()
# the window fits the screen of the user window
width, height = window.winfo_screenwidth(), window.winfo_screenheight()
window_width = 650
window_height = 650

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
    # pathlabel.config(text=os.path.basename(filename),fg="blue")
    # ttk.Button(fr_buttons, text="Upload Pdf File", command=f).grid(column=1, row=0, sticky=tk.W, **paddings)
    print(filename.title())  # printing file path required for extraction

    # extracting/mining all text information in the pdf to text
    all_text = ''
    with pdfplumber.open(filename.title()) as pdf:
        for pdf_page in pdf.pages:
            pdf_page_text = pdf_page.extract_text()
            # print(text)
            # case normalisation of text
            all_text += '\n' + pdf_page_text.lower()

    # # dialog message for checking if correct file name has been uploaded
    # messagebox.showinfo("showinfo", filename + " has been uploaded continue if its the one."
    #                     + "\n" "Otherwise reload to upload ""another" + "\n")

    # file uploading button and function
    ttk.Button(fr_buttons, text="Extract and Display", command=lambda: txt_edit.insert(tk.END,
                                                                                       update_txt(key_phrase_extraction(
                                                                                           all_text, get(var),
                                                                                           get(slider))))).grid(row=9,
                                                                                                                column=0,
                                                                                                                sticky=tk.W,
                                                                                                                **paddings)

    # use a styled disable button with text as the filename being uploaded, white back ground and make slider and
    # menu same size and style to match
    file_name = os.path.basename(filename)
    ttk.Label(fr_buttons, text=("...") + file_name + ("...")).grid(row=0, column=1, sticky=tk.W, **paddings)

    # do the highlighting/ return sentences where key phrases are mentioned in all text

    # co-occurrence button
    btn_concurrence = ttk.Button(fr_buttons, text="Phrase Concurrence Display",
                                 command=lambda: update_txt(all_text))
    btn_concurrence.pack()
    btn_concurrence.grid(row=12, column=0, sticky=tk.W, **paddings)
    print(all_text)


# the get function for getting values/strings from gui input- slider and option buttons
def get(input_variable):
    print(input_variable.get())
    return input_variable.get()


def update_txt(text):
    txt_edit['state'] = 'normal'
    txt_edit.update()
    txt_edit.delete(1.0, tk.END)
    txt_edit.update()
    txt_edit.insert(tk.END, text)
    txt_edit.update()
    txt_edit['state'] = 'disabled'
    txt_edit.update()


# maybe a highlight method for highlighting text


# to be able to highlight and annotate text and  key phrases may be bring the extraction
# method function and do it from here


# def phrase_coocurence(textbox):
#     #  create colour list
#     # color_list = ["red", "yellow"]
#     #     # create key phrase list
#     #   do the yake or rake extraction again depending on the method provided and return  list of key phrases
#     if get(var) == "Algorithm1":
#         # custom_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold,
#         #                                          dedupFunc=deduplication_algo,
#         #                                          windowsSize=windowSize, top=numOfKeywords,
#         #                                          features=None)
#         # keywords = [tup[0] for tup in custom_extractor.extract_keywords(doc_text)]
#         # print(keywords)
#         # for i, word in enumerate(word_tokenize(doc_text)):
#         #     if word in keywords:
#         # use this - simple option
#         #  https://stackoverflow.com/questions/17829713/tkinter-highlight-colour-specific-lines-of-text-based-on-a-keyword
#         # indexing of words for highlighting e.g counting the number characters, positiong number they occur by counting
#         # all words
#         # insert text into the text box then hightlight word
#         word = "ibm"
#         textbox.insert(tk.END, doc_text)
#         textbox.tag_add("one", "1.0", "1.3")
#         # configure the tag
#         textbox.tag_config("one", background="yellow", foreground="blue")
#         # textbox.insert(END, word)
#
#         # try returning the sentences in which the key phrases occur


# creating text box for text display
txt_edit = scrolledtext.ScrolledText(window, undo=True, bd=5, width=100, height=150, relief="flat", wrap=WORD)
txt_edit['font'] = ('consolas', '14')
# txt_edit.config(state='disabled')
txt_edit.pack()
txt_edit.grid(row=0, column=1, sticky=tk.NS, pady=0, padx=0)
txt_edit.columnconfigure(0, weight=20)

# styling the frame
# ttk.Style().configure('TFrame', background='grey', foreground = 'yellow')

# styling all buttons includes 2 buttons used as labels
ttk.Style().configure("TButton", width=21, height=21, padding=5, relief="flat", background="#ccc")

#  styling option menu
menu_style = ttk.Style()
menu_style.configure('TMenubutton', width=10, height=10, padding=0, background="#ccc")

# styling the slider
slider_style = ttk.Style()
slider_style.configure('Horizontal.TScale', width=10, height=10, padding=0, background="#ccc")

# left hand side button frame padding="0.5i"
fr_buttons = ttk.Frame(window, width=100, height=150, relief=tk.RIDGE)
fr_buttons.columnconfigure(0, weight=3)
fr_buttons.columnconfigure(1, weight=1)
fr_buttons.pack()
fr_buttons.grid(row=0, column=0, sticky=tk.NS)

# left hand buttons and grid pos and their padding in the frame
paddings = {'padx': 20, 'pady': 50}
# upload button
btn_upload = ttk.Button(fr_buttons, text="Upload file:", style='TButton')
btn_upload.configure(command=lambda: upload_file())
btn_upload.pack()
btn_upload.grid(row=0, column=0, sticky=tk.W, **paddings)

# option menu
extraction_method_list = [".....Select.....", "Algorithm1", "Algorithm2"]
var = StringVar(fr_buttons)
var.set(extraction_method_list[0])
option = ttk.OptionMenu(fr_buttons, var, *extraction_method_list)
option.pack()
var.trace("w", var.get())
btn_opt_label = ttk.Button(fr_buttons, text='Extraction method:', style='TButton')
btn_opt_label['state'] = 'disabled'
btn_opt_label.pack()
# btn_opt_label.grid(row=6, column=0, sticky=tk.W, **paddings)
btn_opt_label.grid(row=3, column=0, sticky=tk.W, **paddings)
option.grid(row=3, column=1, sticky=tk.W, **paddings)
# .configure(width=25)

# slider button
btn_slider_label = ttk.Button(fr_buttons, text='key phrases number:', style='TButton')
btn_slider_label['state'] = 'disabled'
btn_slider_label.pack()
btn_slider_label.grid(row=6, column=0, sticky=tk.W, **paddings)

slider = tk.Scale(fr_buttons, from_=1, to=20, orient='horizontal')
slider.set(10)
slider.pack()
slider.grid(row=6, column=1, sticky=tk.W, **paddings)

# exit button
btn_exit = ttk.Button(fr_buttons, text="Exit", command=window.quit)
btn_exit.pack()
btn_exit.grid(row=15, column=0, sticky=tk.W, **paddings)

window.mainloop()

# frame arrangements
#  https://stackoverflow.com/questions/45122244/having-frames-next-to-each-other-in-tkinter
# try this as an experiment in extraction process
# https://www.pythontutorial.net/tkinter/ttk-style/
# use disabled buttons lables to make it same as other buttons
# slider.update()
# print(slider.get())
# option.update()
# print(option.get())
# errors in when selecting algorithm option
