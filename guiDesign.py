import tkinter as tk
from tkinter import ttk, RIGHT, Y, END, LEFT, BOTH
from tkinter import filedialog
from tkinter import *
import pdfplumber

window = tk.Tk()
window.state("zoomed")

# the window fits the screen of the user window
width, height = window.winfo_screenwidth(), window.winfo_screenheight()
# window.geometry('%dx%d+0+0' % (width, height))
window.geometry("1010x1050")
window.resizable(False, False)
# making background transparent
# window.attributes('-alpha', 0.94)

# changing the icon by putting the path to the new icon
# window.iconbitmap(......)
window.title("Key phrase Extractor Glossary")
# window.rowconfigure(0, weight=3)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
# window.columnconfigure(2, minsize=50, weight=1)

txt_edit = tk.Text(window, bd=5, width=100, height=150)


# scroll = tk.Scrollbar(window, command=txt_edit.yview)
# txt_edit.configure(yscrollcommand=scroll.set)


# tk. GROOVE/RAISED it's the type of the button
# try to make it a browse button showing the file path being uploaded

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
            all_text += '\n' + pdf_page_text
    # txt_edit.insert(1.0, all_text)
    # print(all_text)  # working text mined successfully and printing in the terminal
    return all_text


# frames to organise buttons, sliders etc
# this is the frame containing the left-hand side buttons

def button_frames_and_grid():
    # left hand side button frame
    fr_buttons = ttk.Frame(window, width=65, height=100, relief=tk.SUNKEN)
    fr_buttons['padding'] = (55, 55, 55, 55)
    fr_buttons.pack()
    # right hand side buttons frame
    # fr2_buttons = tk.Frame(window, relief=tk.GROOVE, bd=2, padx=310)

    # lef hand buttons and grid pos
    # menu_label = tk.Label(fr_buttons, text="Select extraction method")
    # menu_label.config
    btn_upload = tk.Button(fr_buttons, text="Select file to upload", command=lambda: upload_file())

    extraction_method_list = ["Select extraction method:", "Algorithm1", "Algorithm2"]
    var = StringVar(fr_buttons)
    var.set(extraction_method_list[0])
    option = OptionMenu(fr_buttons, var, "Algorithm1", "Algorithm2")
    # option.config(width=25)
    option.pack(side=tk.TOP)
    # var.trace("w", var.get())

    slider_label = tk.Label(fr_buttons, text='Select key phrases number')
    slider = tk.Scale(fr_buttons, from_=0, to=20, orient='horizontal')
    slider.config(width=25)
    slider.set(10)
    slider.pack()

    btn_extract = tk.Button(fr_buttons, text="Extract")
    # btn_phrases = ttk.Button(fr_buttons, text="Key Phrases")
    btn_concurrence = tk.Button(fr_buttons, text="Concurrence")
    # btn_save = ttk.Button(fr_buttons, text="Save As...")
    btn_exit = tk.Button(fr_buttons, text="Exit", height=3, width=5, command=window.quit)

    # grid
    btn_upload.grid(row=0, column=0, sticky=tk.NSEW, padx=0, pady=50)

    # menu_label.grid(row=0, column=0, sticky="we", ipadx=0, ipady=0)
    option.grid(row=1, column=0, sticky=tk.NSEW, padx=0, pady=50)

    slider_label.grid(row=2, column=0, sticky=tk.NSEW, padx=0, pady=0)
    slider.grid(row=3, column=0, sticky=tk.NSEW, padx=0, pady=50)

    # btn_phrases.grid(row=1, column=0, sticky="we", padx=0, pady=50)
    btn_concurrence.grid(row=4, column=0, sticky=tk.NSEW, padx=0, pady=50)
    # btn_save.grid(row=5, column=0, sticky="we", padx=0, pady=5)
    btn_extract.grid(row=5, column=0, sticky=tk.NSEW, padx=0, pady=50)

    btn_exit.grid(row=6, column=0, sticky=tk.NSEW, padx=0, pady=80)
    # btn_exit.config(height=1, width=2)

    fr_buttons.grid(row=0, column=0, sticky=tk.NS)

    # future right hand side buttons and grid pos
    # fr2_buttons.grid(row=0, column=2, sticky="ns")


button_frames_and_grid()

# text box grid pos in the window
txt_edit.grid(row=0, column=1, sticky=tk.NS)

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
