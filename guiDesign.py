import tkinter as tk
from tkinter import ttk, RIGHT, Y, END, LEFT, BOTH
from tkinter import filedialog
import pdfplumber
from termcolor import colored

window = tk.Tk()

# the window fits the screen of the user window
width, height = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry('%dx%d+0+0' % (width, height))
window.resizable(False, False)
# making background transparent
# window.attributes('-alpha', 0.94)

# changing the icon by putting the path to the new icon
# window.iconbitmap(......)
window.title("Key phrase Extractor Glossary")
window.rowconfigure(0, minsize=800, weight=2)
window.columnconfigure(1, minsize=500, weight=2)

txt_edit = tk.Text(window, bd=5)

# tk. GROOVE/RAISED it's the type of the button
# try to make it a browse button showing the file path being uploaded

# this is the frame containing the left-hand side buttons
fr_buttons = tk.Frame(window, relief=tk.GROOVE, bd=2, padx=120)

# this is the frame containing the buttons on the right-hand side
fr2_buttons = tk.Frame(window, relief=tk.GROOVE, bd=2, padx=120)


# function to open and upload the pdf file
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
    txt_edit.insert(1.0, all_text)
    # print(all_text)  # working text mined successfully and printing in the terminal
    return all_text

    # highlighting keywords
    # make a read text only gui - not editable
    # use tkinter tag function and watch videos
    key_list = ["cold", "hot", "warm"]
    txt_line = "today is cold may be tomorrow will be hot or warm"
    h_colour = ["on_yellow", "on_green", "on_blue"]

    c_index = 0
    all_text = " "
    # coloured_txt = []
    # for phrase in key_list:
    #     # for col in h_colour:
    #     if phrase in txt_line.split():
    #         # print(phrase + " " + h_colour[c_index])
    #         # coloured_txt.append(colored(phrase, 'white', h_colour[c_index]))
    #         # all_text += '\n' + phrase + " " + h_colour[c_index]
    # all_text += '\n' + "welcome to plus2net"
    # all_text += '\n' + " ".join(coloured_txt)

    # c_index = c_index + 1
    # txt_edit.tag_add()
    # return phrase
    # txt_edit.insert(tk.END, "Welcome to plus2net")
    # txt_edit.tag_add('my_tag', '1.2', '1.13')
    # font1 = ('Times', 'underline')
    # txt_edit.config('my_tag', background='yellow', foreground='red', font=font1)
    # print(all_text)


# function to save the key phrases extracted and their wikipedia definition links
# def phrases_saveAs():


# All left buttons grouped together, their positional grid and frame
# displays a home page for the glossary- description of what it is about
btn_home = ttk.Button(fr_buttons, text="Home")

# displays the extracted key phrases and their definitions - after users exit extract
btn_phrases = ttk.Button(fr_buttons, text="Key Phrases")

# displays key phrases and their definitions after pressed
btn_concurrence = ttk.Button(fr_buttons, text="Concurrence")

# gives the user the choice to save the key phrases they have extracted
btn_save = ttk.Button(fr_buttons, text="Save As...")

# gives the user the choice to save the key phrases they have extracted
btn_exit = ttk.Button(fr_buttons, text="Exit", command=window.quit)

btn_home.grid(row=0, column=0, sticky="we", padx=0, pady=5)
btn_phrases.grid(row=1, column=0, sticky="we", padx=0, pady=5)
btn_concurrence.grid(row=5, column=0, sticky="we", padx=0, pady=5)
# btn_save.grid(row=5, column=0, sticky="we", padx=0, pady=5)
btn_exit.grid(row=7, column=0, sticky="we", padx=0, pady=5)

fr_buttons.grid(row=0, column=0, sticky="ns")

# All right buttons their positional grid and their frame
btn_algo = ttk.Button(fr2_buttons, text="Extracted Algorithm:")

# command lambda allows to open  the file when the button is pressed
btn_upload = ttk.Button(fr2_buttons, text="File Upload", command=lambda: upload_file())

btn_key = ttk.Button(fr2_buttons, text="Key Phrase No:")

# displays the extracted key phrases and their definitions - after users exit extract
btn_extract = ttk.Button(fr2_buttons, text="Extract")

btn_algo.grid(row=0, column=0, sticky="we", padx=0, pady=5)
btn_upload.grid(row=1, column=0, sticky="we", padx=0, pady=5)
btn_key.grid(row=5, column=0, sticky="we", padx=0, pady=5)
btn_extract.grid(row=7, column=0, sticky="we", padx=0, pady=15)

fr2_buttons.grid(row=0, column=2, sticky="ns")

# setting the text box position in the window
txt_edit.grid(row=0, column=1, sticky="ns")

# creating a scrollbar for the textbox
scrollbar = ttk.Scrollbar(window, orient='vertical', command=txt_edit.yview)
scrollbar.grid(row=0, column=1, sticky='ns')

# communicate back to the scrollbar
txt_edit['yscrollcommand'] = scrollbar.set
# maybe change order of buttons, home, upload/open, extract, show extracted phrases, save the phrases as pdf, exit

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
